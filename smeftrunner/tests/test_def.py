import unittest
import numpy as np
import numpy.testing as npt
from smeftrunner import definitions, beta
import test_beta

C = test_beta.C.copy()
for i in C:
    if i in definitions.WC_keys_2f + definitions.WC_keys_4f:
        # make Wilson coefficients involving fermions complex!
        C[i] = C[i] + 1j*C[i]

class TestSymm(unittest.TestCase):
    def test_keys(self):
        # check no parameter or WC was forgotten in the C_symm_keys lists
        self.assertEqual(
          set(definitions.C_keys),
          set([c for cs in definitions.C_symm_keys.values() for c in cs])
        )

    def test_symmetrize_symmetric(self):
        a = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])
        npt.assert_array_equal(definitions.symmetrize_2(a), a)
        b = np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
        npt.assert_array_equal(definitions.symmetrize_2(b), a)

    def test_symmetrize_hermitian(self):
        a = np.array([[1, 2j, 3j], [-2j, 4, 5j], [-3j, -5j, 6]])
        npt.assert_array_equal(definitions.symmetrize_2(a), a)
        b = np.array([[1, 2j, 3j], [0, 4, 5j], [0, 0, 6]])
        npt.assert_array_equal(definitions.symmetrize_2(b), a)

    def test_symmetrize_C(self):
        C_symm = definitions.symmetrize(C)
        # check all keys are present
        self.assertSetEqual(set(C.keys()), set(C_symm.keys()))
        for i, v in C_symm.items():
            # check trivial cases are the same
            if i in definitions.C_symm_keys[0] + definitions.C_symm_keys[1] + definitions.C_symm_keys[3]:
                if definitions.C_keys_shape[i] == 1:
                    self.assertEqual(v, C[i])
                else:
                    npt.assert_array_equal(v, C[i])
            # check symmetric
            elif i in definitions.C_symm_keys[9]:
                npt.assert_array_equal(v, v.T)
            # check hermitian
            elif i in definitions.C_symm_keys[2]:
                npt.assert_array_equal(v, v.T.conj())
            # check 2 identical FFbar
            elif i in definitions.C_symm_keys[4]:
                npt.assert_array_equal(v, v.transpose((2, 3, 0, 1)))
                npt.assert_array_equal(v, v.transpose((1, 0, 3, 2)).conj())
            # check 2 independent FFbar
            elif i in definitions.C_symm_keys[5]:
                npt.assert_array_equal(v, v.transpose((1, 0, 3, 2)).conj())
            # check special case ee
            elif i in definitions.C_symm_keys[6]:
                npt.assert_array_equal(v, v.transpose((2, 3, 0, 1)))
                npt.assert_array_equal(v, v.transpose((0, 3, 2, 1)))
                npt.assert_array_equal(v, v.transpose((2, 1, 0, 3)))
            # check special case qque
            elif i in definitions.C_symm_keys[7]:
                npt.assert_array_equal(v, v.transpose((1, 0, 2, 3)))
            # check special case qqql
            elif i in definitions.C_symm_keys[8]:
                # see eq. (10) of arXiv:1405.0486
                npt.assert_array_almost_equal(v + v.transpose((1, 0, 2, 3)), v.transpose((1, 2, 0, 3)) + v.transpose((2, 1, 0, 3)), decimal=15)

    def test_redundant(self):
        # generate parameter dict filled with unique, ascending numbers
        C_num = beta.C_array2dict(np.arange(0, 9999, dtype=complex))
        C_num_symm = definitions.symmetrize(C_num)
        for k, el in definitions.redundant_elements.items():
            for e in el:
                # check that the elements in the symmetrized array
                # are NOT equal to the original ones IF they belong
                # to the redundant ones
                if k == 'qqql':
                    continue # OK, this doesn't work for qqql...
                self.assertNotEqual(C_num[k][e].real, C_num_symm[k][e].real)
        # generate parameter dict filled with unique, ascending IMAGINARY numbers
        C_num = beta.C_array2dict(1j*np.arange(0, 9999, dtype=complex))
        C_num_symm = definitions.symmetrize(C_num)
        for k, el in definitions.vanishing_im_parts.items():
            for e in el:
                # original im parts are NOT zero
                self.assertNotEqual(C_num[k][e].imag, 0)
                # symmetrized im parts ARE zero
                self.assertEqual(C_num_symm[k][e].imag, 0)

    def test_rephasing(self):
        # some auxiliary functions
        def diagonal_phase_matrix(a1, a2, a3):
            r"""A diagonal $3\times 3$ matrix with $jj$-element $e^{i a_j}$"""
            return np.diag(np.exp(1j*np.array([a1, a2, a3])))
        # from flavio.physics.ckm
        from math import sin, cos
        from cmath import exp
        def ckm_standard(t12, t13, t23, delta):
            c12 = cos(t12)
            c13 = cos(t13)
            c23 = cos(t23)
            s12 = sin(t12)
            s13 = sin(t13)
            s23 = sin(t23)
            return np.array([[c12*c13,
                c13*s12,
                s13/exp(1j*delta)],
                [-(c23*s12) - c12*exp(1j*delta)*s13*s23,
                c12*c23 - exp(1j*delta)*s12*s13*s23,
                c13*s23],
                [-(c12*c23*exp(1j*delta)*s13) + s12*s23,
                -(c23*exp(1j*delta)*s12*s13) - c12*s23,
                c13*c23]])
        # general CKM/PMNS-like matrix
        def unitary_matrix(t12, t13, t23, delta, delta1, delta2, delta3, phi1, phi2):
            ph1 = diagonal_phase_matrix(delta1, delta2, delta3)
            ph2 = diagonal_phase_matrix(-phi1/2, -phi2/2, 0)
            ckm = ckm_standard(t12, t13, t23, delta)
            return np.dot(ph1, np.dot(ckm, ph2))
        # a random unitary matrix
        U = np.array([[-0.4825-0.5529j,  0.6076-0.0129j,  0.1177+0.2798j],
                   [ 0.1227-0.5748j, -0.1685-0.5786j, -0.2349-0.486j ],
                   [-0.0755+0.3322j,  0.5157+0.0393j, -0.7321-0.2837j]])
        f = definitions.mixing_phases(U)
        # check that matrix reconstructed from extracted angles and phases
        # coincides with original matrix
        npt.assert_array_almost_equal(U, unitary_matrix(**f),
            decimal=4)
        # pathological case: unit matrix. Check that everything is zero
        f = definitions.mixing_phases(np.eye(3))
        for k, v in f.items():
            self.assertEqual(v, 0, msg='{} is not zero'.format(k))
        # random mass matrices
        Mu = np.array([[ 0.6126+0.9819j,  0.0165+0.3709j,  0.0114+0.7819j],
            [ 0.6374+0.8631j,  0.1249+0.8346j,  0.6940+0.4495j],
            [ 0.1652+0.9667j,  0.4952+0.1281j,  0.7719+0.2325j]])
        Md = np.array([[ 0.2874+0.2065j,  0.2210+0.9077j,  0.4053+0.454j ],
            [ 0.0339+0.8332j,  0.5286+0.6339j,  0.3142+0.113j ],
            [ 0.9379+0.2952j,  0.8488+0.634j ,  0.1413+0.9175j]])
        UuL, Su, UuR = definitions.msvd(Mu)
        UdL, Sd, UdR = definitions.msvd(Md)
        f = definitions.mixing_phases(UuL.conj().T @ UdL)
        UuL_, UdL_, UuR_, UdR_ = definitions.rephase_standard(UuL, UdL, UuR, UdR)
        # rephased CKM
        K = UuL_.conj().T @ UdL_
        # CKM in standard parametrization
        K_std = unitary_matrix(f['t12'], f['t13'], f['t23'], f['delta'], 0, 0, 0, 0, 0)
        # ... should be equal!
        npt.assert_array_almost_equal(K, K_std, decimal=10)

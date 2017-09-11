import unittest
import numpy as np
import numpy.testing as npt
from smeftrunner import beta, rge, SMEFT, io, definitions
import json
import pkgutil
import pylha

# read in JSON files with numerical input & output of Mathematica code
rpar = json.loads(pkgutil.get_data('smeftrunner', 'tests/data_with_dim5/random_par.json').decode('utf-8'))
rC = json.loads(pkgutil.get_data('smeftrunner', 'tests/data_with_dim5/random_wc.json').decode('utf-8'))
betas_re = json.loads(pkgutil.get_data('smeftrunner', 'tests/data_with_dim5/betas_re.json').decode('utf-8'))
betas_im = json.loads(pkgutil.get_data('smeftrunner', 'tests/data_with_dim5/betas_im.json').decode('utf-8'))


# reconstruct SM parameters
C = {}
C["g"], C["gp"], C["gs"], C["Lambda"], C["m2"] = rpar[:5]
C["Gu"] = np.array(rpar[5]) + 1j*np.array(rpar[6])
C["Gd"] = np.array(rpar[7]) + 1j*np.array(rpar[8])
C["Ge"] = np.array(rpar[9]) + 1j*np.array(rpar[10])
C["Theta"] = C["Thetap"] = 0
C["Thetas"] = 0
HIGHSCALE = 1000

C0 = definitions.WC_keys_0f
C2 = definitions.WC_keys_2f
C4 = definitions.WC_keys_4f

# construct numerical values of Cs
for i, n in enumerate(C0):
    C[n] = rC[0][i]
for i, n in enumerate(C2):
    C[n] = np.array(rC[1][i])
for i, n in enumerate(C4):
    C[n] = np.array(rC[2][i])

class TestBeta(unittest.TestCase):
    def test_beta(self):
        """check that numerical output of Python code equals Mathematica code"""
        my_beta = beta.beta(C, HIGHSCALE)
        self.assertEqual(list(my_beta.keys()), beta.C_keys)
        for k in beta.C_keys:
            if isinstance(my_beta[k], float) or isinstance(my_beta[k], complex):
                self.assertEqual(beta.C_keys_shape[k], 1)
            else:
                self.assertEqual(my_beta[k].shape, beta.C_keys_shape[k], msg=k)
        for i, n in enumerate(C0):
            self.assertAlmostEqual(betas_re[0][i]/my_beta[n].real, 1, places=4)
        for i, n in enumerate(C2):
            npt.assert_array_almost_equal(betas_re[1][i]/my_beta[n].real, np.ones((3,3)), decimal=2)
        for i, n in enumerate(C4):
            npt.assert_array_almost_equal(betas_re[2][i]/my_beta[n].real, np.ones((3,3,3,3)), decimal=2)
        for i, n in enumerate(C2):
            npt.assert_array_almost_equal(betas_im[1][i]/my_beta[n].imag, np.ones((3,3)), decimal=2)
        for i, n in enumerate(C4):
            npt.assert_array_almost_equal(betas_im[2][i]/my_beta[n].imag, np.ones((3,3,3,3)), decimal=2)

    def test_beta_array(self):
        my_beta = beta.beta_array(C, HIGHSCALE)
        n_op = len(C0) + len(C2)*9 + len(C4)*81
        # shape is no. of op.s + no. of SM parameters
        self.assertEqual(my_beta.shape, (n_op + 5 + 3*9 + 3,))

    def test_array2dict(self):
        d1 = beta.C_array2dict(beta.beta_array(C,  HIGHSCALE))
        d2 = beta.beta(C, HIGHSCALE)
        for k in d1:
            npt.assert_array_equal(d1[k], d2[k])
        d3 = beta.C_array2dict(beta.C_dict2array(C))
        for k in d3:
            npt.assert_array_equal(d3[k], C[k])

class TestRGE(unittest.TestCase):
    def test_rgell(self):
        # evolve only a very small bit and check that LL approximation
        # and full result agree
        C_out_ll = rge.smeft_evolve_leadinglog(C_in=C, scale_high=HIGHSCALE, scale_in=1000, scale_out=950)
        C_out = rge.smeft_evolve(C_in=C, scale_high=HIGHSCALE, scale_in=1000, scale_out=950)
        for n in C0:
            self.assertAlmostEqual((C_out[n]/C_out_ll[n]).real, 1, places=1)
        for n in C2:
            npt.assert_array_almost_equal(C_out[n]/C_out_ll[n], np.ones((3,3)), decimal=1)
        for n in C4:
            npt.assert_array_almost_equal((C_out[n]/C_out_ll[n]).real, np.ones((3,3,3,3)), decimal=1,
                err_msg="failed for {}".format(n))

class TestClasses(unittest.TestCase):
    def test_smeft(self):
        # just check this doesn't raise errors
        smeft = SMEFT()
        with self.assertRaises(Exception):
            # no initial condition set
            smeft.rgevolve(scale_out=900)
        smeft.C_in = 1
        with self.assertRaises(Exception):
            # no initial scale set
            smeft.rgevolve(scale_out=900)
        smeft.set_initial(C_in=C, scale_in=1000, scale_high=1000)
        smeft.rgevolve(scale_out=900)
        smeft.rgevolve_leadinglog(scale_out=900)

class TestIO(unittest.TestCase):
    def test_lhamatrix(self):
        M = np.random.rand(2,3,4)
        values = io.matrix2lha(M)
        M2 = io.lha2matrix(values, (2,3,4))
        npt.assert_array_equal(M, M2)

    def test_load(self):
        sm = pkgutil.get_data('smeftrunner', 'tests/data/SMInput-CPV.dat').decode('utf-8')
        wc = pkgutil.get_data('smeftrunner', 'tests/data/WCsInput-CPV-SMEFT.dat').decode('utf-8')
        wcout = pkgutil.get_data('smeftrunner', 'tests/data/Output_SMEFTrunner.dat').decode('utf-8')
        io.sm_lha2dict(pylha.load(sm))
        io.wc_lha2dict(pylha.load(wc))
        CSM = io.sm_lha2dict(pylha.load(wcout))
        C = io.wc_lha2dict(pylha.load(wcout))
        C2 = io.wc_lha2dict(io.wc_dict2lha(C))
        for k in C:
            npt.assert_array_equal(C[k], C2[k])
        smeft = SMEFT()
        smeft.load_initial((wcout,))
        for k in C:
            npt.assert_array_equal(C[k], smeft.C_in[k], err_msg="Failed for {}".format(k))
        for k in CSM:
            npt.assert_array_equal(CSM[k], smeft.C_in[k], err_msg="Failed for {}".format(k))
        CSM2 = io.sm_lha2dict(io.sm_dict2lha(CSM))
        for k in CSM:
            npt.assert_array_equal(CSM[k], CSM2[k], err_msg="Failed for {}".format(k))

    def test_dump(self):
        wcout = pkgutil.get_data('smeftrunner', 'tests/data/Output_SMEFTrunner.dat').decode('utf-8')
        smeft = SMEFT()
        smeft.load_initial((wcout,))
        smeft.scale_in = 1000
        smeft.scale_high = 1000
        C_out = smeft.rgevolve(scale_out=900)
        C_dump = smeft.dump(C_out)
        smeft.load_initial((C_dump,))
        for k in C_out:
            npt.assert_array_almost_equal(C_out[k].real, smeft.C_in[k].real, err_msg="Failed for {}".format(k))

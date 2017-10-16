import unittest
import numpy as np
import numpy.testing as npt
from smeftrunner import SMEFT
from test_beta import C

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

    def test_rotation(self):
        smeft = SMEFT()
        smeft.set_initial(C_in=C, scale_in=1000, scale_high=1000)
        C_out = smeft.rgevolve(scale_out=160)
        C_rot = smeft.rotate_defaultbasis(C_out)
        # check that input & output dicts have same keys
        self.assertSetEqual(set(C_out.keys()), set(C_rot.keys()))
        # new parameter point with diagonal sorted positive Yukawas and vanishing C_Xphi
        C_new = C.copy()
        for k in ['Gu', 'Gd', 'Ge']:
            C_new[k] = np.diag(np.sort(np.abs(np.diag(C[k]))))
        for k in ['uphi', 'dphi', 'ephi']:
            C_new[k] = np.zeros((3,3))
        smeft_new = SMEFT()
        smeft_new.set_initial(C_new, scale_in=160, scale_high=1000)
        C_new_rot = smeft_new.rotate_defaultbasis(C_new)
        for k in C_new:
            # now all the WCs & parameters should be rotation invariant!
            npt.assert_array_equal(C_new[k], C_new_rot[k])

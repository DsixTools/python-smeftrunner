import unittest
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

import unittest
import numpy as np
import numpy.testing as npt
from beta import beta, beta_array
import json

# read in JSON files with numerical input & output of Mathematica code
rpar = json.load(open('random_par.json', 'r'))
rC = json.load(open('random_wc.json', 'r'))
betas_re = json.load(open('betas_re.json', 'r'))
betas_im = json.load(open('betas_im.json', 'r'))

# reconstruct SM parameters
C = {}
C["g"], C["gp"], C["gs"], C["Lambda"], C["m2"] = rpar[:5]
C["Gu"] = np.array(rpar[5]) + 1j*np.array(rpar[6])
C["Gd"] = np.array(rpar[7]) + 1j*np.array(rpar[8])
C["Ge"] = np.array(rpar[9]) + 1j*np.array(rpar[10])
C["HIGHSCALE"] = 1000

# names of Cs with 0, 2, or 4 fermions (i.e. scalars, 3x3 matrices, and 3x3x3x3 tensors)
C0 = ["G", "Gtilde", "W", "Wtilde", "CurlyPhi", "CurlyPhiEmptySquare", "CurlyPhiD", "CurlyPhiG", "CurlyPhiB", "CurlyPhiW", "CurlyPhiWB", "CurlyPhiGtilde", "CurlyPhiBtilde", "CurlyPhiWtilde", "CurlyPhiWtildeB"]
C2 = ["uCurlyPhi", "dCurlyPhi", "eCurlyPhi", "eW", "eB", "uG", "uW", "uB", "dG", "dW", "dB", "CurlyPhil1", "CurlyPhil3", "CurlyPhie", "CurlyPhiq1", "CurlyPhiq3", "CurlyPhiu", "CurlyPhid", "CurlyPhiud"]
C4 = ["ll", "qq1", "qq3", "lq1", "lq3", "ee", "uu", "dd", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1", "qd1", "qu8", "qd8", "ledq", "quqd1", "quqd8", "lequ1", "lequ3", "duql", "qque", "qqql", "duue"]

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
        my_beta = beta(C)
        for i, n in enumerate(C0):
            self.assertAlmostEqual(betas_re[0][i]/my_beta[n].real, 1, places=4)
        for i, n in enumerate(C2):
            npt.assert_array_almost_equal(betas_re[1][i]/my_beta[n].real, np.ones((3,3)), decimal=4)
        for i, n in enumerate(C4):
            npt.assert_array_almost_equal(betas_re[2][i]/my_beta[n].real, np.ones((3,3,3,3)), decimal=2)
        for i, n in enumerate(C2):
            npt.assert_array_almost_equal(betas_im[1][i]/my_beta[n].imag, np.ones((3,3)), decimal=4)
        for i, n in enumerate(C4):
            npt.assert_array_almost_equal(betas_im[2][i]/my_beta[n].imag, np.ones((3,3,3,3)), decimal=2)

    def test_beta_array(self):
        my_beta = beta_array(C)
        n_op = len(C0) + len(C2)*9 + len(C4)*81
        # shape is no. of op.s + no. of SM parameters
        self.assertEqual(my_beta.shape, (n_op + 5 + 3*9 + 3,))

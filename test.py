import unittest
import numpy as np
import numpy.testing as npt
from beta import beta
import json

rpar = json.load(open('random_par.json', 'r'))
rwc = json.load(open('random_wc.json', 'r'))
betas_re = json.load(open('betas_re.json', 'r'))
betas_im = json.load(open('betas_im.json', 'r'))

g, gp, gs, Lambda, m2 = rpar[:5]
Gu = np.array(rpar[5]) + 1j*np.array(rpar[6])
Gd = np.array(rpar[7]) + 1j*np.array(rpar[8])
Ge = np.array(rpar[9]) + 1j*np.array(rpar[10])
HIGHSCALE = 1000

WC0 = ["G", "Gtilde", "W", "Wtilde", "CurlyPhi", "CurlyPhiEmptySquare", "CurlyPhiD", "CurlyPhiG", "CurlyPhiB", "CurlyPhiW", "CurlyPhiWB", "CurlyPhiGtilde", "CurlyPhiBtilde", "CurlyPhiWtilde", "CurlyPhiWtildeB"]
WC2 = ["uCurlyPhi", "dCurlyPhi", "eCurlyPhi", "eW", "eB", "uG", "uW", "uB", "dG", "dW", "dB", "CurlyPhil1", "CurlyPhil3", "CurlyPhie", "CurlyPhiq1", "CurlyPhiq3", "CurlyPhiu", "CurlyPhid", "CurlyPhiud"]
WC4 = ["ll", "qq1", "qq3", "lq1", "lq3", "ee", "uu", "dd", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1", "qd1", "qu8", "qd8", "ledq", "quqd1", "quqd8", "lequ1", "lequ3", "duql", "qque", "qqql", "duue"]

WC = {}
for i, n in enumerate(WC0):
    WC[n] = rwc[0][i]
for i, n in enumerate(WC2):
    WC[n] = np.array(rwc[1][i])
for i, n in enumerate(WC4):
    WC[n] = np.array(rwc[2][i])

class TestBeta(unittest.TestCase):

    def test_beta(self):
        my_beta = beta(g, gp, gs, m2, Lambda, Gu, Gd, Ge, HIGHSCALE, WC)
        for i, n in enumerate(WC0):
            self.assertAlmostEqual(betas_re[0][i]/my_beta[n].real, 1, places=4)
        for i, n in enumerate(WC2):
            npt.assert_array_almost_equal(betas_re[1][i]/my_beta[n].real, np.ones((3,3)), decimal=4)
        for i, n in enumerate(WC4):
            npt.assert_array_almost_equal(betas_re[2][i]/my_beta[n].real, np.ones((3,3,3,3)), decimal=2)
        for i, n in enumerate(WC2):
            npt.assert_array_almost_equal(betas_im[1][i]/my_beta[n].imag, np.ones((3,3)), decimal=4)
        for i, n in enumerate(WC4):
            npt.assert_array_almost_equal(betas_im[2][i]/my_beta[n].imag, np.ones((3,3,3,3)), decimal=2)

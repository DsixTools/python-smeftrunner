import unittest
import numpy as np
from beta import beta

class TestBeta(unittest.TestCase):
    def test_beta(self):
        G_u = np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
        G_d = np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
        G_e = np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
        g = 1
        gp = 1
        gs = 1
        m = 1
        HIGHSCALE = 1
        Lambda = 1

        WC={}

        #1D
        WC["G"]=1
        WC["Gtilde"]=1
        WC["W"]=1
        WC["Wtilde"]=1
        WC["CurlyPhi"]=1
        WC["CurlyPhiEmptySquare"]=1
        WC["CurlyPhiD"]=1
        WC["CurlyPhiG"]=1
        WC["CurlyPhiB"]=1
        WC["CurlyPhiW"]=1
        WC["CurlyPhiWB"]=1
        WC["CurlyPhiGtilde"]=1
        WC["CurlyPhiBtilde"]=1
        WC["CurlyPhiWtilde"]=1
        WC["CurlyPhiWtildeB"]=1

        #2D
        x=np.matrix(np.arange(9).reshape((3,3))+1j*np.arange(9).reshape((3,3)))
        WC["uCurlyPhi"]=x
        WC["dCurlyPhi"]=x
        WC["eCurlyPhi"]=x
        WC["eW"]=x
        WC["eB"]=x
        WC["uG"]=x
        WC["uW"]=x
        WC["uB"]=x
        WC["dG"]=x
        WC["dW"]=x
        WC["dB"]=x
        WC["CurlyPhil1"]=x
        WC["CurlyPhil3"]=x
        WC["CurlyPhie"]=x
        WC["CurlyPhiq1"]=x
        WC["CurlyPhiq3"]=x
        WC["CurlyPhiu"]=x
        WC["CurlyPhid"]=x
        WC["CurlyPhiud"]=x

        #4D
        y=np.arange(81).reshape(3,3,3,3)
        WC["ll"]=y
        WC["qq1"]=y
        WC["qq3"]=y
        WC["lq1"]=y
        WC["lq3"]=y
        WC["ee"]=y
        WC["uu"]=y
        WC["dd"]=y
        WC["eu"]=y
        WC["ed"]=y
        WC["ud1"]=y
        WC["ud8"]=y
        WC["le"]=y
        WC["lu"]=y
        WC["ld"]=y
        WC["qe"]=y
        WC["qu1"]=y
        WC["qd1"]=y
        WC["qu8"]=y
        WC["qd8"]=y
        WC["ledq"]=y
        WC["quqd1"]=y
        WC["quqd8"]=y
        WC["lequ1"]=y
        WC["lequ3"]=y
        WC["duql"]=y
        WC["qque"]=y
        WC["qqql"]=y
        WC["duue"]=y

        # just check this runs without error
        beta(g, gp, gs, m, Lambda, G_u, G_d, G_e, HIGHSCALE, WC)

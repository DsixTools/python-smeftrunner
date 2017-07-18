# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:38:21 2017

@author: Xuanyou
"""

import numpy as np



#Parameters
G_u = np.matrix(np.empty([3,3]))
G_d = np.matrix(np.empty([3,3]))
G_e = np.matrix(np.empty([3,3]))
g
gp
gs
m
HIGHSCALE
Lambda
I3 = np.identity(3)


#Functions previous defined...  #c.c.   # i in eta5
Eta1=(3*np.trace(WC["uCurlyPhi"]@G_u.getH())+3*np.trace(WC["dCurlyPhi"]@G_d.getH())+np.trace(WC["eCurlyPhi"]@G_e.getH())+3*np.conj(np.trace(WC["uCurlyPhi"]@G_u.getH()))+3*np.conj(np.trace(WC["dCurlyPhi"]@G_d.getH()))+np.conj(np.trace(WC["eCurlyPhi"]@G_e.getH())))/2
Eta2=-6*np.trace(WC["CurlyPhiq3"]@G_u@G_u.getH())-6*np.trace(WC["CurlyPhiq3"]@G_d@G_d.getH())-2*np.trace(WC["CurlyPhil3"]@G_e@G_e.getH())+3*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+np.conj(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)))
Eta3=3*np.trace(WC["CurlyPhiq1"]@G_d@G_d.getH())-3*np.trace(WC["CurlyPhiq1"]@G_u@G_u.getH())+9*np.trace(WC["CurlyPhiq3"]@G_d@G_d.getH())+9*np.trace(WC["CurlyPhiq3"]@G_u@G_u.getH())+3*np.trace(WC["CurlyPhiu"]@G_u.getH()@G_u)-3*np.trace(WC["CurlyPhid"]@G_d.getH()@G_d)-3*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+np.conj(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)))+np.trace(WC["CurlyPhil1"]@G_e@G_e.getH())+3*np.trace(WC["CurlyPhil3"]@G_e@G_e.getH())-np.trace(WC["CurlyPhie"]@G_e.getH()@G_e)
Eta4=12*np.trace(WC["CurlyPhiq1"]@G_d@G_d.getH())-12*np.trace(WC["CurlyPhiq1"]@G_u@G_u.getH())+12*np.trace(WC["CurlyPhiu"]@G_u.getH()@G_u)-12*np.trace(WC["CurlyPhid"]@G_d.getH()@G_d)+6*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+np.conj(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)))+4*np.trace(WC["CurlyPhil1"]@G_e@G_e.getH())-4*np.trace(WC["CurlyPhie"]@G_e.getH()@G_e)
Eta5=1j*3/2*(np.trace(G_d@WC["dCurlyPhi"].getH())-np.conj(np.trace(G_d@WC["dCurlyPhi"].getH())))-1j*3/2*(np.trace(G_u@WC["uCurlyPhi"].getH())-np.conj(np.trace(G_u@WC["uCurlyPhi"].getH())))+1j*1/2*(np.trace(G_e@WC["eCurlyPhi"].getH())-np.conj(np.trace(G_e@WC["eCurlyPhi"].getH())))

GammaH=np.trace(3*G_u@G_u.getH()+3*G_d@G_d.getH()+G_e@G_e.getH())
Gammaq=1/2*(G_u@G_u.getH()+G_d@G_d.getH())
Gammau=G_u.getH()@G_u
Gammad=G_d.getH()@G_d
Gammal=1/2*G_e@G_e.getH()
Gammae=G_e.getH()@G_e

XiB=2/3*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])+8/3*(-np.trace(WC["CurlyPhil1"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhie"])+2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"]))
Xie=2*np.einsum("prst,rs", WC["le"], G_e)-3*np.einsum("ptsr,rs", WC["ledq"], G_d)+3*np.einsum("ptsr,sr", WC["lequ1"], np.conj(G_u))
Xid=2*(np.einsum("prst,rs", WC["qd1"], G_d)+4/3*np.einsum("prst,rs", WC["qd8"], G_d))-(3*np.einsum("srpt,sr", WC["quqd1"], np.conj(G_u))+1/2*(np.einsum("prst,sr", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("prst,sr", WC["quqd8"], np.conj(G_u))))-np.einsum("srtp,sr", np.conj(WC["ledq"]), G_e)
Xiu=2*(np.einsum("prst,rs", WC["qu1"], G_u)+4/3*np.einsum("prst,rs", WC["qu8"], G_u))-(3*np.einsum("ptsr,sr", WC["quqd1"], np.conj(G_d))+1/2*(np.einsum("stpr,sr", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("stpr,sr", WC["quqd8"], np.conj(G_d))))+np.einsum("srpt,sr", WC["lequ1"], np.conj(G_e))




#Beta function, WC as 2 dictionaries
Beta = {}
WC = {}

#equations of beta functions
Beta["g"]=-19/6*g**3-8*g*m**2/HIGHSCALE**2*WC["CurlyPhiW"]


Beta["gp"]=41/6*gp**3-8*gp*m**2/HIGHSCALE**2*WC["CurlyPhiB"]


Beta["gs"]=-7*gs**3-8*gs*m**2/HIGHSCALE**2*WC["CurlyPhiG"]


Beta["Lambda"]=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)*Lambda+4*Lambda*GammaH-4*(3*np.trace(G_d@G_d.getH()@G_d@G_d.getH()@)+3*np.trace(G_u@G_u.getH()@G_u@G_u.getH()@)+np.trace(G_e@G_e.getH()@G_e@G_e.getH()@))+4*m**2/HIGHSCALE**2*(12*WC["CurlyPhi"]+(-16*Lambda+10/3*g**2)*WC["CurlyPhiEmptySquare"]+(6*Lambda+3/2*(gp**2-g**2))*WC["CurlyPhiD"]+2*(Eta1+Eta2)+9*g**2*WC["CurlyPhiW"]+3*gp**2*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))


Beta["m**2"]=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH+4*m**2/HIGHSCALE**2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"]))


Beta["G_u"]=3/2*(G_u@G_u.getH()@G_u-G_d@G_d.getH()@G_u)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)@G_u+2*m**2/HIGHSCALE**2*(3*WC["uCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])@G_u-WC["CurlyPhiq1"].getH()@G_u+3*WC["CurlyPhiq3"].getH()@G_u+G_u@WC["CurlyPhiu"].getH()-G_d@WC["CurlyPhiud"].getH()-2*(np.einsum("rpts,pt", WC["qu1"], G_u)+4/3*np.einsum("rpts,pt", WC["qu8"], G_u))-np.einsum("ptrs,pt", WC["lequ1"], np.conj(G_e))+3*np.einsum("rspt,pt", WC["quqd1"], np.conj(G_d))+1/2*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d))))


Beta["G_d"]=3/2*(G_d@G_d.getH()@G_d-G_u@G_u.getH()@G_d)+(GammaH-9/4*g**2-5/12*gp**2-8*gs**2)@G_d+2*m**2/HIGHSCALE**2*(3*WC["dCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])@G_d+WC["CurlyPhiq1"].getH()@G_d+3*WC["CurlyPhiq3"].getH()@G_d-G_d@WC["CurlyPhid"].getH()-G_u@CCurlyPhiud-2*(np.einsum("rpts,pt", WC["qd1"], G_d)+4/3*np.einsum("rpts,pt", WC["qd8"], G_d))+np.einsum("ptsr,tp", np.conj(WC["ledq"]), np.conj(G_e))+3*np.einsum("ptrs,pt", WC["quqd1"], np.conj(G_u))+1/2*(np.einsum("rpts,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rpts,pt", WC["quqd8"], np.conj(G_u))))


Beta["G_e"]=3/2*G_e@G_e.getH()@G_e+(GammaH-3/4*(3*g**2+5*gp**2))*G_e+2*m**2/HIGHSCALE**2*(3*WC["eCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])@G_e+WC["CurlyPhil1"].getH()@G_e+3*WC["CurlyPhil3"].getH()@G_e-G_e@WC["CurlyPhie"].getH()-2*np.einsum("rpts,pt", WC["le"], G_e)+3*np.einsum("rspt,tp", WC["ledq"], G_d)-3*np.einsum("rspt,pt", WC["lequ1"], np.conj(G_u)))


Beta["Theta"]=-128*np.pi**2/g**2*m**2/HIGHSCALE**2*WC["CurlyPhiWtilde"]


Beta["Thetap"]=-128*np.pi**2/gp**2*m**2/HIGHSCALE**2*WC["CurlyPhiBtilde"]


Beta["Thetas"]=-128*np.pi**2/gs**2*m**2/HIGHSCALE**2*WC["CurlyPhiGtilde"]


Beta["G"]=15*gs**2*WC["G"]


Beta["Gtilde"]=15*gs**2*WC["Gtilde"]


Beta["W"]=29/2*g**2*WC["W"]


Beta["Wtilde"]=29/2*g**2*WC["Wtilde"]

#c.c.
Beta["CurlyPhi"]=-9/2*(3*g**2+gp**2)*WC["CurlyPhi"]+Lambda*(20/3*g**2*WC["CurlyPhiEmptySquare"]+3*(gp**2-g**2)*WC["CurlyPhiD"])-3/4*(g**2+gp**2)**2*WC["CurlyPhiD"]+6*Lambda*(3*g**2*WC["CurlyPhiW"]+gp**2*WC["CurlyPhiB"]+g*gp*WC["CurlyPhiWB"])-3*(g**2*gp**2+3*g**4)*WC["CurlyPhiW"]-3*(gp**4+g**2*gp**2)*WC["CurlyPhiB"]-3*(g*gp**3+g**3*gp)*WC["CurlyPhiWB"]+8/3*Lambda*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))+54*Lambda*WC["CurlyPhi"]-40*Lambda**2*WC["CurlyPhiEmptySquare"]+12*Lambda**2*WC["CurlyPhiD"]+4*Lambda*(Eta1+Eta2)-4*(3*np.trace(WC["uCurlyPhi"]@G_u.getH()@G_u@G_u.getH())+3*np.trace(WC["dCurlyPhi"]@G_d.getH()@G_d@G_d.getH())+np.trace(WC["eCurlyPhi"]@G_e.getH()@G_e@G_e.getH())+3*np.conj(np.trace(WC["uCurlyPhi"]@G_u.getH()@G_u@G_u.getH()))+3*np.conj(np.trace(WC["dCurlyPhi"]@G_d.getH()@G_d@G_d.getH()))+np.conj(np.trace(WC["eCurlyPhi"]@G_e.getH()@G_e@G_e.getH())))+6*GammaH*WC["CurlyPhi"]


Beta["CurlyPhiEmptySquare"]=-(4*g**2+4/3*gp**2)*WC["CurlyPhiEmptySquare"]+5/3*gp**2*WC["CurlyPhiD"]+2*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))+2/3*gp**2*(2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"])-np.trace(WC["CurlyPhie"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhil1"]))+12*Lambda*WC["CurlyPhiEmptySquare"]-2*Eta3+4*GammaH*WC["CurlyPhiEmptySquare"]


Beta["CurlyPhiD"]=20/3*gp**2*WC["CurlyPhiEmptySquare"]+(9/2*g**2-5/6*gp**2)*WC["CurlyPhiD"]+8/3*gp**2*(2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"])-np.trace(WC["CurlyPhie"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhil1"]))+6*Lambda*WC["CurlyPhiD"]-2*Eta4+4*GammaH*WC["CurlyPhiD"]

#c.c.
Beta["CurlyPhiG"]=(-3/2*gp**2-9/2*g**2-14*gs**2)*WC["CurlyPhiG"]+6*Lambda*WC["CurlyPhiG"]-2*gs*(np.trace(WC["uG"]@G_u.getH())+np.trace(WC["dG"]@G_d.getH())+np.conj(np.trace(WC["uG"]@G_u.getH()))+np.conj(np.trace(WC["dG"]@G_d.getH())))+2*GammaH*WC["CurlyPhiG"]

#c.c.
Beta["CurlyPhiB"]=(85/6*gp**2-9/2*g**2)*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+6*Lambda*WC["CurlyPhiB"]+gp*(-5*np.trace(WC["uB"]@G_u.getH())+np.trace(WC["dB"]@G_d.getH())+3*np.trace(WC["eB"]@G_e.getH())-5*np.conj(np.trace(WC["uB"]@G_u.getH()))+np.conj(np.trace(WC["dB"]@G_d.getH()))+3*np.conj(np.trace(WC["eB"]@G_e.getH())))+2*GammaH*WC["CurlyPhiB"]

#c.c.
Beta["CurlyPhiW"]=(-3/2*gp**2-53/6*g**2)*WC["CurlyPhiW"]+g*gp*WC["CurlyPhiWB"]-15*g**3*WC["W"]+6*Lambda*WC["CurlyPhiW"]-g*(3*np.trace(WC["uW"]@G_u.getH())+3*np.trace(WC["dW"]@G_d.getH())+np.trace(WC["eW"]@G_e.getH())+3*np.conj(np.trace(WC["uW"]@G_u.getH()))+3*np.conj(np.trace(WC["dW"]@G_d.getH()))+np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiW"]

#c.c.
Beta["CurlyPhiWB"]=(19/3*gp**2+4/3*g**2)*WC["CurlyPhiWB"]+2*g*gp*(WC["CurlyPhiB"]+WC["CurlyPhiW"])+3*g**2*gp*WC["W"]+2*Lambda*WC["CurlyPhiWB"]+g*(3*np.trace(WC["uB"]@G_u.getH())-3*np.trace(WC["dB"]@G_d.getH())-np.trace(WC["eB"]@G_e.getH())+3*np.conj(np.trace(WC["uB"]@G_u.getH()))-3*np.conj(np.trace(WC["dB"]@G_d.getH()))-np.conj(np.trace(WC["eB"]@G_e.getH())))+gp*(5*np.trace(WC["uW"]@G_u.getH())+np.trace(WC["dW"]@G_d.getH())+3*np.trace(WC["eW"]@G_e.getH())+5*np.conj(np.trace(WC["uW"]@G_u.getH()))+np.conj(np.trace(WC["dW"]@G_d.getH()))+3*np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiWB"]

#problem with i as I*iCPV
Beta["CurlyPhiGtilde"]=(-3/2*gp**2-9/2*g**2-14*gs**2)*WC["CurlyPhiGtilde"]+6*Lambda*WC["CurlyPhiGtilde"]+2j*gs*(np.trace(WC["uG"]@G_u.getH())+np.trace(WC["dG"]@G_d.getH())-np.conj(np.trace(WC["uG"]@G_u.getH()))-np.conj(np.trace(WC["dG"]@G_d.getH())))+2*GammaH*WC["CurlyPhiGtilde"]

#i
Beta["CurlyPhiBtilde"]=(85/6*gp**2-9/2*g**2)*WC["CurlyPhiBtilde"]+3*g*gp*WC["CurlyPhiWtildeB"]+6*Lambda*WC["CurlyPhiBtilde"]-1j*gp*(-5*np.trace(WC["uB"]@G_u.getH())+np.trace(WC["dB"]@G_d.getH())+3*np.trace(WC["eB"]@G_e.getH())+5*np.conj(np.trace(WC["uB"]@G_u.getH()))-np.conj(np.trace(WC["dB"]@G_d.getH()))-3*np.conj(np.trace(WC["eB"]@G_e.getH())))+2*GammaH*WC["CurlyPhiBtilde"]

#i
Beta["CurlyPhiWtilde"]=(-3/2*gp**2-53/6*g**2)*WC["CurlyPhiWtilde"]+g*gp*WC["CurlyPhiWtildeB"]-15*g**3*WC["Wtilde"]+6*Lambda*WC["CurlyPhiWtilde"]+1j*g*(3*np.trace(WC["uW"]@G_u.getH())+3*np.trace(WC["dW"]@G_d.getH())+np.trace(WC["eW"]@G_e.getH())-3*np.conj(np.trace(WC["uW"]@G_u.getH()))-3*np.conj(np.trace(WC["dW"]@G_d.getH()))-np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiWtilde"]

#i
Beta["CurlyPhiWtildeB"]=(19/3*gp**2+4/3*g**2)*WC["CurlyPhiWtildeB"]+2*g*gp*(WC["CurlyPhiBtilde"]+WC["CurlyPhiWtilde"])+3*g**2*gp*WC["Wtilde"]+2*Lambda*WC["CurlyPhiWtildeB"]-1j*g*(3*np.trace(WC["uB"]@G_u.getH())-3*np.trace(WC["dB"]@G_d.getH())-np.trace(WC["eB"]@G_e.getH())-3*np.conj(np.trace(WC["uB"]@G_u.getH()))+3*np.conj(np.trace(WC["dB"]@G_d.getH()))+np.conj(np.trace(WC["eB"]@G_e.getH())))-1j*gp*(5*np.trace(WC["uW"]@G_u.getH())+np.trace(WC["dW"]@G_d.getH())+3*np.trace(WC["eW"]@G_e.getH())-5*np.conj(np.trace(WC["uW"]@G_u.getH()))-np.conj(np.trace(WC["dW"]@G_d.getH()))-3*np.conj(np.trace(WC["eW"]@G_e.getH())))+2*GammaH*WC["CurlyPhiWtildeB"]

#i  #the coefficients of Eta5 is not equal
Beta["uCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])+17/3*gp**2*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"])-g*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))@G_u-(35/12*gp**2+27/4*g**2+8*gs**2)*WC["uCurlyPhi"]-gp*(5*gp**2-3*g**2)*WC["uB"]+g*(5*gp**2-9*g**2)*WC["uW"]-(3*g**2-gp**2)*G_u@WC["CurlyPhiu"]+3*g**2*G_d@WC["CurlyPhiud"].getH()+4*gp**2*WC["CurlyPhiq1"]@G_u-4*gp**2*WC["CurlyPhiq3"]@G_u-5*gp*(WC["uB"]@G_u.getH()@G_u+G_u@G_u.getH()@WC["uB"])-3*g*(WC["uW"]@G_u.getH()@G_u-G_u@G_u.getH()@WC["uW"])-16*gs*(WC["uG"]@G_u.getH()@G_u+G_u@G_u.getH()@WC["uG"])-12*g*G_d@G_d.getH()@WC["uW"]-6*g*WC["dW"]@G_d.getH()@G_u+Lambda*(12*WC["uCurlyPhi"]-2*WC["CurlyPhiq1"]@G_u+6*WC["CurlyPhiq3"]@G_u+2*G_u@WC["CurlyPhiu"]-2*G_d@WC["CurlyPhiud"].getH()-2*WC["CurlyPhiEmptySquare"]@G_u+WC["CurlyPhiD"]@G_u-4*np.einsum("rpts,pt", WC["qu1"], G_u)-16/3*np.einsum("rpts,pt", WC["qu8"], G_u)-2*np.einsum("ptrs,pt", WC["lequ1"], np.conj(G_e))+6*np.einsum("rspt,pt", WC["quqd1"], np.conj(G_d))+np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))+2*(Eta1+Eta2-1j*Eta5)@G_u+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])@G_u@G_u.getH()@G_u-2*WC["CurlyPhiq1"]@G_u@G_u.getH()@G_u+6*WC["CurlyPhiq3"]@G_d@G_d.getH()@G_u+2*G_u@G_u.getH()@G_u@WC["CurlyPhiu"]-2*G_d@G_d.getH()@G_d@WC["CurlyPhiud"].getH()+8*(np.einsum("rpts,pt", WC["qu1"], G_u@G_u.getH()@G_u)+4/3*np.einsum("rpts,pt", WC["qu8"], G_u@G_u.getH()@G_u))-2*(np.einsum("tsrp,pt", WC["quqd1"], G_d.getH()@G_d@G_d.getH())+4/3*np.einsum("tsrp,pt", WC["quqd8"], G_d.getH()@G_d@G_d.getH()))-12*np.einsum("rstp,pt", WC["quqd1"], G_d.getH()@G_d@G_d.getH())+4*np.einsum("tprs,pt", WC["lequ1"], G_e@G_e.getH()@G_e)+4*WC["uCurlyPhi"]@G_u.getH()@G_u+5*G_u@G_u.getH()@WC["uCurlyPhi"]-2*G_d@WC["dCurlyPhi"].getH()@G_u-WC["dCurlyPhi"]@G_d.getH()@G_u-2*G_d@G_d.getH()@WC["uCurlyPhi"]+3*GammaH*WC["uCurlyPhi"]+Gammaq@WC["uCurlyPhi"]+WC["uCurlyPhi"]@Gammau

#i  #Eta5
Beta["dCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])+5/3*gp**2*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"])+g*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))@G_d-(23/12*gp**2+27/4*g**2+8*gs**2)*WC["dCurlyPhi"]-gp*(3*g**2-gp**2)*WC["dB"]-g*(9*g**2-gp**2)*WC["dW"]+(3*g**2+gp**2)*G_d@WC["CurlyPhid"]+3*g**2*G_u@WC["CurlyPhiud"]-2*gp**2*WC["CurlyPhiq1"]@G_d-2*gp**2*WC["CurlyPhiq3"]@G_d+gp*(WC["dB"]@G_d.getH()@G_d+G_d@G_d.getH()@WC["dB"])-3*g*(WC["dW"]@G_d.getH()@G_d-G_d@G_d.getH()@WC["dW"])-16*gs*(WC["dG"]@G_d.getH()@G_d+G_d@G_d.getH()@WC["dG"])-12*g*G_u@G_u.getH()@WC["dW"]-6*g*WC["uW"]@G_u.getH()@G_d+Lambda*(12*WC["dCurlyPhi"]+2*WC["CurlyPhiq1"]@G_d+6*WC["CurlyPhiq3"]@G_d-2*G_d@WC["CurlyPhid"]-2*G_u@WC["CurlyPhiud"]-2*WC["CurlyPhiEmptySquare"]@G_d+WC["CurlyPhiD"]@G_d-4*np.einsum("rpts,pt", WC["qd1"], G_d)-16/3*np.einsum("rpts,pt", WC["qd8"], G_d)+2*np.einsum("ptsr,tp", np.conj(WC["ledq"]), np.conj(G_e))+6*np.einsum("ptrs,pt", WC["quqd1"], np.conj(G_u))+np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))+2*(Eta1+Eta2+1j*Eta5)@G_d+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])@G_d@G_d.getH()@G_d+2*WC["CurlyPhiq1"]@G_d@G_d.getH()@G_d+6*WC["CurlyPhiq3"]@G_u@G_u.getH()@G_d-2*G_d@G_d.getH()@G_d@WC["CurlyPhid"]-2*G_u@G_u.getH()@G_u@WC["CurlyPhiud"]+8*(np.einsum("rpts,pt", WC["qd1"], G_d@G_d.getH()@G_d)+4/3*np.einsum("rpts,pt", WC["qd8"], G_d@G_d.getH()@G_d))-2*(np.einsum("rpts,pt", WC["quqd1"], G_u.getH()@G_u@G_u.getH())+4/3*np.einsum("rpts,pt", WC["quqd8"], G_u.getH()@G_u@G_u.getH()))-12*np.einsum("tprs,pt", WC["quqd1"], G_u@G_u.getH()@G_u)-4*np.einsum("ptsr,pt", WC["ledqc"], G_e@G_e.getH()@G_e)+4*WC["dCurlyPhi"]@G_d.getH()@G_d+5*G_d@G_d.getH()@WC["dCurlyPhi"]-2*G_u@WC["uCurlyPhi"].getH()@G_d-WC["uCurlyPhi"]@G_u.getH()@G_d-2*G_u@G_u.getH()@WC["dCurlyPhi"]+3*GammaH*WC["dCurlyPhi"]+Gammaq@WC["dCurlyPhi"]+C["dCurlyPhi"]@Gammad

#i
Beta["eCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+9*g**2*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])+15*gp**2*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"])-3*g*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))@G_e-3/4*(7*gp**2+9*g**2)*WC["eCurlyPhi"]-3*gp*(g**2-3*gp**2)*WC["eB"]-9*g*(g**2-gp**2)*WC["eW"]+3*(g**2-gp**2)*G_e@WC["CurlyPhie"]-6*gp**2*WC["CurlyPhil1"]@G_e-6*gp**2*WC["CurlyPhil3"]@G_e+9*gp*(WC["eB"]@G_e.getH()@G_e+G_e@G_e.getH()@WC["eB"])-3*g*(WC["eW"]@G_e.getH()@G_e-G_e@G_e.getH()@WC["eW"])+Lambda*(12*WC["eCurlyPhi"]+2*WC["CurlyPhil1"]@G_e+6*WC["CurlyPhil3"]@G_e-2*G_e@WC["CurlyPhie"]-2*WC["CurlyPhiEmptySquare"]@G_e+WC["CurlyPhiD"]@G_e-4*np.einsum("rpts,pt", WC["le"], G_e)+6*np.einsum("rspt,pt", WC["ledq"], G_d)-6*np.einsum("rspt,pt", WC["lequ1"], np.conj(G_u)))+2*(Eta1+Eta2+1j*Eta5)*G_e+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])@G_e@G_e.getH()@G_e+2*WC["CurlyPhil1"]@G_e@G_e.getH()@G_e-2*G_e@G_e.getH()@G_e@WC["CurlyPhie"]+8*np.einsum("rpts,pt", WC["le"], G_e@G_e.getH()@G_e)-12*np.einsum("rspt,tp", WC["ledq"], G_d@G_d.getH()@G_d)+12*np.einsum("rstp,pt", WC["lequ1"], G_u.getH()@G_u@G_u.getH())+4*WC["eCurlyPhi"]@G_e.getH()@G_e+5*G_e@G_e.getH()@WC["eCurlyPhi"]+3*GammaH*WC["eCurlyPhi"]+Gammal@W["CeCurlyPhi"]+WC["eCurlyPhi"]@Gammae

#i
Beta["eW"]=1/12*(3*gp**2-11*g**2)*WC["eW"]-1/2*g*gp*WC["eB"]-(g*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])-3/2*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"]))@G_e-6*g*np.einsum("rspt,pt", WC["lequ3"], np.conj(G_u))+WC["eW"]@G_e.getH()@G_e+GammaH*WC["eW"]+Gammal@WC["eW"]+WC["eW"]@Gammae

#i
Beta["eB"]=1/4*(151/3*gp**2-9*g**2)*WC["eB"]-3/2*g*gp*WC["eW"]-(3/2*g*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])-3*gp*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"]))@G_e+10*gp*np.einsum("rspt,pt", WC["lequ3"], np.conj(G_u))+WC["eB"]@G_e.getH()@G_e+2*G_e@G_e.getH()@WC["eB"]+GammaH*WC["eB"]+Gammal@WC["eB"]+WC["eB"]@Gammae

#i
Beta["uG"]=-1/36*(81*g**2+19*gp**2+204*gs**2)*WC["uG"]+6*g*gs*WC["uW"]+10/3*gp*gs*WC["uB"]-gs*(4*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*gs*(WC["G"]+1j*WC["Gtilde"]))@G_u-gs*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))-1/6*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))+2*G_u@G_u.getH()@WC["uG"]-2*G_d@G_d.getH()@WC["uG"]-WC["dG"]@G_d.getH()@G_u+WC["uG"]@G_u.getH()@G_u+GammaH*WC["uG"]+Gammaq@WC["uG"]+WC["uG"]@Gammau

#i
Beta["uW"]=-1/36*(33*g**2+19*gp**2-96*gs**2)*WC["uW"]+8/3*g*gs*WC["uG"]-1/6*g*gp*WC["uB"]-(g*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])-5/6*gp*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"]))@G_u+g/4*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))-2*g*np.einsum("ptrs,tp", WC["lequ3"], np.conj(G_e))+2*G_d@G_d.getH()@WC["uW"]-WC["dW"]@G_d.getH()@G_u+WC["uW"]@G_u.getH()@G_u+GammaH*WC["uW"]+Gammaq@WC["uW"]+WC["uW"]@Gammau

#i
Beta["uB"]=-1/36*(81*g**2-313*gp**2-96*gs**2)*WC["uB"]+40/9*gp*gs*WC["uG"]-1/2*g*gp*WC["uW"]-(-3/2*g*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])+5/3*gp*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"]))@G_u+gp/12*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))-6*gp*np.einsum("ptrs,tp", WC["lequ3"], np.conj(G_e))+2*G_u@G_u.getH()@WC["uB"]-2*G_d@G_d.getH()@WC["uB"]-WC["dB"]@G_d.getH()@G_u+WC["uB"]@G_u.getH()@G_u+GammaH*WC["uB"]+Gammaq@WC["uB"]+WC["uB"]@Gammau

#i
Beta["dG"]=-1/36*(81*g**2+31*gp**2+204*gs**2)*WC["dG"]+6*g*gs*WC["dW"]-2/3*gp*gs*WC["dB"]-gs*(4*(WC["CurlyPhiG"]+1j*WC["CurlyPhiGtilde"])+9*gs*(WC["G"]+1j*WC["Gtilde"]))@G_d-gs*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))-1/6*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))-2*G_u@G_u.getH()@WC["dG"]+2*G_d@G_d.getH()@WC["dG"]-WC["uG"]@G_u.getH()@G_d+WC["dG"]@G_d.getH()@G_d+GammaH*WC["dG"]+Gammaq@WC["dG"]+WC["dG"]@Gammad

#i
Beta["dW"]=-1/36*(33*g**2+31*gp**2-96*gs**2)*WC["dW"]+8/3*g*gs*WC["dG"]+5/6*g*gp*WC["dB"]-(g*(WC["CurlyPhiW"]+1j*WC["CurlyPhiWtilde"])-gp/6*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"]))@G_d+g/4*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))+2*G_u@G_u.getH()@WC["dW"]-WC["uW"]@G_u.getH()@G_d+WC["dW"]@G_d.getH()@G_d+GammaH*WC["dW"]+Gammaq@WC["dW"]+WC["dW"]@Gammad

#i
Beta["dB"]=-1/36*(81*g**2-253*gp**2-96*gs**2)*WC["dB"]-8/9*gp*gs*WC["dG"]+5/2*g*gp*WC["dW"]-(3/2*g*(WC["CurlyPhiWB"]+1j*WC["CurlyPhiWtildeB"])-gp/3*(WC["CurlyPhiB"]+1j*WC["CurlyPhiBtilde"]))@G_d-5/12*gp*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))-2*G_u@G_u.getH()@WC["dB"]+2*G_d@G_d.getH()@WC["dB"]-WC["uB"]@G_u.getH()@G_d+WC["dB"]@G_d.getH()@G_d+GammaH*WC["dB"]+Gammaq@WC["dB"]+WC["dB"]@Gammad

#I3 #coefficient not equal with manual!!!!!!
Beta["CurlyPhil1"]=-1/4*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhil1"]-2/3*gp**2*(np.einsum("rstt", WC["ld"])+np.einsum("rstt", WC["le"])+2*np.einsum("rstt", WC["ll"])+np.einsum("rtts", WC["ll"])-np.einsum("rstt", WC["lq1"])-2*np.einsum("rstt", WC["lu"]))-1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_e@G_e.getH()-G_e@WC["CurlyPhie"]@G_e.getH()+3/2*(G_e@G_e.getH()@WC["CurlyPhil1"]+WC["CurlyPhil1"]@G_e@G_e.getH()+3*G_e@G_e.getH()@WC["CurlyPhil3"]+3*WC["CurlyPhil3"]@G_e@G_e.getH())+2*np.einsum("rspt,tp", WC["le"], G_e.getH()@G_e)-2*(2*np.einsum("rspt,tp", WC["ll"], G_e@G_e.getH())+np.einsum("rtps,tp", WC["ll"], G_e@G_e.getH()))-6*np.einsum("rspt,tp", WC["lq1"], G_d@G_d.getH())+6*np.einsum("rspt,tp", WC["lq1"], G_u@G_u.getH())-6*np.einsum("rspt,tp", WC["lu"], G_u.getH()@G_u)+6*np.einsum("rspt,tp", WC["ld"], G_d.getH()@G_d)+2*GammaH*WC["CurlyPhil"]1+Gammal@WC["CurlyPhil1"]+WC["CurlyPhil1"]@Gammal

#I3 #coefficient
Beta["CurlyPhil3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])*I3-17/3*g**2*WC["CurlyPhil3"]+2/3*g**2*np.einsum("rtts", WC["ll"])+2*g**2*np.einsum("rstt", WC["lq3"])-1/2*WC["CurlyPhiEmptySquare"]@G_e@G_e.getH()+1/2*(3*G_e@G_e.getH()@WC["CurlyPhil1"]+3*WC["CurlyPhil1"]@G_e@G_e.getH()+G_e@G_e.getH()@WC["CurlyPhil3"]+WC["CurlyPhil3"]@G_e@G_e.getH())-2*(np.einsum("rtps,tp", WC["ll"], G_e@G_e.getH()))-6*np.einsum("rspt,tp", WC["lq3"], G_d@G_d.getH())-6*np.einsum("rspt,tp", WC["lq3"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhil"]3+Gammal@WC["CurlyPhil3"]+WC["CurlyPhil3"]@Gammal

#I3  #coefficient even terms not equal...
Beta["CurlyPhie"]=-1/2*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhie"]-2/3*gp**2*(np.einsum("rstt", WC["ed"])+4*np.einsum("rstt", WC["ee"])-2*np.einsum("rstt", WC["eu"])+np.einsum("ttrs", WC["le"])-np.einsum("ttrs", WC["qe"]))+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_e.getH()@G_e-2*G_e.getH()@WC["CurlyPhil1"]@G_e+3*(G_e.getH()@G_e@WC["CurlyPhie"]+WC["CurlyPhie"]@G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["le"], G_e@G_e.getH())+8*np.einsum("rspt,tp", WC["ee"], G_e.getH()@G_e)-6*np.einsum("rspt,tp", WC["eu"], G_u.getH()@G_u)+6*np.einsum("rspt,tp", WC["ed"], G_d.getH()@G_d)-6*np.einsum("ptrs,tp", WC["qe"], G_d@G_d.getH())+6*np.einsum("ptrs,tp", WC["qe"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhie"]+Gammae@WC["CurlyPhie"]+WC["CurlyPhie"]@Gammae

#I3  #coefficient???
Beta["CurlyPhiq1"]=1/12*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiq1"]-2/3*gp**2*(np.einsum("ttrs", WC["lq1"])+np.einsum("rstt", WC["qd1"])-2*np.einsum("rstt", WC["qu1"])+np.einsum("rstt", WC["qe"])-2*np.einsum("rstt", WC["qq1"])-1/3*np.einsum("rtts", WC["qq1"])-np.einsum("rtts", WC["qq3"]))+1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@(G_u@G_u.getH()-G_d@G_d.getH())-G_u@WC["CurlyPhiu"]@G_u.getH()-G_d@WC["CurlyPhid"]@G_d.getH()+2*np.einsum("rspt,tp", WC["qe"], G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["lq1"], G_e@G_e.getH())+3/2*(G_d@G_d.getH()@WC["CurlyPhiq1"]+G_u@G_u.getH()@WC["CurlyPhiq1"]+WC["CurlyPhiq1"]@G_d@G_d.getH()+WC["CurlyPhiq1"]@G_u@G_u.getH()+3*G_d@G_d.getH()@WC["CurlyPhiq3"]-3*G_u@G_u.getH()@WC["CurlyPhiq3"]+3*WC["CurlyPhiq3"]@G_d@G_d.getH()-3*WC["CurlyPhiq3"]@G_u@G_u.getH())-2*(6*np.einsum("ptrs,tp", WC["qq1"], G_d@G_d.getH())+np.einsum("psrt,tp", WC["qq1"], G_d@G_d.getH())+3*np.einsum("psrt,tp", WC["qq3"], G_d@G_d.getH())-6*np.einsum("ptrs,tp", WC["qq1"], G_u@G_u.getH())-np.einsum("psrt,tp", WC["qq1"], G_u@G_u.getH())-3*np.einsum("psrt,tp", WC["qq3"], G_u@G_u.getH()))-6*np.einsum("rspt,tp", WC["qu1"], G_u.getH()@G_u)+6*np.einsum("rspt,tp", WC["qd1"], G_d.getH()@G_d)+2*GammaH*WC["CurlyPhiq1"]+Gammaq@WC["CurlyPhiq1"]+WC["CurlyPhiq1"]@Gammaq

#I3 #co
Beta["CurlyPhiq3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])*I3-17/3*g**2*WC["CurlyPhiq3"]+2/3*g**2*(np.einsum("ttrs", WC["lq3"])+np.einsum("rtts", WC["qq1"])+6*np.einsum("rstt", WC["qq3"])-np.einsum("rtts", WC["qq3"]))-1/2*WC["CurlyPhiEmptySquare"]@(G_u@G_u.getH()+G_d@G_d.getH())+1/2*(3*G_d@G_d.getH()@WC["CurlyPhiq1"]-3*G_u@G_u.getH()@WC["CurlyPhiq1"]+3*WC["CurlyPhiq1"]@G_d@G_d.getH()-3*WC["CurlyPhiq1"]@G_u@G_u.getH()+G_d@G_d.getH()@WC["CurlyPhiq3"]+G_u@G_u.getH()@WC["CurlyPhiq3"]+WC["CurlyPhiq3"]@G_d@G_d.getH()+WC["CurlyPhiq3"]@G_u@G_u.getH())-2*(6*np.einsum("rspt,tp", WC["qq3"], G_d@G_d.getH())+np.einsum("rtps,tp", WC["qq1"], G_d@G_d.getH())-np.einsum("rtps,tp", WC["qq3"], G_d@G_d.getH())+6*np.einsum("rspt,tp", WC["qq3"], G_u@G_u.getH())+np.einsum("rtps,tp", WC["qq1"], G_u@G_u.getH())-np.einsum("rtps,tp", WC["qq3"], G_u@G_u.getH()))-2*np.einsum("ptrs,tp", WC["lq3"], G_e@G_e.getH())+2*GammaH*WC["CurlyPhiq3"]+Gammaq@WC["CurlyPhiq3"]+WC["CurlyPhiq3"]@Gammaq

#I3 #co
Beta["CurlyPhiu"]=1/3*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiu"]-2/3*gp**2*(np.einsum("ttrs", WC["eu"])+np.einsum("ttrs", WC["lu"])-np.einsum("ttrs", WC["qu1"])+np.einsum("rstt", WC["ud1"])-4*np.einsum("rstt", WC["uu"])-4/3*np.einsum("rtts", WC["uu"]))-(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_u.getH()@G_u-2*G_u.getH()@WC["CurlyPhiq1"]@G_u+3*(G_u.getH()@G_u@WC["CurlyPhiu"]+WC["CurlyPhiu"]@G_u.getH()@G_u)+G_u.getH()@G_d@WC["CurlyPhiud"].getH()+WC["CurlyPhiud"]@G_d.getH()@G_u-4*(3*np.einsum("rspt,tp", WC["uu"], G_u.getH()@G_u)+np.einsum("rtps,tp", WC["uu"], G_u.getH()@G_u))+2*np.einsum("ptrs,tp", WC["eu"], G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["lu"], G_e@G_e.getH())+6*np.einsum("rspt,tp", WC["ud1"], G_d.getH()@G_d)-6*np.einsum("ptrs,tp", WC["qu1"], G_d@G_d.getH())+6*np.einsum("ptrs,tp", WC["qu1"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhiu"]+Gammau@WC["CurlyPhiu"]+WC["CurlyPhiu"]@Gammau

#I3 #co
Beta["CurlyPhid"]=-1/6*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhid"]-2/3*gp**2*(2*np.einsum("rstt", WC["dd"])+2/3*np.einsum("rtts", WC["dd"])+np.einsum("ttrs", WC["ed"])+np.einsum("ttrs", WC["ld"])-np.einsum("ttrs", WC["qd1"])-2*np.einsum("ttrs", WC["ud1"]))+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_d.getH()@G_d-2*G_d.getH()@WC["CurlyPhiq1"]@G_d+3*(G_d.getH()@G_d@WC["CurlyPhid"]+WC["CurlyPhid"]@G_d.getH()@G_d)-G_d.getH()@G_u@WC["CurlyPhiud"]-WC["CurlyPhiud"].getH()@G_u.getH()@G_d+4*(3*np.einsum("rspt,tp", WC["dd"], G_d.getH()@G_d)+np.einsum("rtps,tp", WC["dd"], G_d.getH()@G_d))+2*np.einsum("ptrs,tp", WC["ed"], G_e.getH()@G_e)-2*np.einsum("ptrs,tp", WC["ld"], G_e@G_e.getH())-6*np.einsum("ptrs,tp", WC["ud1"], G_u.getH()@G_u)-6*np.einsum("ptrs,tp", WC["qd1"], G_d@G_d.getH())+6*np.einsum("ptrs,tp", WC["qd1"], G_u@G_u.getH())+2*GammaH*WC["CurlyPhid"]+Gammad@WC["CurlyPhid"]+WC["CurlyPhid"]@Gammad

    #co
Beta["CurlyPhiud"]=-3*gp**2*WC["CurlyPhiud"]+(2*WC["CurlyPhiEmptySquare"]-WC["CurlyPhiD"])@G_u.getH()@G_d-2*G_u.getH()@G_d@WC["CurlyPhid"]+2*WC["CurlyPhiu"]@G_u.getH()@G_d+4*(np.einsum("rtps,tp", WC["ud1"], G_u.getH()@G_d)+4/3*np.einsum("rtps,tp", WC["ud8"], G_u.getH()@G_d))+2*G_u.getH()@G_u@WC["CurlyPhiud"]+2*WC["CurlyPhiud"]@G_d.getH()@G_d+2*GammaH*WC["CurlyPhiud"]+Gammau@WC["CurlyPhiud"]+WC["CurlyPhiud"]@Gammad









#this file was formed from 'revision.py'


Beta["g"]=-19/6*g**3-8*g*m**2/HIGHSCALE**2*WC["CurlyPhiW"]


Beta["gp"]=41/6*gp**3-8*gp*m**2/HIGHSCALE**2*WC["CurlyPhiB"]


Beta["gs"]=-7*gs**3-8*gs*m**2/HIGHSCALE**2*WC["CurlyPhiG"]


Beta["Lambda"]=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)*Lambda+4*Lambda*GammaH-4*(3*np.trace(G_d@G_d.getH()@G_d@G_d.getH())+3*np.trace(G_u@G_u.getH()@G_u@G_u.getH())+np.trace(G_e@G_e.getH()@G_e@G_e.getH()))+4*m**2/HIGHSCALE**2*(12*WC["CurlyPhi"]+(-16*Lambda+10/3*g**2)*WC["CurlyPhiEmptySquare"]+(6*Lambda+3/2*(gp**2-g**2))*WC["CurlyPhiD"]+2*(Eta1+Eta2)+9*g**2*WC["CurlyPhiW"]+3*gp**2*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))


Beta["m**2"]=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH+4*m**2/HIGHSCALE**2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"]))


Beta["G_u@X"]=3/2*(G_u@G_u.getH()@G_u-G_d@G_d.getH()@G_u)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)@G_u+2*m**2/HIGHSCALE**2*(3*WC["uCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])@G_u-WC["CurlyPhiq1"].getH()@G_u+3*WC["CurlyPhiq3"].getH()@G_u+G_u@WC["CurlyPhiu"].getH()-G_d@WC["CurlyPhiud"].getH()-2*(np.einsum("rpts,pt", WC["qu1"], G_u)+4/3*np.einsum("rpts,pt", WC["qu8"], G_u))-np.einsum("ptrs,pt", WC["lequ1"], np.conj(G_e))+3*np.einsum("rspt,pt", WC["quqd1"], np.conj(G_d))+1/2*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d))))


Beta["G_d@X"]=3/2*(G_d@G_d.getH()@G_d-G_u@G_u.getH()@G_d)+(GammaH-9/4*g**2-5/12*gp**2-8*gs**2)@G_d+2*m**2/HIGHSCALE**2*(3*WC["dCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])@G_d+WC["CurlyPhiq1"].getH()@G_d+3*WC["CurlyPhiq3"].getH()@G_d-G_d@WC["CurlyPhid"].getH()-G_u@CCurlyPhiud-2*(np.einsum("rpts,pt", WC["qd1"], G_d)+4/3*np.einsum("rpts,pt", WC["qd8"], G_d))+np.einsum("ptsr,tp", np.conj(WC["ledq"]), np.conj(G_e))+3*np.einsum("ptrs,pt", WC["quqd1"], np.conj(G_u))+1/2*(np.einsum("rpts,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rpts,pt", WC["quqd8"], np.conj(G_u))))


Beta["G_e@X"]=3/2*G_e@G_e.getH()@G_e+(GammaH-3/4*(3*g**2+5*gp**2))@G_e+2*m**2/HIGHSCALE**2*(3*WC["eCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])@G_e+WC["CurlyPhil1"].getH()@G_e+3*WC["CurlyPhil3"].getH()@G_e-G_e@WC["CurlyPhie"].getH()-2*np.einsum("rpts,pt", WC["le"], G_e)+3*np.einsum("rspt,tp", WC["ledq"], G_d)-3*np.einsum("rspt,pt", WC["lequ1"], np.conj(G_u)))


Beta["Theta"]=-iCPV 128*Pi**2/g**2*m**2/HIGHSCALE**2*WC["CurlyPhiWtilde"]


Beta["Thetap"]=-iCPV 128*Pi**2/gp**2*m**2/HIGHSCALE**2*WC["CurlyPhiBtilde"]


Beta["Thetas"]=-iCPV 128*Pi**2/gs**2*m**2/HIGHSCALE**2*WC["CurlyPhiGtilde"]


BetaSMg=-19/6*g**3


BetaSMgp=41/6*gp**3


BetaSMgs=-7*gs**3


BetaSMLambda=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)*Lambda+4*Lambda*GammaH-4*(3*np.trace(G_d@G_d.getH()@G_d@G_d.getH())+3*np.trace(G_u@G_u.getH()@G_u@G_u.getH())+np.trace(G_e@G_e.getH()@G_e@G_e.getH()))


BetaSMm**2=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH)


BetaSMG_u@X=3/2*(G_u@G_u.getH()@G_u-G_d@G_d.getH()@G_u)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)@G_u


BetaSMG_d@X=3/2*(G_d@G_d.getH()@G_d-G_u@G_u.getH()@G_d)+(GammaH-9/4*g**2-5/12*gp**2-8*gs**2)@G_d


BetaSMG_e@X=3/2*G_e@G_e.getH()@G_e+(GammaH-3/4*(3*g**2+5*gp**2))@G_e


BetaSMTheta=0


BetaSMThetap=0


BetaSMThetas=0


Beta["G"]=15*gs**2*WC["G"]


Beta["Gtilde"]=15*gs**2*WC["Gtilde"]


Beta["W"]=29/2*g**2*WC["W"]


Beta["Wtilde"]=29/2*g**2*WC["Wtilde"]


Beta["CurlyPhi"]=-9/2*(3*g**2+gp**2)*WC["CurlyPhi"]+Lambda(20/3*g**2*WC["CurlyPhiEmptySquare"]+3*(gp**2-g**2)*WC["CurlyPhiD"])-3/4*(g**2+gp**2)**2*WC["CurlyPhiD"]+6*Lambda(3*g**2*WC["CurlyPhiW"]+gp**2*WC["CurlyPhiB"]+g*gp*WC["CurlyPhiWB"])-3*(g**2*gp**2+3*g**4)*WC["CurlyPhiW"]-3*(gp**4+g**2*gp**2)*WC["CurlyPhiB"]-3*(g*gp**3+g**3*gp)*WC["CurlyPhiWB"]+8/3*Lambda*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))+54*Lambda*WC["CurlyPhi"]-40*Lambda**2*WC["CurlyPhiEmptySquare"]+12*Lambda**2*WC["CurlyPhiD"]+4*Lambda(Eta1+Eta2)-4*(3*np.trace(WC["uCurlyPhiG_u"]).getH()@G_u@G_u.getH()+3*np.trace(WC["dCurlyPhiG_d"]).getH()@G_d@G_d.getH()+np.trace(WC["eCurlyPhiG_e"]).getH()@G_e@G_e.getH()+3*cnp.trace(WC["uCurlyPhiG_u"]).getH()@G_u@G_u.getH()+3*cnp.trace(WC["dCurlyPhiG_d"]).getH()@G_d@G_d.getH()+cnp.trace(WC["eCurlyPhiG_e"]).getH()@G_e@G_e.getH())+6*GammaH*WC["CurlyPhi"]


Beta["CurlyPhiEmptySquare"]=-(4*g**2+4/3*gp**2)*WC["CurlyPhiEmptySquare"]+5/3*gp**2*WC["CurlyPhiD"]+2*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))+2/3*gp**2*(2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"])-np.trace(WC["CurlyPhie"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhil1"]))+12*Lambda*WC["CurlyPhiEmptySquare"]-2*Eta3+4*GammaH*WC["CurlyPhiEmptySquare"]


Beta["CurlyPhiD"]=20/3*gp**2*WC["CurlyPhiEmptySquare"]+(9/2*g**2-5/6*gp**2)*WC["CurlyPhiD"]+8/3*gp**2*(2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"])-np.trace(WC["CurlyPhie"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhil1"]))+6*Lambda*WC["CurlyPhiD"]-2*Eta4+4*GammaH*WC["CurlyPhiD"]


Beta["CurlyPhiG"]=(-3/2*gp**2-9/2*g**2-14*gs**2)*WC["CurlyPhiG"]+6*Lambda*WC["CurlyPhiG"]-2*gs(np.trace(WC["uGG_u"]).getH()+np.trace(WC["dGG_d"]).getH()+cnp.trace(WC["uGG_u"]).getH()+cnp.trace(WC["dGG_d"]).getH())+2*GammaH*WC["CurlyPhiG"]


Beta["CurlyPhiB"]=(85/6*gp**2-9/2*g**2)*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+6*Lambda*WC["CurlyPhiB"]+gp(-5*np.trace(WC["uBG_u"]).getH()+np.trace(WC["dBG_d"]).getH()+3*np.trace(WC["eBG_e"]).getH()-5*cnp.trace(WC["uBG_u"]).getH()+cnp.trace(WC["dBG_d"]).getH()+3*cnp.trace(WC["eBG_e"]).getH())+2*GammaH*WC["CurlyPhiB"]


Beta["CurlyPhiW"]=(-3/2*gp**2-53/6*g**2)*WC["CurlyPhiW"]+g*gp*WC["CurlyPhiWB"]-15*g**3*WC["W"]+6*Lambda*WC["CurlyPhiW"]-g(3*np.trace(WC["uWG_u"]).getH()+3*np.trace(WC["dWG_d"]).getH()+np.trace(WC["eWG_e"]).getH()+3*cnp.trace(WC["uWG_u"]).getH()+3*cnp.trace(WC["dWG_d"]).getH()+cnp.trace(WC["eWG_e"]).getH())+2*GammaH*WC["CurlyPhiW"]


Beta["CurlyPhiWB"]=(19/3*gp**2+4/3*g**2)*WC["CurlyPhiWB"]+2*g*gp(WC["CurlyPhiB"]+WC["CurlyPhiW"])+3*g**2*gp*WC["W"]+2*Lambda*WC["CurlyPhiWB"]+g(3*np.trace(WC["uBG_u"]).getH()-3*np.trace(WC["dBG_d"]).getH()-np.trace(WC["eBG_e"]).getH()+3*cnp.trace(WC["uBG_u"]).getH()-3*cnp.trace(WC["dBG_d"]).getH()-cnp.trace(WC["eBG_e"]).getH())+gp(5*np.trace(WC["uWG_u"]).getH()+np.trace(WC["dWG_d"]).getH()+3*np.trace(WC["eWG_e"]).getH()+5*cnp.trace(WC["uWG_u"]).getH()+cnp.trace(WC["dWG_d"]).getH()+3*cnp.trace(WC["eWG_e"]).getH())+2*GammaH*WC["CurlyPhiWB"]


Beta["CurlyPhiGtilde"]=(-3/2*gp**2-9/2*g**2-14*gs**2)*WC["CurlyPhiGtilde"]+6*Lambda*WC["CurlyPhiGtilde"]+2*I*iCPV*gs(np.trace(WC["uGG_u"]).getH()+np.trace(WC["dGG_d"]).getH()-cnp.trace(WC["uGG_u"]).getH()-cnp.trace(WC["dGG_d"]).getH())+2*GammaH*WC["CurlyPhiGtilde"]


Beta["CurlyPhiBtilde"]=(85/6*gp**2-9/2*g**2)*WC["CurlyPhiBtilde"]+3*g*gp*WC["CurlyPhiWtildeB"]+6*Lambda*WC["CurlyPhiBtilde"]-I*iCPV*gp(-5*np.trace(WC["uBG_u"]).getH()+np.trace(WC["dBG_d"]).getH()+3*np.trace(WC["eBG_e"]).getH()+5*cnp.trace(WC["uBG_u"]).getH()-cnp.trace(WC["dBG_d"]).getH()-3*cnp.trace(WC["eBG_e"]).getH())+2*GammaH*WC["CurlyPhiBtilde"]


Beta["CurlyPhiWtilde"]=(-3/2*gp**2-53/6*g**2)*WC["CurlyPhiWtilde"]+g*gp*WC["CurlyPhiWtildeB"]-15*g**3*WC["Wtilde"]+6*Lambda*WC["CurlyPhiWtilde"]+I*iCPV*g(3*np.trace(WC["uWG_u"]).getH()+3*np.trace(WC["dWG_d"]).getH()+np.trace(WC["eWG_e"]).getH()-3*cnp.trace(WC["uWG_u"]).getH()-3*cnp.trace(WC["dWG_d"]).getH()-cnp.trace(WC["eWG_e"]).getH())+2*GammaH*WC["CurlyPhiWtilde"]


Beta["CurlyPhiWtildeB"]=(19/3*gp**2+4/3*g**2)*WC["CurlyPhiWtildeB"]+2*g*gp(WC["CurlyPhiBtilde"]+WC["CurlyPhiWtilde"])+3*g**2*gp*WC["Wtilde"]+2*Lambda*WC["CurlyPhiWtildeB"]-I*iCPV*g(3*np.trace(WC["uBG_u"]).getH()-3*np.trace(WC["dBG_d"]).getH()-np.trace(WC["eBG_e"]).getH()-3*cnp.trace(WC["uBG_u"]).getH()+3*cnp.trace(WC["dBG_d"]).getH()+cnp.trace(WC["eBG_e"]).getH())-I*iCPV*gp(5*np.trace(WC["uWG_u"]).getH()+np.trace(WC["dWG_d"]).getH()+3*np.trace(WC["eWG_e"]).getH()-5*cnp.trace(WC["uWG_u"]).getH()-cnp.trace(WC["dWG_d"]).getH()-3*cnp.trace(WC["eWG_e"]).getH())+2*GammaH*WC["CurlyPhiWtildeB"]


Beta["uCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])+17/3*gp**2*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"])-g*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))@G_u-(35/12*gp**2+27/4*g**2+8*gs**2)*WC["uCurlyPhi"]-gp(5*gp**2-3*g**2)*WC["uB"]+g(5*gp**2-9*g**2)*WC["uW"]-(3*g**2-gp**2)@G_u@CCurlyPhiu+3*g**2*G_d@WC["CurlyPhiud"].getH()+4*gp**2*CCurlyPhiq1*G_u-4*gp**2*CCurlyPhiq3*G_u-5*gp(CuBG_u.getH()@G_u+G_u@G_u.getH()@CuB)-3*g(CuWG_u.getH()@G_u-G_u@G_u.getH()@CuW)-16*gs(CuGG_u.getH()@G_u+G_u@G_u.getH()@CuG)-12*g*G_d@G_d.getH()@CuW-6*g*CdWG_d.getH()@G_u+Lambda(12*WC["uCurlyPhi"]-2*CCurlyPhiq1*G_u+6*CCurlyPhiq3*G_u+2*G_u@CCurlyPhiu-2*G_d@WC["CurlyPhiud"].getH()-2*WC["CurlyPhiEmptySquareG_u@"]+WC["CurlyPhiDG_u@"]-4*np.einsum("rpts,pt", WC["qu1"], G_u)-16/3*np.einsum("rpts,pt", WC["qu8"], G_u)-2*np.einsum("ptrs,pt", WC["lequ1"], np.conj(G_e))+6*np.einsum("rspt,pt", WC["quqd1"], np.conj(G_d))+np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))+2*(Eta1+Eta2-Eta5)@G_u+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])@G_u@G_u.getH()@G_u-2*CCurlyPhiq1*G_u@G_u.getH()@G_u+6*CCurlyPhiq3*G_d@G_d.getH()@G_u+2*G_u@G_u.getH()@G_u@CCurlyPhiu-2*G_d@G_d.getH()@G_d@WC["CurlyPhiud"].getH()+8*(Cqu1*G_u@G_u.getH()@G_u@rpts,pt+4/3*Cqu8*G_u@G_u.getH()@G_u@rpts,pt)-2*(Cquqd1*G_d.getH()@G_d@G_d.getH()@tsrp,pt+4/3*Cquqd8*G_d.getH()@G_d@G_d.getH()@tsrp,pt)-12*Cquqd1*G_d.getH()@G_d@G_d.getH()@rstp,pt+4*Clequ1*G_e@G_e.getH()@G_e@tprs,pt+4*CuCurlyPhiG_u.getH()@G_u+5*G_u@G_u.getH()@CuCurlyPhi-2*G_d@WC["dCurlyPhi"].getH()@G_u-CdCurlyPhiG_d.getH()@G_u-2*G_d@G_d.getH()@CuCurlyPhi+3*GammaH*WC["uCurlyPhi"]+GammaqCuCurlyPhi+CuCurlyPhiGammau


Beta["dCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])+5/3*gp**2*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"])+g*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))@G_d-(23/12*gp**2+27/4*g**2+8*gs**2)*WC["dCurlyPhi"]-gp(3*g**2-gp**2)*WC["dB"]-g(9*g**2-gp**2)*WC["dW"]+(3*g**2+gp**2)@G_d@CCurlyPhid+3*g**2*G_u@CCurlyPhiud-2*gp**2*CCurlyPhiq1*G_d-2*gp**2*CCurlyPhiq3*G_d+gp(CdBG_d.getH()@G_d+G_d@G_d.getH()@CdB)-3*g(CdWG_d.getH()@G_d-G_d@G_d.getH()@CdW)-16*gs(CdGG_d.getH()@G_d+G_d@G_d.getH()@CdG)-12*g*G_u@G_u.getH()@CdW-6*g*CuWG_u.getH()@G_d+Lambda(12*WC["dCurlyPhi"]+2*CCurlyPhiq1*G_d+6*CCurlyPhiq3*G_d-2*G_d@CCurlyPhid-2*G_u@CCurlyPhiud-2*WC["CurlyPhiEmptySquareG_d@"]+WC["CurlyPhiDG_d@"]-4*np.einsum("rpts,pt", WC["qd1"], G_d)-16/3*np.einsum("rpts,pt", WC["qd8"], G_d)+2*np.einsum("ptsr,tp", np.conj(WC["ledq"]), np.conj(G_e))+6*np.einsum("ptrs,pt", WC["quqd1"], np.conj(G_u))+np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))+2*(Eta1+Eta2+Eta5)@G_d+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])@G_d@G_d.getH()@G_d+2*CCurlyPhiq1*G_d@G_d.getH()@G_d+6*CCurlyPhiq3*G_u@G_u.getH()@G_d-2*G_d@G_d.getH()@G_d@CCurlyPhid-2*G_u@G_u.getH()@G_u@CCurlyPhiud+8*(Cqd1*G_d@G_d.getH()@G_d@rpts,pt+4/3*Cqd8*G_d@G_d.getH()@G_d@rpts,pt)-2*(Cquqd1*G_u.getH()@G_u@G_u.getH()@rpts,pt+4/3*Cquqd8*G_u.getH()@G_u@G_u.getH()@rpts,pt)-12*Cquqd1*G_u@G_u.getH()@G_u@tprs,pt-4*CledqcG_e@G_e.getH()@G_e@ptsr,pt+4*CdCurlyPhiG_d.getH()@G_d+5*G_d@G_d.getH()@CdCurlyPhi-2*G_u@WC["uCurlyPhi"].getH()@G_d-CuCurlyPhiG_u.getH()@G_d-2*G_u@G_u.getH()@CdCurlyPhi+3*GammaH*WC["dCurlyPhi"]+GammaqCdCurlyPhi+CdCurlyPhiGammad


Beta["eCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)*WC["CurlyPhiD"]+9*g**2*(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])+15*gp**2*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"])-3*g*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))@G_e-3/4*(7*gp**2+9*g**2)*WC["eCurlyPhi"]-3*gp(g**2-3*gp**2)*WC["eB"]-9*g(g**2-gp**2)*WC["eW"]+3*(g**2-gp**2)@G_e@CCurlyPhie-6*gp**2*CCurlyPhil1*G_e-6*gp**2*CCurlyPhil3*G_e+9*gp(CeBG_e.getH()@G_e+G_e@G_e.getH()@CeB)-3*g(CeWG_e.getH()@G_e-G_e@G_e.getH()@CeW)+Lambda(12*WC["eCurlyPhi"]+2*CCurlyPhil1*G_e+6*CCurlyPhil3*G_e-2*G_e@CCurlyPhie-2*WC["CurlyPhiEmptySquareG_e@"]+WC["CurlyPhiDG_e@"]-4*np.einsum("rpts,pt", WC["le"], G_e)+6*np.einsum("rspt,pt", WC["ledq"], G_d)-6*np.einsum("rspt,pt", WC["lequ1"], np.conj(G_u)))+2*(Eta1+Eta2+Eta5)@G_e+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])@G_e@G_e.getH()@G_e+2*CCurlyPhil1*G_e@G_e.getH()@G_e-2*G_e@G_e.getH()@G_e@CCurlyPhie+8*CleG_e@G_e.getH()@G_e@rpts,pt-12*CledqG_d@G_d.getH()@G_d@rspt,tp+12*Clequ1*G_u.getH()@G_u@G_u.getH()@rstp,pt+4*CeCurlyPhiG_e.getH()@G_e+5*G_e@G_e.getH()@CeCurlyPhi+3*GammaH*WC["eCurlyPhi"]+GammalCeCurlyPhi+CeCurlyPhiGammae


Beta["eW"]=1/12*(3*gp**2-11*g**2)*WC["eW"]-1/2*g*gp*WC["eB"]-(g(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])-3/2*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"]))@G_e-6*g*np.einsum("rspt,pt", WC["lequ3"], np.conj(G_u))+CeWG_e.getH()@G_e+GammaH*WC["eW"]+GammalCeW+CeWGammae


Beta["eB"]=1/4*(151/3*gp**2-9*g**2)*WC["eB"]-3/2*g*gp*WC["eW"]-(3/2*g(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])-3*gp(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"]))@G_e+10*gp*np.einsum("rspt,pt", WC["lequ3"], np.conj(G_u))+CeBG_e.getH()@G_e+2*G_e@G_e.getH()@CeB+GammaH*WC["eB"]+GammalCeB+CeBGammae


Beta["uG"]=-1/36*(81*g**2+19*gp**2+204*gs**2)*WC["uG"]+6*g*gs*WC["uW"]+10/3*gp*gs*WC["uB"]-gs(4*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*gs(WC["G"]+I*iCPV*WC["Gtilde"]))@G_u-gs(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))-1/6*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))+2*G_u@G_u.getH()@CuG-2*G_d@G_d.getH()@CuG-CdGG_d.getH()@G_u+CuGG_u.getH()@G_u+GammaH*WC["uG"]+GammaqCuG+CuGGammau


Beta["uW"]=-1/36*(33*g**2+19*gp**2-96*gs**2)*WC["uW"]+8/3*g*gs*WC["uG"]-1/6*g*gp*WC["uB"]-(g(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])-5/6*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"]))@G_u+g/4*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))-2*g*np.einsum("ptrs,tp", WC["lequ3"], np.conj(G_e))+2*G_d@G_d.getH()@CuW-CdWG_d.getH()@G_u+CuWG_u.getH()@G_u+GammaH*WC["uW"]+GammaqCuW+CuWGammau


Beta["uB"]=-1/36*(81*g**2-313*gp**2-96*gs**2)*WC["uB"]+40/9*gp*gs*WC["uG"]-1/2*g*gp*WC["uW"]-(-3/2*g(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+5/3*gp(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"]))@G_u+gp/12*(np.einsum("psrt,pt", WC["quqd1"], np.conj(G_d))+4/3*np.einsum("psrt,pt", WC["quqd8"], np.conj(G_d)))-6*gp*np.einsum("ptrs,tp", WC["lequ3"], np.conj(G_e))+2*G_u@G_u.getH()@CuB-2*G_d@G_d.getH()@CuB-CdBG_d.getH()@G_u+CuBG_u.getH()@G_u+GammaH*WC["uB"]+GammaqCuB+CuBGammau


Beta["dG"]=-1/36*(81*g**2+31*gp**2+204*gs**2)*WC["dG"]+6*g*gs*WC["dW"]-2/3*gp*gs*WC["dB"]-gs(4*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*gs(WC["G"]+I*iCPV*WC["Gtilde"]))@G_d-gs(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))-1/6*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))-2*G_u@G_u.getH()@CdG+2*G_d@G_d.getH()@CdG-CuGG_u.getH()@G_d+CdGG_d.getH()@G_d+GammaH*WC["dG"]+GammaqCdG+CdGGammad


Beta["dW"]=-1/36*(33*g**2+31*gp**2-96*gs**2)*WC["dW"]+8/3*g*gs*WC["dG"]+5/6*g*gp*WC["dB"]-(g(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])-gp/6*(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"]))@G_d+g/4*(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))+2*G_u@G_u.getH()@CdW-CuWG_u.getH()@G_d+CdWG_d.getH()@G_d+GammaH*WC["dW"]+GammaqCdW+CdWGammad


Beta["dB"]=-1/36*(81*g**2-253*gp**2-96*gs**2)*WC["dB"]-8/9*gp*gs*WC["dG"]+5/2*g*gp*WC["dW"]-(3/2*g(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])-gp/3*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"]))@G_d-5/12*gp(np.einsum("rtps,pt", WC["quqd1"], np.conj(G_u))+4/3*np.einsum("rtps,pt", WC["quqd8"], np.conj(G_u)))-2*G_u@G_u.getH()@CdB+2*G_d@G_d.getH()@CdB-CuBG_u.getH()@G_d+CdBG_d.getH()@G_d+GammaH*WC["dB"]+GammaqCdB+CdBGammad


Beta["CurlyPhil1"]=-1/4*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhil"]1-2/3*gp**2*(Cldrstt+Clerstt+2*Cllrstt+Cllrtts-Clq1*rstt-2*Clurstt)-1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_e@G_e.getH()-G_e@CCurlyPhieG_e.getH()+3/2*(G_e@G_e.getH()@CCurlyPhil1+CCurlyPhil1*G_e@G_e.getH()+3*G_e@G_e.getH()@CCurlyPhil3+3*CCurlyPhil3*G_e@G_e.getH())+2*CleG_e.getH()@G_e@rspt,tp-2*(2*CllG_e@G_e.getH()@rspt,tp+CllG_e@G_e.getH()@rtps,tp)-6*Clq1*G_d@G_d.getH()@rspt,tp+6*Clq1*G_u@G_u.getH()@rspt,tp-6*CluG_u.getH()@G_u@rspt,tp+6*CldG_d.getH()@G_d@rspt,tp+2*GammaH*WC["CurlyPhil"]1+GammalCCurlyPhil1+CCurlyPhil1*Gammal


Beta["CurlyPhil3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))*I3-17/3*g**2*WC["CurlyPhil"]3+2/3*g**2*Cllrtts+2*g**2*Clq3*rstt-1/2*WC["CurlyPhiEmptySquareG_e@G_e.getH()@"]+1/2*(3*G_e@G_e.getH()@CCurlyPhil1+3*CCurlyPhil1*G_e@G_e.getH()+G_e@G_e.getH()@CCurlyPhil3+CCurlyPhil3*G_e@G_e.getH())-2*(CllG_e@G_e.getH()@rtps,tp)-6*Clq3*G_d@G_d.getH()@rspt,tp-6*Clq3*G_u@G_u.getH()@rspt,tp+2*GammaH*WC["CurlyPhil"]3+GammalCCurlyPhil3+CCurlyPhil3*Gammal


Beta["CurlyPhie"]=-1/2*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhie"]-2/3*gp**2*(Cedrstt+4*Ceerstt-2*Ceurstt+Clettrs-Cqettrs)+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_e.getH()@G_e-2*G_e.getH()@CCurlyPhil1*G_e+3*(G_e.getH()@G_e@CCurlyPhie+CCurlyPhieG_e.getH()@G_e)-2*CleG_e@G_e.getH()@ptrs,tp+8*CeeG_e.getH()@G_e@rspt,tp-6*CeuG_u.getH()@G_u@rspt,tp+6*CedG_d.getH()@G_d@rspt,tp-6*CqeG_d@G_d.getH()@ptrs,tp+6*CqeG_u@G_u.getH()@ptrs,tp+2*GammaH*WC["CurlyPhie"]+GammaeCCurlyPhie+CCurlyPhieGammae


Beta["CurlyPhiq1"]=1/12*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiq"]1-2/3*gp**2*(Clq1*ttrs+Cqd1*rstt-2*Cqu1*rstt+Cqerstt-2*Cqq1*rstt-1/3*Cqq1*rtts-Cqq3*rtts)+1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])*(G_u@G_u.getH()-G_d@G_d.getH())-G_u@CCurlyPhiuG_u.getH()-G_d@CCurlyPhidG_d.getH()+2*CqeG_e.getH()@G_e@rspt,tp-2*Clq1*G_e@G_e.getH()@ptrs,tp+3/2*(G_d@G_d.getH()@CCurlyPhiq1+G_u@G_u.getH()@CCurlyPhiq1+CCurlyPhiq1*G_d@G_d.getH()+CCurlyPhiq1*G_u@G_u.getH()+3*G_d@G_d.getH()@CCurlyPhiq3-3*G_u@G_u.getH()@CCurlyPhiq3+3*CCurlyPhiq3*G_d@G_d.getH()-3*CCurlyPhiq3*G_u@G_u.getH())-2*(6*Cqq1*G_d@G_d.getH()@ptrs,tp+Cqq1*G_d@G_d.getH()@psrt,tp+3*Cqq3*G_d@G_d.getH()@psrt,tp-6*Cqq1*G_u@G_u.getH()@ptrs,tp-Cqq1*G_u@G_u.getH()@psrt,tp-3*Cqq3*G_u@G_u.getH()@psrt,tp)-6*Cqu1*G_u.getH()@G_u@rspt,tp+6*Cqd1*G_d.getH()@G_d@rspt,tp+2*GammaH*WC["CurlyPhiq"]1+GammaqCCurlyPhiq1+CCurlyPhiq1*Gammaq


Beta["CurlyPhiq3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"]))*I3-17/3*g**2*WC["CurlyPhiq"]3+2/3*g**2*(Clq3*ttrs+Cqq1*rtts+6*Cqq3*rstt-Cqq3*rtts)-1/2*WC["CurlyPhiEmptySquare"](G_u@G_u.getH()+G_d@G_d.getH())+1/2*(3*G_d@G_d.getH()@CCurlyPhiq1-3*G_u@G_u.getH()@CCurlyPhiq1+3*CCurlyPhiq1*G_d@G_d.getH()-3*CCurlyPhiq1*G_u@G_u.getH()+G_d@G_d.getH()@CCurlyPhiq3+G_u@G_u.getH()@CCurlyPhiq3+CCurlyPhiq3*G_d@G_d.getH()+CCurlyPhiq3*G_u@G_u.getH())-2*(6*Cqq3*G_d@G_d.getH()@rspt,tp+Cqq1*G_d@G_d.getH()@rtps,tp-Cqq3*G_d@G_d.getH()@rtps,tp+6*Cqq3*G_u@G_u.getH()@rspt,tp+Cqq1*G_u@G_u.getH()@rtps,tp-Cqq3*G_u@G_u.getH()@rtps,tp)-2*Clq3*G_e@G_e.getH()@ptrs,tp+2*GammaH*WC["CurlyPhiq"]3+GammaqCCurlyPhiq3+CCurlyPhiq3*Gammaq


Beta["CurlyPhiu"]=1/3*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiu"]-2/3*gp**2*(Ceuttrs+Cluttrs-Cqu1*ttrs+Cud1*rstt-4*Cuurstt-4/3*Cuurtts)-(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_u.getH()@G_u-2*G_u.getH()@CCurlyPhiq1*G_u+3*(G_u.getH()@G_u@CCurlyPhiu+CCurlyPhiuG_u.getH()@G_u)+G_u.getH()@G_d@WC["CurlyPhiud"].getH()+CCurlyPhiudG_d.getH()@G_u-4*(3*CuuG_u.getH()@G_u@rspt,tp+CuuG_u.getH()@G_u@rtps,tp)+2*CeuG_e.getH()@G_e@ptrs,tp-2*CluG_e@G_e.getH()@ptrs,tp+6*Cud1*G_d.getH()@G_d@rspt,tp-6*Cqu1*G_d@G_d.getH()@ptrs,tp+6*Cqu1*G_u@G_u.getH()@ptrs,tp+2*GammaH*WC["CurlyPhiu"]+GammauCCurlyPhiu+CCurlyPhiuGammau


Beta["CurlyPhid"]=-1/6*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhid"]-2/3*gp**2*(2*Cddrstt+2/3*Cddrtts+Cedttrs+Cldttrs-Cqd1*ttrs-2*Cud1*ttrs)+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])@G_d.getH()@G_d-2*G_d.getH()@CCurlyPhiq1*G_d+3*(G_d.getH()@G_d@CCurlyPhid+CCurlyPhidG_d.getH()@G_d)-G_d.getH()@G_u@CCurlyPhiud-WC["CurlyPhiud"].getH()@G_u.getH()@G_d+4*(3*CddG_d.getH()@G_d@rspt,tp+CddG_d.getH()@G_d@rtps,tp)+2*CedG_e.getH()@G_e@ptrs,tp-2*CldG_e@G_e.getH()@ptrs,tp-6*Cud1*G_u.getH()@G_u@ptrs,tp-6*Cqd1*G_d@G_d.getH()@ptrs,tp+6*Cqd1*G_u@G_u.getH()@ptrs,tp+2*GammaH*WC["CurlyPhid"]+GammadCCurlyPhid+CCurlyPhidGammad


Beta["CurlyPhiud"]=-3*gp**2*WC["CurlyPhiud"]+(2*WC["CurlyPhiEmptySquare"]-WC["CurlyPhiD"])@G_u.getH()@G_d-2*G_u.getH()@G_d@CCurlyPhid+2*CCurlyPhiuG_u.getH()@G_d+4*(Cud1*G_u.getH()@G_d@rtps,tp+4/3*Cud8*G_u.getH()@G_d@rtps,tp)+2*G_u.getH()@G_u@CCurlyPhiud+2*CCurlyPhiudG_d.getH()@G_d+2*GammaH*WC["CurlyPhiud"]+GammauCCurlyPhiud+CCurlyPhiudGammad


Beta["ll"]=-1/6*gp**2*CCurlyPhil1*Delta_st,pr-1/6*g**2*(CCurlyPhil3*Delta_st,pr-2*CCurlyPhil3*Delta_sr,pt)+1/3*gp**2*(2*CllDelta_prww,st+CllDelta_pwwr,st)-1/3*g**2*CllDelta_pwwr,st+2/3*g**2*CllDelta_swwr,pt-1/3*gp**2*Clq1*Delta_prww,st-g**2*Clq3*Delta_prww,st+2*g**2*Clq3*Delta_ptww,rs+1/3*gp**2*(-2*CluDelta_prww,st+CldDelta_prww,st+CleDelta_prww,st)-1/2*(G_e@G_e.getH()@xCCurlyPhil1*pr,st-G_e@G_e.getH()@xCCurlyPhil3*pr,st)-G_e@G_e.getH()@xCCurlyPhil3*pt,sr-1/2*G_e@np.conj(G_e)@Clesv,tw,prvw+GammalCllpv,vrst+CllGammalpvst,vr-1/6*gp**2*CCurlyPhil1*Delta_pr,st-1/6*g**2*(CCurlyPhil3*Delta_pr,st-2*CCurlyPhil3*Delta_pt,sr)+1/3*gp**2*(2*CllDelta_stww,pr+CllDelta_swwt,pr)-1/3*g**2*CllDelta_swwt,pr+2/3*g**2*CllDelta_pwwt,sr-1/3*gp**2*Clq1*Delta_stww,pr-g**2*Clq3*Delta_stww,pr+2*g**2*Clq3*Delta_srww,tp+1/3*gp**2*(-2*CluDelta_stww,pr+CldDelta_stww,pr+CleDelta_stww,pr)-1/2*(G_e@G_e.getH()@xCCurlyPhil1*st,pr-G_e@G_e.getH()@xCCurlyPhil3*st,pr)-G_e@G_e.getH()@xCCurlyPhil3*sr,pt-1/2*G_e@np.conj(G_e)@Clepv,rw,stvw+GammalCllsv,vtpr+CllGammalsvpr,vt+6*g**2*Cllptsr+3*(gp**2-g**2)*Cllprst


Beta["qq1"]=1/18*gp**2*CCurlyPhiq1*Delta_st,pr-1/9*gp**2*Clq1*Delta_wwst,pr+1/9*gp**2*(2*Cqq1*Delta_prww,st+1/3*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st))+1/3*gs**2*(Cqq1*Delta_swwr,pt+3*Cqq3*Delta_swwr,pt)-2/9*gs**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+2/9*gp**2*Cqu1*Delta_prww,st-1/9*gp**2*Cqd1*Delta_prww,st+1/12*gs**2*(Cqu8*Delta_srww,pt+Cqd8*Delta_srww,pt)-1/18*gs**2*(Cqu8*Delta_prww,st+Cqd8*Delta_prww,st)-1/9*gp**2*CqeDelta_prww,st+1/2*(G_u@G_u.getH()@xCCurlyPhiq1*pr,st-G_d@G_d.getH()@xCCurlyPhiq1*pr,st)-1/2*(G_u@np.conj(G_u)@Cqu1*pv,rw,stvw-1/6*G_u@np.conj(G_u)@Cqu8*pv,rw,stvw)-1/2*(G_d@np.conj(G_d)@Cqd1*pv,rw,stvw-1/6*G_d@np.conj(G_d)@Cqd8*pv,rw,stvw)-1/8*(G_u@np.conj(G_u)@Cqu8*pv,tw,srvw+G_d@np.conj(G_d)@Cqd8*pv,tw,srvw)-1/8*(np.conj(G_d)@np.conj(G_u)@Cquqd1*tw,rv,pvsw-1/6*np.conj(G_d)@np.conj(G_u)@Cquqd8*tw,rv,pvsw)-1/8*(G_d@G_u@Cquqd1*csw,pv,rvtw-1/6*G_d@G_u@Cquqd8*csw,pv,rvtw)+1/16*(np.conj(G_d)@np.conj(G_u)@Cquqd8*tw,rv,svpw+G_d@G_u@Cquqd8*csw,pv,tvrw)+GammaqCqq1*pv,vrst+Cqq1*Gammaqpvst,vr+1/18*gp**2*CCurlyPhiq1*Delta_pr,st-1/9*gp**2*Clq1*Delta_wwpr,st+1/9*gp**2*(2*Cqq1*Delta_stww,pr+1/3*(Cqq1*Delta_swwt,pr+3*Cqq3*Delta_swwt,pr))+1/3*gs**2*(Cqq1*Delta_pwwt,sr+3*Cqq3*Delta_pwwt,sr)-2/9*gs**2*(Cqq1*Delta_swwt,pr+3*Cqq3*Delta_swwt,pr)+2/9*gp**2*Cqu1*Delta_stww,pr-1/9*gp**2*Cqd1*Delta_stww,pr+1/12*gs**2*(Cqu8*Delta_ptww,sr+Cqd8*Delta_ptww,sr)-1/18*gs**2*(Cqu8*Delta_stww,pr+Cqd8*Delta_stww,pr)-1/9*gp**2*CqeDelta_stww,pr+1/2*(G_u@G_u.getH()@xCCurlyPhiq1*st,pr-G_d@G_d.getH()@xCCurlyPhiq1*st,pr)-1/2*(G_u@np.conj(G_u)@Cqu1*sv,tw,prvw-1/6*G_u@np.conj(G_u)@Cqu8*sv,tw,prvw)-1/2*(G_d@np.conj(G_d)@Cqd1*sv,tw,prvw-1/6*G_d@np.conj(G_d)@Cqd8*sv,tw,prvw)-1/8*(G_u@np.conj(G_u)@Cqu8*sv,rw,ptvw+G_d@np.conj(G_d)@Cqd8*sv,rw,ptvw)-1/8*(np.conj(G_d)@np.conj(G_u)@Cquqd1*rw,tv,svpw-1/6*np.conj(G_d)@np.conj(G_u)@Cquqd8*rw,tv,svpw)-1/8*(G_d@G_u@Cquqd1*cpw,sv,tvrw-1/6*G_d@G_u@Cquqd8*cpw,sv,tvrw)+1/16*(np.conj(G_d)@np.conj(G_u)@Cquqd8*rw,tv,pvsw+G_d@G_u@Cquqd8*cpw,sv,rvtw)+GammaqCqq1*sv,vtpr+Cqq1*Gammaqsvpr,vt+9*g**2*Cqq3*prst-2*(gs**2-1/6*gp**2)*Cqq1*prst+3*gs**2*(Cqq1*ptsr+3*Cqq3*ptsr)


Beta["qq3"]=1/6*g**2*CCurlyPhiq3*Delta_st,pr+1/3*g**2*Clq3*Delta_wwst,pr+1/3*g**2*(Cqq1*Delta_pwwr,st-Cqq3*Delta_pwwr,st)+2*g**2*Cqq3*Delta_prww,st+1/3*gs**2*(Cqq1*Delta_swwr,pt+3*Cqq3*Delta_swwr,pt)+1/12*gs**2*(Cqu8*Delta_srww,pt+Cqd8*Delta_srww,pt)-1/2*(G_u@G_u.getH()@xCCurlyPhiq3*pr,st+G_d@G_d.getH()@xCCurlyPhiq3*pr,st)-1/8*(G_u@np.conj(G_u)@Cqu8*pv,tw,srvw+G_d@np.conj(G_d)@Cqd8*pv,tw,srvw)+1/8*(np.conj(G_d)@np.conj(G_u)@Cquqd1*tw,rv,pvsw-1/6*np.conj(G_d)@np.conj(G_u)@Cquqd8*tw,rv,pvsw)+1/8*(G_d@G_u@Cquqd1*csw,pv,rvtw-1/6*G_d@G_u@Cquqd8*csw,pv,rvtw)-1/16*(np.conj(G_d)@np.conj(G_u)@Cquqd8*tw,rv,svpw+G_d@G_u@Cquqd8*csw,pv,tvrw)+GammaqCqq3*pv,vrst+Cqq3*Gammaqpvst,vr+1/6*g**2*CCurlyPhiq3*Delta_pr,st+1/3*g**2*Clq3*Delta_wwpr,st+1/3*g**2*(Cqq1*Delta_swwt,pr-Cqq3*Delta_swwt,pr)+2*g**2*Cqq3*Delta_stww,pr+1/3*gs**2*(Cqq1*Delta_pwwt,sr+3*Cqq3*Delta_pwwt,sr)+1/12*gs**2*(Cqu8*Delta_ptww,sr+Cqd8*Delta_ptww,sr)-1/2*(G_u@G_u.getH()@xCCurlyPhiq3*st,pr+G_d@G_d.getH()@xCCurlyPhiq3*st,pr)-1/8*(G_u@np.conj(G_u)@Cqu8*sv,rw,ptvw+G_d@np.conj(G_d)@Cqd8*sv,rw,ptvw)+1/8*(np.conj(G_d)@np.conj(G_u)@Cquqd1*rw,tv,svpw-1/6*np.conj(G_d)@np.conj(G_u)@Cquqd8*rw,tv,svpw)+1/8*(G_d@G_u@Cquqd1*cpw,sv,tvrw-1/6*G_d@G_u@Cquqd8*cpw,sv,tvrw)-1/16*(np.conj(G_d)@np.conj(G_u)@Cquqd8*rw,tv,pvsw+G_d@G_u@Cquqd8*cpw,sv,rvtw)+GammaqCqq3*sv,vtpr+Cqq3*Gammaqsvpr,vt+3*gs**2*(Cqq1*ptsr-Cqq3*ptsr)-2*(gs**2+3*g**2-1/6*gp**2)*Cqq3*prst+3*g**2*Cqq1*prst


Beta["lq1"]=-1/3*gp**2*CCurlyPhiq1*Delta_st,pr+1/9*gp**2*CCurlyPhil1*Delta_pr,st-2/9*gp**2*(2*CllDelta_prww,st+CllDelta_pwwr,st)+2/9*gp**2*Clq1*Delta_prww,st+2/3*gp**2*Clq1*Delta_wwst,pr-2/9*gp**2*(6*Cqq1*Delta_stww,pr+Cqq1*Delta_swwt,pr+3*Cqq3*Delta_swwt,pr)-2/3*gp**2*(2*Cqu1*Delta_stww,pr-Cqd1*Delta_stww,pr-CqeDelta_stww,pr)+2/9*gp**2*(2*CluDelta_prww,st-CldDelta_prww,st-CleDelta_prww,st)-gp**2*Clq1*prst+9*g**2*Clq3*prst-G_e@G_e.getH()@xCCurlyPhiq1*pr,st+G_u@G_u.getH()@xCCurlyPhil1*st,pr-G_d@G_d.getH()@xCCurlyPhil1*st,pr+1/4*(np.conj(G_u)@np.conj(G_e)@Clequ1*tw,rv,pvsw-12*np.conj(G_u)@np.conj(G_e)@Clequ3*tw,rv,pvsw+G_u@G_e@Clequ1*csw,pv,rvtw-12*G_u@G_e@Clequ3*csw,pv,rvtw)-G_u@np.conj(G_u)@Clusv,tw,prvw-G_d@np.conj(G_d)@Cldsv,tw,prvw-G_e@np.conj(G_e)@Cqepv,rw,stvw+1/4*(G_d@np.conj(G_e)@Cledqsw,rv,pvwt+G_e@np.conj(G_d)@Cledqcpv,tw,rvws)+GammalClq1*pv,vrst+GammaqClq1*sv,prvt+Clq1*Gammalpvst,vr+Clq1*Gammaqprsv,vt


Beta["lq3"]=1/3*g**2*(CCurlyPhiq3*Delta_st,pr+CCurlyPhil3*Delta_pr,st)+2/3*g**2*(3*Clq3*Delta_prww,st+Clq3*Delta_wwst,pr)+2/3*g**2*(6*Cqq3*Delta_stww,pr+Cqq1*Delta_swwt,pr-Cqq3*Delta_swwt,pr)+2/3*g**2*CllDelta_pwwr,st+3*g**2*Clq1*prst-(6*g**2+gp**2)*Clq3*prst-G_e@G_e.getH()@xCCurlyPhiq3*pr,st-G_u@G_u.getH()@xCCurlyPhil3*st,pr-G_d@G_d.getH()@xCCurlyPhil3*st,pr-1/4*(np.conj(G_u)@np.conj(G_e)@Clequ1*tw,rv,pvsw-12*np.conj(G_u)@np.conj(G_e)@Clequ3*tw,rv,pvsw+G_u@G_e@Clequ1*csw,pv,rvtw-12*G_u@G_e@Clequ3*csw,pv,rvtw)+1/4*(G_d@np.conj(G_e)@Cledqsw,rv,pvwt+G_e@np.conj(G_d)@Cledqcpv,tw,rvws)+GammalClq3*pv,vrst+GammaqClq3*sv,prvt+Clq3*Gammalpvst,vr+Clq3*Gammaqprsv,vt


Beta["ee"]=-1/3*gp**2*CCurlyPhieDelta_st,pr+2/3*gp**2*(CleDelta_wwpr,st-CqeDelta_wwpr,st-2*CeuDelta_prww,st+CedDelta_prww,st+4*CeeDelta_prww,st)+G_e.getH()@G_e@xCCurlyPhiepr,st-G_e@np.conj(G_e)@Clewr,vp,vwst+GammaeCeepv,vrst+CeeGammaepvst,vr-1/3*gp**2*CCurlyPhieDelta_pr,st+2/3*gp**2*(CleDelta_wwst,pr-CqeDelta_wwst,pr-2*CeuDelta_stww,pr+CedDelta_stww,pr+4*CeeDelta_wwst,pr)+G_e.getH()@G_e@xCCurlyPhiest,pr-G_e@np.conj(G_e)@Clewt,vs,vwpr+GammaeCeesv,vtpr+CeeGammaesvpr,vt+12*gp**2*Ceeprst


Beta["uu"]=2/9*gp**2*CCurlyPhiuDelta_st,pr-4/9*gp**2*(CeuDelta_wwst,pr+CluDelta_wwst,pr-Cqu1*Delta_wwst,pr-4*CuuDelta_wwst,pr-4/3*CuuDelta_swwt,pr)-1/9*gs**2*(Cqu8*Delta_wwst,pr-3*Cqu8*Delta_wwsr,pt)+2/3*gs**2*CuuDelta_pwwt,rs-2/9*gs**2*CuuDelta_swwt,pr-4/9*gp**2*Cud1*Delta_stww,pr-1/18*gs**2*(Cud8*Delta_stww,pr-3*Cud8*Delta_srww,pt)-G_u.getH()@G_u@xCCurlyPhiupr,st-(G_u@np.conj(G_u)@Cqu1*wr,vp,vwst-1/6*G_u@np.conj(G_u)@Cqu8*wr,vp,vwst)-1/2*G_u@np.conj(G_u)@Cqu8*wr,vs,vwpt+GammauCuupv,vrst+CuuGammaupvst,vr+2/9*gp**2*CCurlyPhiuDelta_pr,st-4/9*gp**2*(CeuDelta_wwpr,st+CluDelta_wwpr,st-Cqu1*Delta_wwpr,st-4*CuuDelta_wwpr,st-4/3*CuuDelta_pwwr,st)-1/9*gs**2*(Cqu8*Delta_wwpr,st-3*Cqu8*Delta_wwpt,sr)+2/3*gs**2*CuuDelta_swwr,tp-2/9*gs**2*CuuDelta_pwwr,st-4/9*gp**2*Cud1*Delta_prww,st-1/18*gs**2*(Cud8*Delta_prww,st-3*Cud8*Delta_ptww,sr)-G_u.getH()@G_u@xCCurlyPhiust,pr-(G_u@np.conj(G_u)@Cqu1*wt,vs,vwpr-1/6*G_u@np.conj(G_u)@Cqu8*wt,vs,vwpr)-1/2*G_u@np.conj(G_u)@Cqu8*wt,vp,vwsr+GammauCuusv,vtpr+CuuGammausvpr,vt+2*(8/3*gp**2-gs**2)*Cuuprst+6*gs**2*Cuuptsr


Beta["dd"]=-1/9*gp**2*CCurlyPhidDelta_st,pr+2/9*gp**2*(CedDelta_wwst,pr+CldDelta_wwst,pr-Cqd1*Delta_wwst,pr+2*CddDelta_wwst,pr+2/3*CddDelta_swwt,pr)-1/9*gs**2*(Cqd8*Delta_wwst,pr-3*Cqd8*Delta_wwsr,pt)+2/3*gs**2*CddDelta_pwwt,rs-2/9*gs**2*CddDelta_swwt,pr-4/9*gp**2*Cud1*Delta_wwst,pr-1/18*gs**2*(Cud8*Delta_wwst,pr-3*Cud8*Delta_wwsr,pt)+G_d.getH()@G_d@xCCurlyPhidpr,st-(G_d@np.conj(G_d)@Cqd1*wr,vp,vwst-1/6*G_d@np.conj(G_d)@Cqd8*wr,vp,vwst)-1/2*G_d@np.conj(G_d)@Cqd8*wr,vs,vwpt+GammadCddpv,vrst+CddGammadpvst,vr-1/9*gp**2*CCurlyPhidDelta_pr,st+2/9*gp**2*(CedDelta_wwpr,st+CldDelta_wwpr,st-Cqd1*Delta_wwpr,st+2*CddDelta_wwpr,st+2/3*CddDelta_pwwr,st)-1/9*gs**2*(Cqd8*Delta_wwpr,st-3*Cqd8*Delta_wwpt,sr)+2/3*gs**2*CddDelta_swwr,tp-2/9*gs**2*CddDelta_pwwr,st-4/9*gp**2*Cud1*Delta_wwpr,st-1/18*gs**2*(Cud8*Delta_wwpr,st-3*Cud8*Delta_wwpt,sr)+G_d.getH()@G_d@xCCurlyPhidst,pr-(G_d@np.conj(G_d)@Cqd1*wt,vs,vwpr-1/6*G_d@np.conj(G_d)@Cqd8*wt,vs,vwpr)-1/2*G_d@np.conj(G_d)@Cqd8*wt,vp,vwsr+GammadCddsv,vtpr+CddGammadsvpr,vt+2*(2/3*gp**2-gs**2)*Cddprst+6*gs**2*Cddptsr


Beta["eu"]=-2/3*gp**2*(CCurlyPhiuDelta_st,pr+2*(Cqu1*Delta_wwst,pr-CluDelta_wwst,pr+4*CuuDelta_wwst,pr-CeuDelta_wwst,pr-Cud1*Delta_stww,pr)+8/3*CuuDelta_swwt,pr)+4/9*gp**2*(CCurlyPhieDelta_pr,st+2*(CqeDelta_wwpr,st-CleDelta_wwpr,st-4*CeeDelta_prww,st+2*CeuDelta_prww,st-CedDelta_prww,st))-8*gp**2*Ceuprst+2*G_e.getH()@G_e@xCCurlyPhiupr,st-2*G_u.getH()@G_u@xCCurlyPhiest,pr+np.conj(G_e)@np.conj(G_u)@Clequ1*vp,ws,vrwt-12*np.conj(G_e)@np.conj(G_u)@Clequ3*vp,ws,vrwt+G_e@G_u@Clequ1*cvr,wt,vpws-12*G_e@G_u@Clequ3*cvr,wt,vpws-2*np.conj(G_e)@G_e@Cluvp,wr,vwst-2*np.conj(G_u)@G_u@Cqevs,wt,vwpr+GammaeCeupv,vrst+GammauCeusv,prvt+CeuGammaepvst,vr+CeuGammauprsv,vt


Beta["ed"]=-2/3*gp**2*(CCurlyPhidDelta_st,pr+2*(Cqd1*Delta_wwst,pr-CldDelta_wwst,pr-2*CddDelta_wwst,pr-CedDelta_wwst,pr+2*Cud1*Delta_wwst,pr)-4/3*CddDelta_swwt,pr)-2/9*gp**2*(CCurlyPhieDelta_pr,st+2*(CqeDelta_wwpr,st-CleDelta_wwpr,st-4*CeeDelta_prww,st-CedDelta_prww,st+2*CeuDelta_prww,st))+4*gp**2*Cedprst+2*G_e.getH()@G_e@xCCurlyPhidpr,st+2*G_d.getH()@G_d@xCCurlyPhiest,pr-2*np.conj(G_e)@G_e@Cldvp,wr,vwst-2*np.conj(G_d)@G_d@Cqevs,wt,vwpr+np.conj(G_e)@G_d@Cledqvp,wt,vrsw+G_e@np.conj(G_d)@Cledqcvr,ws,vptw+GammaeCedpv,vrst+GammadCedsv,prvt+CedGammaepvst,vr+CedGammadprsv,vt


Beta["ud1"]=4/9*gp**2*(CCurlyPhidDelta_st,pr+2*(Cqd1*Delta_wwst,pr-CldDelta_wwst,pr-2*CddDelta_wwst,pr+2*Cud1*Delta_wwst,pr-CedDelta_wwst,pr)-4/3*CddDelta_swwt,pr)-2/9*gp**2*(CCurlyPhiuDelta_pr,st+2*(Cqu1*Delta_wwpr,st-CluDelta_wwpr,st+4*CuuDelta_wwpr,st-Cud1*Delta_prww,st-CeuDelta_wwpr,st)+8/3*CuuDelta_pwwr,st)-8/3*(gp**2*Cud1*prst-gs**2*Cud8*prst)-2*G_u.getH()@G_u@xCCurlyPhidpr,st+2*G_d.getH()@G_d@xCCurlyPhiust,pr+2/3*G_d.getH()@G_u@xCCurlyPhiudsr,pt+2/3*G_u.getH()@G_d@xCCurlyPhiudcpt,rs+1/3*(np.conj(G_d)@np.conj(G_u)@Cquqd1*vs,wp,vrwt+4/3*np.conj(G_d)@np.conj(G_u)@Cquqd8*vs,wp,vrwt+G_d@G_u@Cquqd1*cvt,wr,vpws+4/3*G_d@G_u@Cquqd8*cvt,wr,vpws)-np.conj(G_d)@np.conj(G_u)@Cquqd1*ws,vp,vrwt-G_d@G_u@Cquqd1*cwt,vr,vpws-2*np.conj(G_u)@G_u@Cqd1*vp,wr,vwst-2*np.conj(G_d)@G_d@Cqu1*vs,wt,vwpr+GammauCud1*pv,vrst+GammadCud1*sv,prvt+Cud1*Gammaupvst,vr+Cud1*Gammadprsv,vt


Beta["ud8"]=8/3*gs**2*CuuDelta_pwwr,st+8/3*gs**2*CddDelta_swwt,pr+4/3*gs**2*Cqu8*Delta_wwpr,st+4/3*gs**2*Cqd8*Delta_wwst,pr+2/3*gs**2*Cud8*Delta_prww,st+2/3*gs**2*Cud8*Delta_wwst,pr-4*(2/3*gp**2+gs**2)*Cud8*prst+12*gs**2*Cud1*prst+4*G_d.getH()@G_u@xCCurlyPhiudsr,pt+4*G_u.getH()@G_d@xCCurlyPhiudcpt,rs+2*(np.conj(G_d)@np.conj(G_u)@Cquqd1*vs,wp,vrwt-1/6*np.conj(G_d)@np.conj(G_u)@Cquqd8*vs,wp,vrwt+G_d@G_u@Cquqd1*cvt,wr,vpws-1/6*G_d@G_u@Cquqd8*cvt,wr,vpws)-2*np.conj(G_u)@G_u@Cqd8*vp,wr,vwst-2*np.conj(G_d)@G_d@Cqu8*vs,wt,vwpr-(np.conj(G_d)@np.conj(G_u)@Cquqd8*ws,vp,vrwt+G_d@G_u@Cquqd8*cwt,vr,vpws)+GammauCud8*pv,vrst+GammadCud8*sv,prvt+Cud8*Gammaupvst,vr+Cud8*Gammadprsv,vt


Beta["le"]=-1/3*gp**2*CCurlyPhieDelta_st,pr-2/3*gp**2*CCurlyPhil1*Delta_pr,st+8/3*gp**2*CllDelta_prww,st+4/3*gp**2*CllDelta_pwwr,st-4/3*gp**2*Clq1*Delta_prww,st-2/3*gp**2*CqeDelta_wwst,pr+4/3*gp**2*CleDelta_prww,st+2/3*gp**2*CleDelta_wwst,pr-8/3*gp**2*CluDelta_prww,st+4/3*gp**2*CldDelta_prww,st-4/3*gp**2*CeuDelta_stww,pr+2/3*gp**2*CedDelta_stww,pr+8/3*gp**2*CeeDelta_wwst,pr-6*gp**2*Cleprst+np.conj(G_e)@Xiers,pt+G_e@Xiecpt,rs-G_e@G_e.getH()@xCCurlyPhiepr,st+2*G_e.getH()@G_e@xCCurlyPhil1*st,pr-4*G_e@np.conj(G_e)@Ceepv,rw,vtsw+G_e@np.conj(G_e)@Clepw,vs,vrwt-2*G_e@np.conj(G_e)@Cllwt,vs,pwvr-4*G_e@np.conj(G_e)@Cllwt,vs,prvw+G_e@np.conj(G_e)@Clevt,rw,pvsw+GammalClepv,vrst+GammaeClesv,prvt+CleGammalpvst,vr+CleGammaeprsv,vt


Beta["lu"]=-1/3*gp**2*CCurlyPhiuDelta_st,pr+4/9*gp**2*CCurlyPhil1*Delta_pr,st-16/9*gp**2*CllDelta_prww,st-8/9*gp**2*CllDelta_pwwr,st+8/9*gp**2*Clq1*Delta_prww,st-2/3*gp**2*Cqu1*Delta_wwst,pr+16/9*gp**2*CluDelta_prww,st+2/3*gp**2*CluDelta_wwst,pr-8/9*gp**2*CldDelta_prww,st-8/9*gp**2*CleDelta_prww,st+2/3*gp**2*Cud1*Delta_stww,pr+2/3*gp**2*CeuDelta_wwst,pr-8/3*gp**2*CuuDelta_stww,pr-8/9*gp**2*CuuDelta_swwt,pr+4*gp**2*Cluprst-G_e@G_e.getH()@xCCurlyPhiupr,st-2*G_u.getH()@G_u@xCCurlyPhil1*st,pr-1/2*(np.conj(G_e)@np.conj(G_u)@Clequ1*rv,ws,pvwt+12*np.conj(G_e)@np.conj(G_u)@Clequ3*rv,ws,pvwt)-1/2*(G_e@G_u@Clequ1*cpv,wt,rvws+12*G_e@G_u@Clequ3*cpv,wt,rvws)-2*np.conj(G_u)@G_u@Clq1*vs,wt,prvw-np.conj(G_e)@G_e@Ceurw,pv,vwst+GammalClupv,vrst+GammauClusv,prvt+CluGammalpvst,vr+CluGammauprsv,vt


Beta["ld"]=-1/3*gp**2*CCurlyPhidDelta_st,pr-2/9*gp**2*CCurlyPhil1*Delta_pr,st+8/9*gp**2*CllDelta_prww,st+4/9*gp**2*CllDelta_pwwr,st-4/9*gp**2*Clq1*Delta_prww,st-2/3*gp**2*Cqd1*Delta_wwst,pr+4/9*gp**2*CldDelta_prww,st+2/3*gp**2*CldDelta_wwst,pr-8/9*gp**2*CluDelta_prww,st+4/9*gp**2*CleDelta_prww,st-4/3*gp**2*Cud1*Delta_wwst,pr+2/3*gp**2*CedDelta_wwst,pr+4/3*gp**2*CddDelta_stww,pr+4/9*gp**2*CddDelta_swwt,pr-2*gp**2*Cldprst-G_e@G_e.getH()@xCCurlyPhidpr,st+2*G_d.getH()@G_d@xCCurlyPhil1*st,pr-1/2*np.conj(G_e)@G_d@Cledqrv,wt,pvsw-1/2*G_e@np.conj(G_d)@Cledqcpv,ws,rvtw-2*np.conj(G_d)@G_d@Clq1*vs,wt,prvw-np.conj(G_e)@G_e@Cedrw,pv,vwst+GammalCldpv,vrst+GammadCldsv,prvt+CldGammalpvst,vr+CldGammadprsv,vt


Beta["qe"]=1/9*gp**2*CCurlyPhieDelta_st,pr-2/3*gp**2*CCurlyPhiq1*Delta_pr,st-8/3*gp**2*Cqq1*Delta_prww,st-4/9*gp**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+4/3*gp**2*Clq1*Delta_wwpr,st-2/9*gp**2*CleDelta_wwst,pr+4/3*gp**2*CqeDelta_prww,st+2/9*gp**2*CqeDelta_wwst,pr-8/3*gp**2*Cqu1*Delta_prww,st+4/3*gp**2*Cqd1*Delta_prww,st+4/9*gp**2*CeuDelta_stww,pr-2/9*gp**2*CedDelta_stww,pr-8/9*gp**2*CeeDelta_wwst,pr+2*gp**2*Cqeprst+G_u@G_u.getH()@xCCurlyPhiepr,st-G_d@G_d.getH()@xCCurlyPhiepr,st+2*G_e.getH()@G_e@xCCurlyPhiq1*st,pr-1/2*G_d@np.conj(G_e)@Cledqpw,vs,vtwr-1/2*G_e@np.conj(G_d)@Cledqcvt,rw,vswp-2*np.conj(G_e)@G_e@Clq1*vs,wt,vwpr-1/2*(np.conj(G_u)@np.conj(G_e)@Clequ1*rw,vs,vtpw+12*np.conj(G_u)@np.conj(G_e)@Clequ3*rw,vs,vtpw)-1/2*(G_u@G_e@Clequ1*cpw,vt,vsrw+12*G_u@G_e@Clequ3*cpw,vt,vsrw)-np.conj(G_d)@G_d@Cedrw,pv,stvw-np.conj(G_u)@G_u@Ceurw,pv,stvw+GammaqCqepv,vrst+GammaeCqesv,prvt+CqeGammaqpvst,vr+CqeGammaeprsv,vt


Beta["qu1"]=1/9*gp**2*CCurlyPhiuDelta_st,pr+4/9*gp**2*CCurlyPhiq1*Delta_pr,st+16/9*gp**2*Cqq1*Delta_prww,st+8/27*gp**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)-8/9*gp**2*Clq1*Delta_wwpr,st-8/9*gp**2*CqeDelta_prww,st-8/9*gp**2*Cqd1*Delta_prww,st+16/9*gp**2*Cqu1*Delta_prww,st+2/9*gp**2*Cqu1*Delta_wwst,pr-2/9*gp**2*CluDelta_wwst,pr-2/9*gp**2*CeuDelta_wwst,pr-2/9*gp**2*Cud1*Delta_stww,pr+8/9*gp**2*CuuDelta_stww,pr+8/27*gp**2*CuuDelta_swwt,pr-4/3*gp**2*Cqu1*prst-8/3*gs**2*Cqu8*prst+1/3*np.conj(G_u)@Xiurs,pt+1/3*G_u@Xiucpt,rs+G_u@G_u.getH()@xCCurlyPhiupr,st-G_d@G_d.getH()@xCCurlyPhiupr,st-2*G_u.getH()@G_u@xCCurlyPhiq1*st,pr+1/3*(G_u@np.conj(G_u)@Cqu1*pw,vs,vrwt+4/3*G_u@np.conj(G_u)@Cqu8*pw,vs,vrwt)+1/3*(G_u@np.conj(G_u)@Cqu1*vt,rw,pvsw+4/3*G_u@np.conj(G_u)@Cqu8*vt,rw,pvsw)+1/3*(np.conj(G_d)@np.conj(G_u)@Cquqd1*rw,vs,ptvw+4/3*np.conj(G_d)@np.conj(G_u)@Cquqd8*rw,vs,ptvw)+1/3*(G_d@G_u@Cquqd1*cpw,vt,rsvw+4/3*G_d@G_u@Cquqd8*cpw,vt,rsvw)+1/2*np.conj(G_d)@np.conj(G_u)@Cquqd1*rw,vs,vtpw+1/2*G_d@G_u@Cquqd1*cpw,vt,vsrw-2/3*(G_u@np.conj(G_u)@Cqq1*vt,ws,pvwr+3*G_u@np.conj(G_u)@Cqq3*vt,ws,pvwr)-4*G_u@np.conj(G_u)@Cqq1*wt,vs,prvw-2/3*G_u@np.conj(G_u)@Cuupv,rw,vtsw-2*G_u@np.conj(G_u)@Cuupv,rw,vwst-G_d@np.conj(G_d)@Cud1*pv,rw,stvw+GammaqCqu1*pv,vrst+GammauCqu1*sv,prvt+Cqu1*Gammaqpvst,vr+Cqu1*Gammauprsv,vt


Beta["qd1"]=1/9*gp**2*CCurlyPhidDelta_st,pr-2/9*gp**2*CCurlyPhiq1*Delta_pr,st-8/9*gp**2*Cqq1*Delta_prww,st-4/27*gp**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+4/9*gp**2*Clq1*Delta_wwpr,st+4/9*gp**2*CqeDelta_prww,st-8/9*gp**2*Cqu1*Delta_prww,st+4/9*gp**2*Cqd1*Delta_prww,st+2/9*gp**2*Cqd1*Delta_wwst,pr-2/9*gp**2*CldDelta_wwst,pr-2/9*gp**2*CedDelta_wwst,pr+4/9*gp**2*Cud1*Delta_wwst,pr-4/9*gp**2*CddDelta_stww,pr-4/27*gp**2*CddDelta_swwt,pr+2/3*gp**2*Cqd1*prst-8/3*gs**2*Cqd8*prst+1/3*np.conj(G_d)@Xidrs,pt+1/3*G_d@Xidcpt,rs+G_u@G_u.getH()@xCCurlyPhidpr,st-G_d@G_d.getH()@xCCurlyPhidpr,st+2*G_d.getH()@G_d@xCCurlyPhiq1*st,pr+1/3*(G_d@np.conj(G_d)@Cqd1*pw,vs,vrwt+4/3*G_d@np.conj(G_d)@Cqd8*pw,vs,vrwt)+1/3*(G_d@np.conj(G_d)@Cqd1*vt,rw,pvsw+4/3*G_d@np.conj(G_d)@Cqd8*vt,rw,pvsw)+1/3*(np.conj(G_u)@np.conj(G_d)@Cquqd1*rw,vs,vwpt+4/3*np.conj(G_u)@np.conj(G_d)@Cquqd8*rw,vs,vwpt)+1/3*(G_u@G_d@Cquqd1*cpw,vt,vwrs+4/3*G_u@G_d@Cquqd8*cpw,vt,vwrs)+1/2*np.conj(G_d)@np.conj(G_u)@Cquqd1*ws,rv,pvwt+1/2*G_u@G_d@Cquqd1*cpv,wt,rvws-2/3*(G_d@np.conj(G_d)@Cqq1*vt,ws,pvwr+3*G_d@np.conj(G_d)@Cqq3*vt,ws,pvwr)-4*G_d@np.conj(G_d)@Cqq1*wt,vs,prvw-2/3*G_d@np.conj(G_d)@Cddpv,rw,vtsw-2*G_d@np.conj(G_d)@Cddpv,rw,vwst-G_u@np.conj(G_u)@Cud1*pv,rw,vwst+GammaqCqd1*pv,vrst+GammadCqd1*sv,prvt+Cqd1*Gammaqpvst,vr+Cqd1*Gammadprsv,vt


Beta["qu8"]=8/3*gs**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+2/3*gs**2*Cqu8*Delta_prww,st+2/3*gs**2*Cqd8*Delta_prww,st+4/3*gs**2*Cqu8*Delta_wwst,pr+2/3*gs**2*Cud8*Delta_stww,pr+8/3*gs**2*CuuDelta_swwt,pr-(4/3*gp**2+14*gs**2)*Cqu8*prst-12*gs**2*Cqu1*prst+2*np.conj(G_u)@Xiurs,pt+2*G_u@Xiucpt,rs+2*(G_u@np.conj(G_u)@Cqu1*pw,vs,vrwt-1/6*G_u@np.conj(G_u)@Cqu8*pw,vs,vrwt)+2*(G_u@np.conj(G_u)@Cqu1*vt,rw,pvsw-1/6*G_u@np.conj(G_u)@Cqu8*vt,rw,pvsw)+2*(np.conj(G_d)@np.conj(G_u)@Cquqd1*rw,vs,ptvw-1/6*np.conj(G_d)@np.conj(G_u)@Cquqd8*rw,vs,ptvw)+2*(G_d@G_u@Cquqd1*cpw,vt,rsvw-1/6*G_d@G_u@Cquqd8*cpw,vt,rsvw)+1/2*np.conj(G_u)@np.conj(G_d)@Cquqd8*vs,rw,vtpw+1/2*G_u@G_d@Cquqd8*cvt,pw,vsrw-4*(G_u@np.conj(G_u)@Cqq1*vt,ws,pvwr+3*G_u@np.conj(G_u)@Cqq3*vt,ws,pvwr)-4*G_u@np.conj(G_u)@Cuupv,rw,vtsw-G_d@np.conj(G_d)@Cud8*pv,rw,stvw+GammaqCqu8*pv,vrst+GammauCqu8*sv,prvt+Cqu8*Gammaqpvst,vr+Cqu8*Gammauprsv,vt


Beta["qd8"]=8/3*gs**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+2/3*gs**2*Cqu8*Delta_prww,st+2/3*gs**2*Cqd8*Delta_prww,st+4/3*gs**2*Cqd8*Delta_wwst,pr+2/3*gs**2*Cud8*Delta_wwst,pr+8/3*gs**2*CddDelta_swwt,pr-(-2/3*gp**2+14*gs**2)*Cqd8*prst-12*gs**2*Cqd1*prst+2*np.conj(G_d)@Xidrs,pt+2*G_d@Xidcpt,rs+2*(G_d@np.conj(G_d)@Cqd1*pw,vs,vrwt-1/6*G_d@np.conj(G_d)@Cqd8*pw,vs,vrwt)+2*(G_d@np.conj(G_d)@Cqd1*vt,rw,pvsw-1/6*G_d@np.conj(G_d)@Cqd8*vt,rw,pvsw)+2*(np.conj(G_u)@np.conj(G_d)@Cquqd1*rw,vs,vwpt-1/6*np.conj(G_u)@np.conj(G_d)@Cquqd8*rw,vs,vwpt)+2*(G_u@G_d@Cquqd1*cpw,vt,vwrs-1/6*G_u@G_d@Cquqd8*cpw,vt,vwrs)+1/2*np.conj(G_d)@np.conj(G_u)@Cquqd8*vs,rw,pwvt+1/2*G_d@G_u@Cquqd8*cvt,pw,rwvs-4*(G_d@np.conj(G_d)@Cqq1*vt,ws,pvwr+3*G_d@np.conj(G_d)@Cqq3*vt,ws,pvwr)-4*G_d@np.conj(G_d)@Cddpv,rw,vtsw-G_u@np.conj(G_u)@Cud8*pv,rw,vwst+GammaqCqd8*pv,vrst+GammadCqd8*sv,prvt+Cqd8*Gammaqpvst,vr+Cqd8*Gammadprsv,vt


Beta["ledq"]=-(8/3*gp**2+8*gs**2)*Cledqprst-2*np.conj(G_d)@Xiets,pr-2*G_e@Xidcrp,st+2*G_e@np.conj(G_d)@Cedpv,tw,vrsw-2*G_e@np.conj(G_d)@Cldvr,tw,pvsw+2*G_e@np.conj(G_d)@Clq1*vr,ws,pvwt+6*G_e@np.conj(G_d)@Clq3*vr,ws,pvwt-2*G_e@np.conj(G_d)@Cqepw,vs,vtwr+2*np.conj(G_d)@np.conj(G_u)@Clequ1*vs,tw,prvw+GammalCledqpv,vrst+GammaqCledqsv,prvt+CledqGammaepvst,vr+CledqGammadprsv,vt


Beta["quqd1"]=10/3*gp*CdBG_u@st,pr-6*g*CdWG_u@st,pr-20/9*gp*CdBG_u@pt,sr+4*g*CdWG_u@pt,sr-64/9*gs*CdGG_u@pt,sr-2/3*gp*CuBG_d@pr,st-6*g*CuWG_d@pr,st+4/9*gp*CuBG_d@sr,pt+4*g*CuWG_d@sr,pt-64/9*gs*CuGG_d@sr,pt-1/2*(11/9*gp**2+3*g**2+32*gs**2)*Cquqd1*prst-1/3*(-5/9*gp**2-3*g**2+64/3*gs**2)*Cquqd1*srpt-4/9*(-5/9*gp**2-3*g**2+28/3*gs**2)*Cquqd8*srpt+16/9*gs**2*Cquqd8*prst-2*G_u@Xidpr,st-2*G_d@Xiust,pr+4/3*(G_u@G_d@Cqd1*vr,pw,svwt+4/3*G_u@G_d@Cqd8*vr,pw,svwt+G_d@G_u@Cqu1*vt,sw,pvwr+4/3*G_d@G_u@Cqu8*vt,sw,pvwr+G_d@G_u@Cud1*pw,sv,vrwt+4/3*G_d@G_u@Cud8*pw,sv,vrwt)+8/3*(G_d@G_u@Cqq1*wt,vr,svpw-3*G_d@G_u@Cqq3*wt,vr,svpw-3*G_d@G_u@Cqq1*wt,vr,swpv+9*G_d@G_u@Cqq3*wt,vr,swpv)-4*G_d@G_u@Cud1*sw,pv,vrwt+GammaqCquqd1*pv,vrst+GammaqCquqd1*sv,prvt+Cquqd1*Gammaupvst,vr+Cquqd1*Gammadprsv,vt


Beta["quqd8"]=8*gs*CdGG_u@st,pr-40/3*gp*CdBG_u@pt,sr+24*g*CdWG_u@pt,sr+16/3*gs*CdGG_u@pt,sr+8*gs*CuGG_d@pr,st+8/3*gp*CuBG_d@sr,pt+24*g*CuWG_d@sr,pt+16/3*gs*CuGG_d@sr,pt+8*gs**2*Cquqd1*prst+(10/9*gp**2+6*g**2+16/3*gs**2)*Cquqd1*srpt+(-11/18*gp**2-3/2*g**2+16/3*gs**2)*Cquqd8*prst-1/3*(5/9*gp**2+3*g**2+44/3*gs**2)*Cquqd8*srpt+8*(G_u@G_d@Cqd1*vr,pw,svwt-1/6*G_u@G_d@Cqd8*vr,pw,svwt+G_d@G_u@Cqu1*vt,sw,pvwr-1/6*G_d@G_u@Cqu8*vt,sw,pvwr+G_d@G_u@Cud1*pw,sv,vrwt-1/6*G_d@G_u@Cud8*pw,sv,vrwt)+16*(G_d@G_u@Cqq1*wt,vr,svpw-3*G_d@G_u@Cqq3*wt,vr,svpw)-4*G_d@G_u@Cud8*sw,pv,vrwt+GammaqCquqd8*pv,vrst+GammaqCquqd8*sv,prvt+Cquqd8*Gammaupvst,vr+Cquqd8*Gammadprsv,vt


Beta["lequ1"]=-(11/3*gp**2+8*gs**2)*Clequ1*prst+(30*gp**2+18*g**2)*Clequ3*prst+2*G_u@Xiest,pr+2*G_e@Xiupr,st+2*G_d@G_u@Cledqsv,wt,prvw+2*G_e@G_u@Ceupv,sw,vrwt+2*G_e@G_u@Clq1*vr,wt,pvsw-6*G_e@G_u@Clq3*vr,wt,pvsw-2*G_e@G_u@Cluvr,sw,pvwt-2*G_e@G_u@Cqepw,vt,svwr+GammalClequ1*pv,vrst+GammaqClequ1*sv,prvt+Clequ1*Gammaepvst,vr+Clequ1*Gammauprsv,vt


Beta["lequ3"]=5/6*gp*CeBG_u@pr,st-3/2*g*CuWG_e@st,pr-3/2*gp*CuBG_e@st,pr-3/2*g*CeWG_u@pr,st+(2/9*gp**2-3*g**2+8/3*gs**2)*Clequ3*prst+1/8*(5*gp**2+3*g**2)*Clequ1*prst-1/2*G_u@G_e@Ceusw,pv,vrwt-1/2*G_e@G_u@Clq1*vr,wt,pvsw+3/2*G_e@G_u@Clq3*vr,wt,pvsw-1/2*G_e@G_u@Cluvr,sw,pvwt-1/2*G_e@G_u@Cqepw,vt,svwr+GammalClequ3*pv,vrst+GammaqClequ3*sv,prvt+Clequ3*Gammaepvst,vr+Clequ3*Gammauprsv,vt


Beta["duql"]=-(9/2*g**2+11/6*gp**2+4*gs**2)*Cduqlprst-np.conj(G_d)@G_d@Cduqlsv,wp,vrwt-np.conj(G_u)@G_u@Cduqlsv,wr,pvwt+2*np.conj(G_e)@np.conj(G_u)@Cduuetv,sw,prwv+np.conj(G_e)@np.conj(G_u)@Cduuetv,sw,pwrv+4*G_d@G_u@Cqqqlvp,wr,vwst+4*G_d@G_u@Cqqqlvp,wr,wvst-G_d@G_u@Cqqqlvp,wr,vswt-G_d@G_u@Cqqqlvp,wr,wsvt+2*G_d@np.conj(G_e)@Cqquewp,tv,wsrv+G_d.getH()@G_d@Cduqlvp,vrst+G_u.getH()@G_u@Cduqlvr,pvst+1/2*(G_u@G_u.getH()@Cduqlvs,prvt+G_d@G_d.getH()@Cduqlvs,prvt)+1/2*G_e@G_e.getH()@Cduqlvt,prsv


Beta["qque"]=-(9/2*g**2+23/6*gp**2+4*gs**2)*Cqqueprst-np.conj(G_u)@G_u@Cqquerv,ws,pwvt+1/2*G_e@np.conj(G_d)@Cduqlwt,rv,vspw-1/2*(2*np.conj(G_d)@np.conj(G_u)@Cduuepv,rw,vwst+np.conj(G_d)@np.conj(G_u)@Cduuepv,rw,vswt)+1/2*(-2*G_u@G_e@Cqqqlws,vt,prwv+G_u@G_e@Cqqqlws,vt,pwrv-2*G_u@G_e@Cqqqlws,vt,wprv)+1/2*(G_u@G_u.getH()@Cqquevp,vrst+G_d@G_d.getH()@Cqquevp,vrst)-np.conj(G_u)@G_u@Cqquepv,ws,rwvt+1/2*G_e@np.conj(G_d)@Cduqlwt,pv,vsrw-1/2*(2*np.conj(G_d)@np.conj(G_u)@Cduuerv,pw,vwst+np.conj(G_d)@np.conj(G_u)@Cduuerv,pw,vswt)+1/2*(-2*G_u@G_e@Cqqqlws,vt,rpwv+G_u@G_e@Cqqqlws,vt,rwpv-2*G_u@G_e@Cqqqlws,vt,wrpv)+1/2*(G_u@G_u.getH()@Cqquevr,vpst+G_d@G_d.getH()@Cqquevr,vpst)+G_u.getH()@G_u@Cqquevs,prvt+G_e.getH()@G_e@Cqquevt,prsv


Beta["qqql"]=-(3*g**2+1/3*gp**2+4*gs**2)*Cqqqlprst-4*g**2*(Cqqqlrpst+Cqqqlsrpt+Cqqqlpsrt)-4*np.conj(G_e)@np.conj(G_u)@Cqquetv,sw,prwv+2*(np.conj(G_d)@np.conj(G_u)@Cduqlpv,rw,vwst+np.conj(G_d)@np.conj(G_u)@Cduqlrv,pw,vwst)+1/2*(G_u@G_u.getH()@Cqqqlvp,vrst+G_d@G_d.getH()@Cqqqlvp,vrst)+1/2*(G_u@G_u.getH()@Cqqqlvr,pvst+G_d@G_d.getH()@Cqqqlvr,pvst)+1/2*(G_u@G_u.getH()@Cqqqlvs,prvt+G_d@G_d.getH()@Cqqqlvs,prvt)+1/2*G_e@G_e.getH()@Cqqqlvt,prsv


Beta["duue"]=-(2*gp**2+4*gs**2)*Cduueprst-20/3*gp**2*Cduuepsrt+4*G_u@G_e@Cduqlws,vt,prwv-8*G_d@G_u@Cqquevp,wr,vwst+G_d.getH()@G_d@Cduuevp,vrst+G_u.getH()@G_u@Cduuevr,pvst+G_u.getH()@G_u@Cduuevs,prvt+G_e.getH()@G_e@Cduuevt,prsv

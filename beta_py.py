#this file was formed from 'revision.py'


Beta["g"]=-19/6*g**3-8*g*m**2/HIGHSCALE**2*WC["CurlyPhiW"];


Beta["gp"]=41/6*gp**3-8*gp*m**2/HIGHSCALE**2*WC["CurlyPhiB"];


Beta["gs"]=-7*gs**3-8*gs*m**2/HIGHSCALE**2*WC["CurlyPhiG"];


Beta["Lambda"]=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)Lambda+4*Lambda*GammaH-4*(3*np.trace(d.G@d.Gh@d.G@d.Gh)+3*np.trace(u.G@u.Gh@u.G@u.Gh)+np.trace(e.G@e.Gh@e.G@e.Gh))+4*m**2/HIGHSCALE**2*(12*WC["CurlyPhi"]+(-16*Lambda+10/3*g**2)WC["CurlyPhiEmptySquare"]+(6*Lambda+3/2*(gp**2-g**2))WC["CurlyPhiD"]+2*(Eta1+Eta2)+9*g**2*WC["CurlyPhiW"]+3*gp**2*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+4/3*g**2*(TrCCurlyPhil3+3*TrCCurlyPhiq3));


Beta["m**2"]=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH+4*m**2/HIGHSCALE**2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"]));


Beta["u.G@X"]=3/2*(u.G@u.Gh@u.G-d.G@d.Gh@u.G)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)u.G+2*m**2/HIGHSCALE**2*(3*WC["uCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])u.G-CCurlyPhiq1*hu.G+3*CCurlyPhiq3*hu.G+u.G@CCurlyPhiuh-d.G@CCurlyPhiudh-2*(Cqu1*u.G@rpts,pt+4/3*Cqu8*u.G@rpts,pt)-Clequ1*e.G@cptrs,pt+3*Cquqd1*d.G@crspt,pt+1/2*(Cquqd1*d.G@cpsrt,pt+4/3*Cquqd8*d.G@cpsrt,pt));


Beta["d.G@X"]=3/2*(d.G@d.Gh@d.G-u.G@u.Gh@d.G)+(GammaH-9/4*g**2-5/12*gp**2-8*gs**2)d.G+2*m**2/HIGHSCALE**2*(3*WC["dCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])d.G+CCurlyPhiq1*hd.G+3*CCurlyPhiq3*hd.G-d.G@CCurlyPhidh-u.G@CCurlyPhiud-2*(Cqd1*d.G@rpts,pt+4/3*Cqd8*d.G@rpts,pt)+Cledqce.G@cptsr,tp+3*Cquqd1*u.G@cptrs,pt+1/2*(Cquqd1*u.G@crpts,pt+4/3*Cquqd8*u.G@crpts,pt));


Beta["e.G@X"]=3/2*e.G@e.Gh@e.G+(GammaH-3/4*(3*g**2+5*gp**2))e.G+2*m**2/HIGHSCALE**2*(3*WC["eCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])e.G+CCurlyPhil1*he.G+3*CCurlyPhil3*he.G-e.G@CCurlyPhieh-2*Clee.G@rpts,pt+3*Cledqd.G@rspt,tp-3*Clequ1*u.G@crspt,pt);


Beta["Theta"]=-iCPV 128*Pi**2/g**2*m**2/HIGHSCALE**2*WC["CurlyPhiWtilde"];


Beta["Thetap"]=-iCPV 128*Pi**2/gp**2*m**2/HIGHSCALE**2*WC["CurlyPhiBtilde"];


Beta["Thetas"]=-iCPV 128*Pi**2/gs**2*m**2/HIGHSCALE**2*WC["CurlyPhiGtilde"];


BetaSMg=-19/6*g**3;


BetaSMgp=41/6*gp**3;


BetaSMgs=-7*gs**3;


BetaSMLambda=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)Lambda+4*Lambda*GammaH-4*(3*np.trace(d.G@d.Gh@d.G@d.Gh)+3*np.trace(u.G@u.Gh@u.G@u.Gh)+np.trace(e.G@e.Gh@e.G@e.Gh));


BetaSMm**2=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH);


BetaSMu.G@X=3/2*(u.G@u.Gh@u.G-d.G@d.Gh@u.G)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)u.G@;


BetaSMd.G@X=3/2*(d.G@d.Gh@d.G-u.G@u.Gh@d.G)+(GammaH-9/4*g**2-5/12*gp**2-8*gs**2)d.G@;


BetaSMe.G@X=3/2*e.G@e.Gh@e.G+(GammaH-3/4*(3*g**2+5*gp**2))e.G@;


BetaSMTheta=0;


BetaSMThetap=0;


BetaSMThetas=0;


Beta["G"]=15*gs**2*WC["G"];


Beta["Gtilde"]=15*gs**2*WC["Gtilde"];


Beta["W"]=29/2*g**2*WC["W"];


Beta["Wtilde"]=29/2*g**2*WC["Wtilde"];


Beta["CurlyPhi"]=-9/2*(3*g**2+gp**2)WC["CurlyPhi"]+Lambda(20/3*g**2*WC["CurlyPhiEmptySquare"]+3*(gp**2-g**2)WC["CurlyPhiD"])-3/4*(g**2+gp**2)**2*WC["CurlyPhiD"]+6*Lambda(3*g**2*WC["CurlyPhiW"]+gp**2*WC["CurlyPhiB"]+g*gp*WC["CurlyPhiWB"])-3*(g**2*gp**2+3*g**4)WC["CurlyPhiW"]-3*(gp**4+g**2*gp**2)WC["CurlyPhiB"]-3*(g*gp**3+g**3*gp)WC["CurlyPhiWB"]+8/3*Lambda*g**2*(TrCCurlyPhil3+3*TrCCurlyPhiq3)+54*Lambda*WC["CurlyPhi"]-40*Lambda**2*WC["CurlyPhiEmptySquare"]+12*Lambda**2*WC["CurlyPhiD"]+4*Lambda(Eta1+Eta2)-4*(3*np.trace(CuCurlyPhiu.Gh@u.G@u.Gh)+3*np.trace(CdCurlyPhid.Gh@d.G@d.Gh)+np.trace(CeCurlyPhie.Gh@e.G@e.Gh)+3*cnp.trace(CuCurlyPhiu.Gh@u.G@u.Gh)+3*cnp.trace(CdCurlyPhid.Gh@d.G@d.Gh)+cnp.trace(CeCurlyPhie.Gh@e.G@e.Gh))+6*GammaH*WC["CurlyPhi"];


Beta["CurlyPhiEmptySquare"]=-(4*g**2+4/3*gp**2)WC["CurlyPhiEmptySquare"]+5/3*gp**2*WC["CurlyPhiD"]+2*g**2*(TrCCurlyPhil3+3*TrCCurlyPhiq3)+2/3*gp**2*(2*TrCCurlyPhiu-TrCCurlyPhid-TrCCurlyPhie+TrCCurlyPhiq1-TrCCurlyPhil1)+12*Lambda*WC["CurlyPhiEmptySquare"]-2*Eta3+4*GammaH*WC["CurlyPhiEmptySquare"];


Beta["CurlyPhiD"]=20/3*gp**2*WC["CurlyPhiEmptySquare"]+(9/2*g**2-5/6*gp**2)WC["CurlyPhiD"]+8/3*gp**2*(2*TrCCurlyPhiu-TrCCurlyPhid-TrCCurlyPhie+TrCCurlyPhiq1-TrCCurlyPhil1)+6*Lambda*WC["CurlyPhiD"]-2*Eta4+4*GammaH*WC["CurlyPhiD"];


Beta["CurlyPhiG"]=(-3/2*gp**2-9/2*g**2-14*gs**2)WC["CurlyPhiG"]+6*Lambda*WC["CurlyPhiG"]-2*gs(np.trace(CuGu.Gh)+np.trace(CdGd.Gh)+cnp.trace(CuGu.Gh)+cnp.trace(CdGd.Gh))+2*GammaH*WC["CurlyPhiG"];


Beta["CurlyPhiB"]=(85/6*gp**2-9/2*g**2)WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+6*Lambda*WC["CurlyPhiB"]+gp(-5*np.trace(CuBu.Gh)+np.trace(CdBd.Gh)+3*np.trace(CeBe.Gh)-5*cnp.trace(CuBu.Gh)+cnp.trace(CdBd.Gh)+3*cnp.trace(CeBe.Gh))+2*GammaH*WC["CurlyPhiB"];


Beta["CurlyPhiW"]=(-3/2*gp**2-53/6*g**2)WC["CurlyPhiW"]+g*gp*WC["CurlyPhiWB"]-15*g**3*WC["W"]+6*Lambda*WC["CurlyPhiW"]-g(3*np.trace(CuWu.Gh)+3*np.trace(CdWd.Gh)+np.trace(CeWe.Gh)+3*cnp.trace(CuWu.Gh)+3*cnp.trace(CdWd.Gh)+cnp.trace(CeWe.Gh))+2*GammaH*WC["CurlyPhiW"];


Beta["CurlyPhiWB"]=(19/3*gp**2+4/3*g**2)WC["CurlyPhiWB"]+2*g*gp(WC["CurlyPhiB"]+WC["CurlyPhiW"])+3*g**2*gp*WC["W"]+2*Lambda*WC["CurlyPhiWB"]+g(3*np.trace(CuBu.Gh)-3*np.trace(CdBd.Gh)-np.trace(CeBe.Gh)+3*cnp.trace(CuBu.Gh)-3*cnp.trace(CdBd.Gh)-cnp.trace(CeBe.Gh))+gp(5*np.trace(CuWu.Gh)+np.trace(CdWd.Gh)+3*np.trace(CeWe.Gh)+5*cnp.trace(CuWu.Gh)+cnp.trace(CdWd.Gh)+3*cnp.trace(CeWe.Gh))+2*GammaH*WC["CurlyPhiWB"];


Beta["CurlyPhiGtilde"]=(-3/2*gp**2-9/2*g**2-14*gs**2)WC["CurlyPhiGtilde"]+6*Lambda*WC["CurlyPhiGtilde"]+2*I*iCPV*gs(np.trace(CuGu.Gh)+np.trace(CdGd.Gh)-cnp.trace(CuGu.Gh)-cnp.trace(CdGd.Gh))+2*GammaH*WC["CurlyPhiGtilde"];


Beta["CurlyPhiBtilde"]=(85/6*gp**2-9/2*g**2)WC["CurlyPhiBtilde"]+3*g*gp*WC["CurlyPhiWtildeB"]+6*Lambda*WC["CurlyPhiBtilde"]-I*iCPV*gp(-5*np.trace(CuBu.Gh)+np.trace(CdBd.Gh)+3*np.trace(CeBe.Gh)+5*cnp.trace(CuBu.Gh)-cnp.trace(CdBd.Gh)-3*cnp.trace(CeBe.Gh))+2*GammaH*WC["CurlyPhiBtilde"];


Beta["CurlyPhiWtilde"]=(-3/2*gp**2-53/6*g**2)WC["CurlyPhiWtilde"]+g*gp*WC["CurlyPhiWtildeB"]-15*g**3*WC["Wtilde"]+6*Lambda*WC["CurlyPhiWtilde"]+I*iCPV*g(3*np.trace(CuWu.Gh)+3*np.trace(CdWd.Gh)+np.trace(CeWe.Gh)-3*cnp.trace(CuWu.Gh)-3*cnp.trace(CdWd.Gh)-cnp.trace(CeWe.Gh))+2*GammaH*WC["CurlyPhiWtilde"];


Beta["CurlyPhiWtildeB"]=(19/3*gp**2+4/3*g**2)WC["CurlyPhiWtildeB"]+2*g*gp(WC["CurlyPhiBtilde"]+WC["CurlyPhiWtilde"])+3*g**2*gp*WC["Wtilde"]+2*Lambda*WC["CurlyPhiWtildeB"]-I*iCPV*g(3*np.trace(CuBu.Gh)-3*np.trace(CdBd.Gh)-np.trace(CeBe.Gh)-3*cnp.trace(CuBu.Gh)+3*cnp.trace(CdBd.Gh)+cnp.trace(CeBe.Gh))-I*iCPV*gp(5*np.trace(CuWu.Gh)+np.trace(CdWd.Gh)+3*np.trace(CeWe.Gh)-5*cnp.trace(CuWu.Gh)-cnp.trace(CdWd.Gh)-3*cnp.trace(CeWe.Gh))+2*GammaH*WC["CurlyPhiWtildeB"];


Beta["uCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])+17/3*gp**2*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"])-g*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+4/3*g**2*(TrCCurlyPhil3+3*TrCCurlyPhiq3))u.G-(35/12*gp**2+27/4*g**2+8*gs**2)WC["uCurlyPhi"]-gp(5*gp**2-3*g**2)WC["uB"]+g(5*gp**2-9*g**2)WC["uW"]-(3*g**2-gp**2)u.G@CCurlyPhiu+3*g**2*d.G@CCurlyPhiudh+4*gp**2*CCurlyPhiq1*u.G-4*gp**2*CCurlyPhiq3*u.G-5*gp(CuBu.Gh@u.G+u.G@u.Gh@CuB)-3*g(CuWu.Gh@u.G-u.G@u.Gh@CuW)-16*gs(CuGu.Gh@u.G+u.G@u.Gh@CuG)-12*g*d.G@d.Gh@CuW-6*g*CdWd.Gh@u.G+Lambda(12*WC["uCurlyPhi"]-2*CCurlyPhiq1*u.G+6*CCurlyPhiq3*u.G+2*u.G@CCurlyPhiu-2*d.G@CCurlyPhiudh-2*WC["CurlyPhiEmptySquareu.G@"]+WC["CurlyPhiDu.G@"]-4*Cqu1*u.G@rpts,pt-16/3*Cqu8*u.G@rpts,pt-2*Clequ1*e.G@cptrs,pt+6*Cquqd1*d.G@crspt,pt+Cquqd1*d.G@cpsrt,pt+4/3*Cquqd8*d.G@cpsrt,pt)+2*(Eta1+Eta2-Eta5)u.G+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])u.G@u.Gh@u.G-2*CCurlyPhiq1*u.G@u.Gh@u.G+6*CCurlyPhiq3*d.G@d.Gh@u.G+2*u.G@u.Gh@u.G@CCurlyPhiu-2*d.G@d.Gh@d.G@CCurlyPhiudh+8*(Cqu1*u.G@u.Gh@u.G@rpts,pt+4/3*Cqu8*u.G@u.Gh@u.G@rpts,pt)-2*(Cquqd1*d.Gh@d.G@d.Gh@tsrp,pt+4/3*Cquqd8*d.Gh@d.G@d.Gh@tsrp,pt)-12*Cquqd1*d.Gh@d.G@d.Gh@rstp,pt+4*Clequ1*e.G@e.Gh@e.G@tprs,pt+4*CuCurlyPhiu.Gh@u.G+5*u.G@u.Gh@CuCurlyPhi-2*d.G@CdCurlyPhihu.G-CdCurlyPhid.Gh@u.G-2*d.G@d.Gh@CuCurlyPhi+3*GammaH*WC["uCurlyPhi"]+GammaqCuCurlyPhi+CuCurlyPhiGammau;


Beta["dCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)WC["CurlyPhiD"]+32*gs**2*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*g**2*(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])+5/3*gp**2*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"])+g*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+4/3*g**2*(TrCCurlyPhil3+3*TrCCurlyPhiq3))d.G-(23/12*gp**2+27/4*g**2+8*gs**2)WC["dCurlyPhi"]-gp(3*g**2-gp**2)WC["dB"]-g(9*g**2-gp**2)WC["dW"]+(3*g**2+gp**2)d.G@CCurlyPhid+3*g**2*u.G@CCurlyPhiud-2*gp**2*CCurlyPhiq1*d.G-2*gp**2*CCurlyPhiq3*d.G+gp(CdBd.Gh@d.G+d.G@d.Gh@CdB)-3*g(CdWd.Gh@d.G-d.G@d.Gh@CdW)-16*gs(CdGd.Gh@d.G+d.G@d.Gh@CdG)-12*g*u.G@u.Gh@CdW-6*g*CuWu.Gh@d.G+Lambda(12*WC["dCurlyPhi"]+2*CCurlyPhiq1*d.G+6*CCurlyPhiq3*d.G-2*d.G@CCurlyPhid-2*u.G@CCurlyPhiud-2*WC["CurlyPhiEmptySquared.G@"]+WC["CurlyPhiDd.G@"]-4*Cqd1*d.G@rpts,pt-16/3*Cqd8*d.G@rpts,pt+2*Cledqce.G@cptsr,tp+6*Cquqd1*u.G@cptrs,pt+Cquqd1*u.G@crtps,pt+4/3*Cquqd8*u.G@crtps,pt)+2*(Eta1+Eta2+Eta5)d.G+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])d.G@d.Gh@d.G+2*CCurlyPhiq1*d.G@d.Gh@d.G+6*CCurlyPhiq3*u.G@u.Gh@d.G-2*d.G@d.Gh@d.G@CCurlyPhid-2*u.G@u.Gh@u.G@CCurlyPhiud+8*(Cqd1*d.G@d.Gh@d.G@rpts,pt+4/3*Cqd8*d.G@d.Gh@d.G@rpts,pt)-2*(Cquqd1*u.Gh@u.G@u.Gh@rpts,pt+4/3*Cquqd8*u.Gh@u.G@u.Gh@rpts,pt)-12*Cquqd1*u.G@u.Gh@u.G@tprs,pt-4*Cledqce.G@e.Gh@e.G@ptsr,pt+4*CdCurlyPhid.Gh@d.G+5*d.G@d.Gh@CdCurlyPhi-2*u.G@CuCurlyPhihd.G-CuCurlyPhiu.Gh@d.G-2*u.G@u.Gh@CdCurlyPhi+3*GammaH*WC["dCurlyPhi"]+GammaqCdCurlyPhi+CdCurlyPhiGammad;


Beta["eCurlyPhi"]=(10/3*g**2*WC["CurlyPhiEmptySquare"]+3/2*(gp**2-g**2)WC["CurlyPhiD"]+9*g**2*(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])+15*gp**2*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"])-3*g*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+4/3*g**2*(TrCCurlyPhil3+3*TrCCurlyPhiq3))e.G-3/4*(7*gp**2+9*g**2)WC["eCurlyPhi"]-3*gp(g**2-3*gp**2)WC["eB"]-9*g(g**2-gp**2)WC["eW"]+3*(g**2-gp**2)e.G@CCurlyPhie-6*gp**2*CCurlyPhil1*e.G-6*gp**2*CCurlyPhil3*e.G+9*gp(CeBe.Gh@e.G+e.G@e.Gh@CeB)-3*g(CeWe.Gh@e.G-e.G@e.Gh@CeW)+Lambda(12*WC["eCurlyPhi"]+2*CCurlyPhil1*e.G+6*CCurlyPhil3*e.G-2*e.G@CCurlyPhie-2*WC["CurlyPhiEmptySquaree.G@"]+WC["CurlyPhiDe.G@"]-4*Clee.G@rpts,pt+6*Cledqd.G@rspt,pt-6*Clequ1*u.G@crspt,pt)+2*(Eta1+Eta2+Eta5)e.G+(WC["CurlyPhiD"]-6*WC["CurlyPhiEmptySquare"])e.G@e.Gh@e.G+2*CCurlyPhil1*e.G@e.Gh@e.G-2*e.G@e.Gh@e.G@CCurlyPhie+8*Clee.G@e.Gh@e.G@rpts,pt-12*Cledqd.G@d.Gh@d.G@rspt,tp+12*Clequ1*u.Gh@u.G@u.Gh@rstp,pt+4*CeCurlyPhie.Gh@e.G+5*e.G@e.Gh@CeCurlyPhi+3*GammaH*WC["eCurlyPhi"]+GammalCeCurlyPhi+CeCurlyPhiGammae;


Beta["eW"]=1/12*(3*gp**2-11*g**2)WC["eW"]-1/2*g*gp*WC["eB"]-(g(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])-3/2*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"]))e.G-6*g*Clequ3*u.G@crspt,pt+CeWe.Gh@e.G+GammaH*WC["eW"]+GammalCeW+CeWGammae;


Beta["eB"]=1/4*(151/3*gp**2-9*g**2)WC["eB"]-3/2*g*gp*WC["eW"]-(3/2*g(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])-3*gp(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"]))e.G+10*gp*Clequ3*u.G@crspt,pt+CeBe.Gh@e.G+2*e.G@e.Gh@CeB+GammaH*WC["eB"]+GammalCeB+CeBGammae;


Beta["uG"]=-1/36*(81*g**2+19*gp**2+204*gs**2)WC["uG"]+6*g*gs*WC["uW"]+10/3*gp*gs*WC["uB"]-gs(4*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*gs(WC["G"]+I*iCPV*WC["Gtilde"]))u.G-gs(Cquqd1*d.G@cpsrt,pt-1/6*Cquqd8*d.G@cpsrt,pt)+2*u.G@u.Gh@CuG-2*d.G@d.Gh@CuG-CdGd.Gh@u.G+CuGu.Gh@u.G+GammaH*WC["uG"]+GammaqCuG+CuGGammau;


Beta["uW"]=-1/36*(33*g**2+19*gp**2-96*gs**2)WC["uW"]+8/3*g*gs*WC["uG"]-1/6*g*gp*WC["uB"]-(g(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])-5/6*gp(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"]))u.G+g/4*(Cquqd1*d.G@cpsrt,pt+4/3*Cquqd8*d.G@cpsrt,pt)-2*g*Clequ3*e.G@cptrs,tp+2*d.G@d.Gh@CuW-CdWd.Gh@u.G+CuWu.Gh@u.G+GammaH*WC["uW"]+GammaqCuW+CuWGammau;


Beta["uB"]=-1/36*(81*g**2-313*gp**2-96*gs**2)WC["uB"]+40/9*gp*gs*WC["uG"]-1/2*g*gp*WC["uW"]-(-3/2*g(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])+5/3*gp(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"]))u.G+gp/12*(Cquqd1*d.G@cpsrt,pt+4/3*Cquqd8*d.G@cpsrt,pt)-6*gp*Clequ3*e.G@cptrs,tp+2*u.G@u.Gh@CuB-2*d.G@d.Gh@CuB-CdBd.Gh@u.G+CuBu.Gh@u.G+GammaH*WC["uB"]+GammaqCuB+CuBGammau;


Beta["dG"]=-1/36*(81*g**2+31*gp**2+204*gs**2)WC["dG"]+6*g*gs*WC["dW"]-2/3*gp*gs*WC["dB"]-gs(4*(WC["CurlyPhiG"]+I*iCPV*WC["CurlyPhiGtilde"])+9*gs(WC["G"]+I*iCPV*WC["Gtilde"]))d.G-gs(Cquqd1*u.G@crtps,pt-1/6*Cquqd8*u.G@crtps,pt)-2*u.G@u.Gh@CdG+2*d.G@d.Gh@CdG-CuGu.Gh@d.G+CdGd.Gh@d.G+GammaH*WC["dG"]+GammaqCdG+CdGGammad;


Beta["dW"]=-1/36*(33*g**2+31*gp**2-96*gs**2)WC["dW"]+8/3*g*gs*WC["dG"]+5/6*g*gp*WC["dB"]-(g(WC["CurlyPhiW"]+I*iCPV*WC["CurlyPhiWtilde"])-gp/6*(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"]))d.G+g/4*(Cquqd1*u.G@crtps,pt+4/3*Cquqd8*u.G@crtps,pt)+2*u.G@u.Gh@CdW-CuWu.Gh@d.G+CdWd.Gh@d.G+GammaH*WC["dW"]+GammaqCdW+CdWGammad;


Beta["dB"]=-1/36*(81*g**2-253*gp**2-96*gs**2)WC["dB"]-8/9*gp*gs*WC["dG"]+5/2*g*gp*WC["dW"]-(3/2*g(WC["CurlyPhiWB"]+I*iCPV*WC["CurlyPhiWtildeB"])-gp/3*(WC["CurlyPhiB"]+I*iCPV*WC["CurlyPhiBtilde"]))d.G-5/12*gp(Cquqd1*u.G@crtps,pt+4/3*Cquqd8*u.G@crtps,pt)-2*u.G@u.Gh@CdB+2*d.G@d.Gh@CdB-CuBu.Gh@d.G+CdBd.Gh@d.G+GammaH*WC["dB"]+GammaqCdB+CdBGammad;


Beta["CurlyPhil1"]=-1/4*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhil"]1-2/3*gp**2*(Cldrstt+Clerstt+2*Cllrstt+Cllrtts-Clq1*rstt-2*Clurstt)-1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])e.G@e.Gh-e.G@CCurlyPhiee.Gh+3/2*(e.G@e.Gh@CCurlyPhil1+CCurlyPhil1*e.G@e.Gh+3*e.G@e.Gh@CCurlyPhil3+3*CCurlyPhil3*e.G@e.Gh)+2*Clee.Gh@e.G@rspt,tp-2*(2*Clle.G@e.Gh@rspt,tp+Clle.G@e.Gh@rtps,tp)-6*Clq1*d.G@d.Gh@rspt,tp+6*Clq1*u.G@u.Gh@rspt,tp-6*Cluu.Gh@u.G@rspt,tp+6*Cldd.Gh@d.G@rspt,tp+2*GammaH*WC["CurlyPhil"]1+GammalCCurlyPhil1+CCurlyPhil1*Gammal;


Beta["CurlyPhil3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+TrCCurlyPhil3+3*TrCCurlyPhiq3)I3-17/3*g**2*WC["CurlyPhil"]3+2/3*g**2*Cllrtts+2*g**2*Clq3*rstt-1/2*WC["CurlyPhiEmptySquaree.G@e.Gh@"]+1/2*(3*e.G@e.Gh@CCurlyPhil1+3*CCurlyPhil1*e.G@e.Gh+e.G@e.Gh@CCurlyPhil3+CCurlyPhil3*e.G@e.Gh)-2*(Clle.G@e.Gh@rtps,tp)-6*Clq3*d.G@d.Gh@rspt,tp-6*Clq3*u.G@u.Gh@rspt,tp+2*GammaH*WC["CurlyPhil"]3+GammalCCurlyPhil3+CCurlyPhil3*Gammal;


Beta["CurlyPhie"]=-1/2*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhie"]-2/3*gp**2*(Cedrstt+4*Ceerstt-2*Ceurstt+Clettrs-Cqettrs)+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])e.Gh@e.G-2*e.Gh@CCurlyPhil1*e.G+3*(e.Gh@e.G@CCurlyPhie+CCurlyPhiee.Gh@e.G)-2*Clee.G@e.Gh@ptrs,tp+8*Ceee.Gh@e.G@rspt,tp-6*Ceuu.Gh@u.G@rspt,tp+6*Cedd.Gh@d.G@rspt,tp-6*Cqed.G@d.Gh@ptrs,tp+6*Cqeu.G@u.Gh@ptrs,tp+2*GammaH*WC["CurlyPhie"]+GammaeCCurlyPhie+CCurlyPhieGammae;


Beta["CurlyPhiq1"]=1/12*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiq"]1-2/3*gp**2*(Clq1*ttrs+Cqd1*rstt-2*Cqu1*rstt+Cqerstt-2*Cqq1*rstt-1/3*Cqq1*rtts-Cqq3*rtts)+1/2*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])(u.G@u.Gh-d.G@d.Gh)-u.G@CCurlyPhiuu.Gh-d.G@CCurlyPhidd.Gh+2*Cqee.Gh@e.G@rspt,tp-2*Clq1*e.G@e.Gh@ptrs,tp+3/2*(d.G@d.Gh@CCurlyPhiq1+u.G@u.Gh@CCurlyPhiq1+CCurlyPhiq1*d.G@d.Gh+CCurlyPhiq1*u.G@u.Gh+3*d.G@d.Gh@CCurlyPhiq3-3*u.G@u.Gh@CCurlyPhiq3+3*CCurlyPhiq3*d.G@d.Gh-3*CCurlyPhiq3*u.G@u.Gh)-2*(6*Cqq1*d.G@d.Gh@ptrs,tp+Cqq1*d.G@d.Gh@psrt,tp+3*Cqq3*d.G@d.Gh@psrt,tp-6*Cqq1*u.G@u.Gh@ptrs,tp-Cqq1*u.G@u.Gh@psrt,tp-3*Cqq3*u.G@u.Gh@psrt,tp)-6*Cqu1*u.Gh@u.G@rspt,tp+6*Cqd1*d.Gh@d.G@rspt,tp+2*GammaH*WC["CurlyPhiq"]1+GammaqCCurlyPhiq1+CCurlyPhiq1*Gammaq;


Beta["CurlyPhiq3"]=2/3*g**2*(1/4*WC["CurlyPhiEmptySquare"]+TrCCurlyPhil3+3*TrCCurlyPhiq3)I3-17/3*g**2*WC["CurlyPhiq"]3+2/3*g**2*(Clq3*ttrs+Cqq1*rtts+6*Cqq3*rstt-Cqq3*rtts)-1/2*WC["CurlyPhiEmptySquare"](u.G@u.Gh+d.G@d.Gh)+1/2*(3*d.G@d.Gh@CCurlyPhiq1-3*u.G@u.Gh@CCurlyPhiq1+3*CCurlyPhiq1*d.G@d.Gh-3*CCurlyPhiq1*u.G@u.Gh+d.G@d.Gh@CCurlyPhiq3+u.G@u.Gh@CCurlyPhiq3+CCurlyPhiq3*d.G@d.Gh+CCurlyPhiq3*u.G@u.Gh)-2*(6*Cqq3*d.G@d.Gh@rspt,tp+Cqq1*d.G@d.Gh@rtps,tp-Cqq3*d.G@d.Gh@rtps,tp+6*Cqq3*u.G@u.Gh@rspt,tp+Cqq1*u.G@u.Gh@rtps,tp-Cqq3*u.G@u.Gh@rtps,tp)-2*Clq3*e.G@e.Gh@ptrs,tp+2*GammaH*WC["CurlyPhiq"]3+GammaqCCurlyPhiq3+CCurlyPhiq3*Gammaq;


Beta["CurlyPhiu"]=1/3*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhiu"]-2/3*gp**2*(Ceuttrs+Cluttrs-Cqu1*ttrs+Cud1*rstt-4*Cuurstt-4/3*Cuurtts)-(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])u.Gh@u.G-2*u.Gh@CCurlyPhiq1*u.G+3*(u.Gh@u.G@CCurlyPhiu+CCurlyPhiuu.Gh@u.G)+u.Gh@d.G@CCurlyPhiudh+CCurlyPhiudd.Gh@u.G-4*(3*Cuuu.Gh@u.G@rspt,tp+Cuuu.Gh@u.G@rtps,tp)+2*Ceue.Gh@e.G@ptrs,tp-2*Clue.G@e.Gh@ptrs,tp+6*Cud1*d.Gh@d.G@rspt,tp-6*Cqu1*d.G@d.Gh@ptrs,tp+6*Cqu1*u.G@u.Gh@ptrs,tp+2*GammaH*WC["CurlyPhiu"]+GammauCCurlyPhiu+CCurlyPhiuGammau;


Beta["CurlyPhid"]=-1/6*XiB*gp**2*I3+1/3*gp**2*WC["CurlyPhid"]-2/3*gp**2*(2*Cddrstt+2/3*Cddrtts+Cedttrs+Cldttrs-Cqd1*ttrs-2*Cud1*ttrs)+(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])d.Gh@d.G-2*d.Gh@CCurlyPhiq1*d.G+3*(d.Gh@d.G@CCurlyPhid+CCurlyPhidd.Gh@d.G)-d.Gh@u.G@CCurlyPhiud-CCurlyPhiudhu.Gh@d.G+4*(3*Cddd.Gh@d.G@rspt,tp+Cddd.Gh@d.G@rtps,tp)+2*Cede.Gh@e.G@ptrs,tp-2*Clde.G@e.Gh@ptrs,tp-6*Cud1*u.Gh@u.G@ptrs,tp-6*Cqd1*d.G@d.Gh@ptrs,tp+6*Cqd1*u.G@u.Gh@ptrs,tp+2*GammaH*WC["CurlyPhid"]+GammadCCurlyPhid+CCurlyPhidGammad;


Beta["CurlyPhiud"]=-3*gp**2*WC["CurlyPhiud"]+(2*WC["CurlyPhiEmptySquare"]-WC["CurlyPhiD"])u.Gh@d.G-2*u.Gh@d.G@CCurlyPhid+2*CCurlyPhiuu.Gh@d.G+4*(Cud1*u.Gh@d.G@rtps,tp+4/3*Cud8*u.Gh@d.G@rtps,tp)+2*u.Gh@u.G@CCurlyPhiud+2*CCurlyPhiudd.Gh@d.G+2*GammaH*WC["CurlyPhiud"]+GammauCCurlyPhiud+CCurlyPhiudGammad;


Beta["ll"]=-1/6*gp**2*CCurlyPhil1*Delta_st,pr-1/6*g**2*(CCurlyPhil3*Delta_st,pr-2*CCurlyPhil3*Delta_sr,pt)+1/3*gp**2*(2*CllDelta_prww,st+CllDelta_pwwr,st)-1/3*g**2*CllDelta_pwwr,st+2/3*g**2*CllDelta_swwr,pt-1/3*gp**2*Clq1*Delta_prww,st-g**2*Clq3*Delta_prww,st+2*g**2*Clq3*Delta_ptww,rs+1/3*gp**2*(-2*CluDelta_prww,st+CldDelta_prww,st+CleDelta_prww,st)-1/2*(e.G@e.Gh@xCCurlyPhil1*pr,st-e.G@e.Gh@xCCurlyPhil3*pr,st)-e.G@e.Gh@xCCurlyPhil3*pt,sr-1/2*e.G@e.G@cClesv,tw,prvw+GammalCllpv,vrst+CllGammalpvst,vr-1/6*gp**2*CCurlyPhil1*Delta_pr,st-1/6*g**2*(CCurlyPhil3*Delta_pr,st-2*CCurlyPhil3*Delta_pt,sr)+1/3*gp**2*(2*CllDelta_stww,pr+CllDelta_swwt,pr)-1/3*g**2*CllDelta_swwt,pr+2/3*g**2*CllDelta_pwwt,sr-1/3*gp**2*Clq1*Delta_stww,pr-g**2*Clq3*Delta_stww,pr+2*g**2*Clq3*Delta_srww,tp+1/3*gp**2*(-2*CluDelta_stww,pr+CldDelta_stww,pr+CleDelta_stww,pr)-1/2*(e.G@e.Gh@xCCurlyPhil1*st,pr-e.G@e.Gh@xCCurlyPhil3*st,pr)-e.G@e.Gh@xCCurlyPhil3*sr,pt-1/2*e.G@e.G@cClepv,rw,stvw+GammalCllsv,vtpr+CllGammalsvpr,vt+6*g**2*Cllptsr+3*(gp**2-g**2)Cllprst;


Beta["qq1"]=1/18*gp**2*CCurlyPhiq1*Delta_st,pr-1/9*gp**2*Clq1*Delta_wwst,pr+1/9*gp**2*(2*Cqq1*Delta_prww,st+1/3*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st))+1/3*gs**2*(Cqq1*Delta_swwr,pt+3*Cqq3*Delta_swwr,pt)-2/9*gs**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+2/9*gp**2*Cqu1*Delta_prww,st-1/9*gp**2*Cqd1*Delta_prww,st+1/12*gs**2*(Cqu8*Delta_srww,pt+Cqd8*Delta_srww,pt)-1/18*gs**2*(Cqu8*Delta_prww,st+Cqd8*Delta_prww,st)-1/9*gp**2*CqeDelta_prww,st+1/2*(u.G@u.Gh@xCCurlyPhiq1*pr,st-d.G@d.Gh@xCCurlyPhiq1*pr,st)-1/2*(u.G@u.G@cCqu1*pv,rw,stvw-1/6*u.G@u.G@cCqu8*pv,rw,stvw)-1/2*(d.G@d.G@cCqd1*pv,rw,stvw-1/6*d.G@d.G@cCqd8*pv,rw,stvw)-1/8*(u.G@u.G@cCqu8*pv,tw,srvw+d.G@d.G@cCqd8*pv,tw,srvw)-1/8*(d.G@cu.G@cCquqd1*tw,rv,pvsw-1/6*d.G@cu.G@cCquqd8*tw,rv,pvsw)-1/8*(d.G@u.G@Cquqd1*csw,pv,rvtw-1/6*d.G@u.G@Cquqd8*csw,pv,rvtw)+1/16*(d.G@cu.G@cCquqd8*tw,rv,svpw+d.G@u.G@Cquqd8*csw,pv,tvrw)+GammaqCqq1*pv,vrst+Cqq1*Gammaqpvst,vr+1/18*gp**2*CCurlyPhiq1*Delta_pr,st-1/9*gp**2*Clq1*Delta_wwpr,st+1/9*gp**2*(2*Cqq1*Delta_stww,pr+1/3*(Cqq1*Delta_swwt,pr+3*Cqq3*Delta_swwt,pr))+1/3*gs**2*(Cqq1*Delta_pwwt,sr+3*Cqq3*Delta_pwwt,sr)-2/9*gs**2*(Cqq1*Delta_swwt,pr+3*Cqq3*Delta_swwt,pr)+2/9*gp**2*Cqu1*Delta_stww,pr-1/9*gp**2*Cqd1*Delta_stww,pr+1/12*gs**2*(Cqu8*Delta_ptww,sr+Cqd8*Delta_ptww,sr)-1/18*gs**2*(Cqu8*Delta_stww,pr+Cqd8*Delta_stww,pr)-1/9*gp**2*CqeDelta_stww,pr+1/2*(u.G@u.Gh@xCCurlyPhiq1*st,pr-d.G@d.Gh@xCCurlyPhiq1*st,pr)-1/2*(u.G@u.G@cCqu1*sv,tw,prvw-1/6*u.G@u.G@cCqu8*sv,tw,prvw)-1/2*(d.G@d.G@cCqd1*sv,tw,prvw-1/6*d.G@d.G@cCqd8*sv,tw,prvw)-1/8*(u.G@u.G@cCqu8*sv,rw,ptvw+d.G@d.G@cCqd8*sv,rw,ptvw)-1/8*(d.G@cu.G@cCquqd1*rw,tv,svpw-1/6*d.G@cu.G@cCquqd8*rw,tv,svpw)-1/8*(d.G@u.G@Cquqd1*cpw,sv,tvrw-1/6*d.G@u.G@Cquqd8*cpw,sv,tvrw)+1/16*(d.G@cu.G@cCquqd8*rw,tv,pvsw+d.G@u.G@Cquqd8*cpw,sv,rvtw)+GammaqCqq1*sv,vtpr+Cqq1*Gammaqsvpr,vt+9*g**2*Cqq3*prst-2*(gs**2-1/6*gp**2)Cqq1*prst+3*gs**2*(Cqq1*ptsr+3*Cqq3*ptsr);


Beta["qq3"]=1/6*g**2*CCurlyPhiq3*Delta_st,pr+1/3*g**2*Clq3*Delta_wwst,pr+1/3*g**2*(Cqq1*Delta_pwwr,st-Cqq3*Delta_pwwr,st)+2*g**2*Cqq3*Delta_prww,st+1/3*gs**2*(Cqq1*Delta_swwr,pt+3*Cqq3*Delta_swwr,pt)+1/12*gs**2*(Cqu8*Delta_srww,pt+Cqd8*Delta_srww,pt)-1/2*(u.G@u.Gh@xCCurlyPhiq3*pr,st+d.G@d.Gh@xCCurlyPhiq3*pr,st)-1/8*(u.G@u.G@cCqu8*pv,tw,srvw+d.G@d.G@cCqd8*pv,tw,srvw)+1/8*(d.G@cu.G@cCquqd1*tw,rv,pvsw-1/6*d.G@cu.G@cCquqd8*tw,rv,pvsw)+1/8*(d.G@u.G@Cquqd1*csw,pv,rvtw-1/6*d.G@u.G@Cquqd8*csw,pv,rvtw)-1/16*(d.G@cu.G@cCquqd8*tw,rv,svpw+d.G@u.G@Cquqd8*csw,pv,tvrw)+GammaqCqq3*pv,vrst+Cqq3*Gammaqpvst,vr+1/6*g**2*CCurlyPhiq3*Delta_pr,st+1/3*g**2*Clq3*Delta_wwpr,st+1/3*g**2*(Cqq1*Delta_swwt,pr-Cqq3*Delta_swwt,pr)+2*g**2*Cqq3*Delta_stww,pr+1/3*gs**2*(Cqq1*Delta_pwwt,sr+3*Cqq3*Delta_pwwt,sr)+1/12*gs**2*(Cqu8*Delta_ptww,sr+Cqd8*Delta_ptww,sr)-1/2*(u.G@u.Gh@xCCurlyPhiq3*st,pr+d.G@d.Gh@xCCurlyPhiq3*st,pr)-1/8*(u.G@u.G@cCqu8*sv,rw,ptvw+d.G@d.G@cCqd8*sv,rw,ptvw)+1/8*(d.G@cu.G@cCquqd1*rw,tv,svpw-1/6*d.G@cu.G@cCquqd8*rw,tv,svpw)+1/8*(d.G@u.G@Cquqd1*cpw,sv,tvrw-1/6*d.G@u.G@Cquqd8*cpw,sv,tvrw)-1/16*(d.G@cu.G@cCquqd8*rw,tv,pvsw+d.G@u.G@Cquqd8*cpw,sv,rvtw)+GammaqCqq3*sv,vtpr+Cqq3*Gammaqsvpr,vt+3*gs**2*(Cqq1*ptsr-Cqq3*ptsr)-2*(gs**2+3*g**2-1/6*gp**2)Cqq3*prst+3*g**2*Cqq1*prst;


Beta["lq1"]=-1/3*gp**2*CCurlyPhiq1*Delta_st,pr+1/9*gp**2*CCurlyPhil1*Delta_pr,st-2/9*gp**2*(2*CllDelta_prww,st+CllDelta_pwwr,st)+2/9*gp**2*Clq1*Delta_prww,st+2/3*gp**2*Clq1*Delta_wwst,pr-2/9*gp**2*(6*Cqq1*Delta_stww,pr+Cqq1*Delta_swwt,pr+3*Cqq3*Delta_swwt,pr)-2/3*gp**2*(2*Cqu1*Delta_stww,pr-Cqd1*Delta_stww,pr-CqeDelta_stww,pr)+2/9*gp**2*(2*CluDelta_prww,st-CldDelta_prww,st-CleDelta_prww,st)-gp**2*Clq1*prst+9*g**2*Clq3*prst-e.G@e.Gh@xCCurlyPhiq1*pr,st+u.G@u.Gh@xCCurlyPhil1*st,pr-d.G@d.Gh@xCCurlyPhil1*st,pr+1/4*(u.G@ce.G@cClequ1*tw,rv,pvsw-12*u.G@ce.G@cClequ3*tw,rv,pvsw+u.G@e.G@Clequ1*csw,pv,rvtw-12*u.G@e.G@Clequ3*csw,pv,rvtw)-u.G@u.G@cClusv,tw,prvw-d.G@d.G@cCldsv,tw,prvw-e.G@e.G@cCqepv,rw,stvw+1/4*(d.G@e.G@cCledqsw,rv,pvwt+e.G@d.G@cCledqcpv,tw,rvws)+GammalClq1*pv,vrst+GammaqClq1*sv,prvt+Clq1*Gammalpvst,vr+Clq1*Gammaqprsv,vt;


Beta["lq3"]=1/3*g**2*(CCurlyPhiq3*Delta_st,pr+CCurlyPhil3*Delta_pr,st)+2/3*g**2*(3*Clq3*Delta_prww,st+Clq3*Delta_wwst,pr)+2/3*g**2*(6*Cqq3*Delta_stww,pr+Cqq1*Delta_swwt,pr-Cqq3*Delta_swwt,pr)+2/3*g**2*CllDelta_pwwr,st+3*g**2*Clq1*prst-(6*g**2+gp**2)Clq3*prst-e.G@e.Gh@xCCurlyPhiq3*pr,st-u.G@u.Gh@xCCurlyPhil3*st,pr-d.G@d.Gh@xCCurlyPhil3*st,pr-1/4*(u.G@ce.G@cClequ1*tw,rv,pvsw-12*u.G@ce.G@cClequ3*tw,rv,pvsw+u.G@e.G@Clequ1*csw,pv,rvtw-12*u.G@e.G@Clequ3*csw,pv,rvtw)+1/4*(d.G@e.G@cCledqsw,rv,pvwt+e.G@d.G@cCledqcpv,tw,rvws)+GammalClq3*pv,vrst+GammaqClq3*sv,prvt+Clq3*Gammalpvst,vr+Clq3*Gammaqprsv,vt;


Beta["ee"]=-1/3*gp**2*CCurlyPhieDelta_st,pr+2/3*gp**2*(CleDelta_wwpr,st-CqeDelta_wwpr,st-2*CeuDelta_prww,st+CedDelta_prww,st+4*CeeDelta_prww,st)+e.Gh@e.G@xCCurlyPhiepr,st-e.G@e.G@cClewr,vp,vwst+GammaeCeepv,vrst+CeeGammaepvst,vr-1/3*gp**2*CCurlyPhieDelta_pr,st+2/3*gp**2*(CleDelta_wwst,pr-CqeDelta_wwst,pr-2*CeuDelta_stww,pr+CedDelta_stww,pr+4*CeeDelta_wwst,pr)+e.Gh@e.G@xCCurlyPhiest,pr-e.G@e.G@cClewt,vs,vwpr+GammaeCeesv,vtpr+CeeGammaesvpr,vt+12*gp**2*Ceeprst;


Beta["uu"]=2/9*gp**2*CCurlyPhiuDelta_st,pr-4/9*gp**2*(CeuDelta_wwst,pr+CluDelta_wwst,pr-Cqu1*Delta_wwst,pr-4*CuuDelta_wwst,pr-4/3*CuuDelta_swwt,pr)-1/9*gs**2*(Cqu8*Delta_wwst,pr-3*Cqu8*Delta_wwsr,pt)+2/3*gs**2*CuuDelta_pwwt,rs-2/9*gs**2*CuuDelta_swwt,pr-4/9*gp**2*Cud1*Delta_stww,pr-1/18*gs**2*(Cud8*Delta_stww,pr-3*Cud8*Delta_srww,pt)-u.Gh@u.G@xCCurlyPhiupr,st-(u.G@u.G@cCqu1*wr,vp,vwst-1/6*u.G@u.G@cCqu8*wr,vp,vwst)-1/2*u.G@u.G@cCqu8*wr,vs,vwpt+GammauCuupv,vrst+CuuGammaupvst,vr+2/9*gp**2*CCurlyPhiuDelta_pr,st-4/9*gp**2*(CeuDelta_wwpr,st+CluDelta_wwpr,st-Cqu1*Delta_wwpr,st-4*CuuDelta_wwpr,st-4/3*CuuDelta_pwwr,st)-1/9*gs**2*(Cqu8*Delta_wwpr,st-3*Cqu8*Delta_wwpt,sr)+2/3*gs**2*CuuDelta_swwr,tp-2/9*gs**2*CuuDelta_pwwr,st-4/9*gp**2*Cud1*Delta_prww,st-1/18*gs**2*(Cud8*Delta_prww,st-3*Cud8*Delta_ptww,sr)-u.Gh@u.G@xCCurlyPhiust,pr-(u.G@u.G@cCqu1*wt,vs,vwpr-1/6*u.G@u.G@cCqu8*wt,vs,vwpr)-1/2*u.G@u.G@cCqu8*wt,vp,vwsr+GammauCuusv,vtpr+CuuGammausvpr,vt+2*(8/3*gp**2-gs**2)Cuuprst+6*gs**2*Cuuptsr;


Beta["dd"]=-1/9*gp**2*CCurlyPhidDelta_st,pr+2/9*gp**2*(CedDelta_wwst,pr+CldDelta_wwst,pr-Cqd1*Delta_wwst,pr+2*CddDelta_wwst,pr+2/3*CddDelta_swwt,pr)-1/9*gs**2*(Cqd8*Delta_wwst,pr-3*Cqd8*Delta_wwsr,pt)+2/3*gs**2*CddDelta_pwwt,rs-2/9*gs**2*CddDelta_swwt,pr-4/9*gp**2*Cud1*Delta_wwst,pr-1/18*gs**2*(Cud8*Delta_wwst,pr-3*Cud8*Delta_wwsr,pt)+d.Gh@d.G@xCCurlyPhidpr,st-(d.G@d.G@cCqd1*wr,vp,vwst-1/6*d.G@d.G@cCqd8*wr,vp,vwst)-1/2*d.G@d.G@cCqd8*wr,vs,vwpt+GammadCddpv,vrst+CddGammadpvst,vr-1/9*gp**2*CCurlyPhidDelta_pr,st+2/9*gp**2*(CedDelta_wwpr,st+CldDelta_wwpr,st-Cqd1*Delta_wwpr,st+2*CddDelta_wwpr,st+2/3*CddDelta_pwwr,st)-1/9*gs**2*(Cqd8*Delta_wwpr,st-3*Cqd8*Delta_wwpt,sr)+2/3*gs**2*CddDelta_swwr,tp-2/9*gs**2*CddDelta_pwwr,st-4/9*gp**2*Cud1*Delta_wwpr,st-1/18*gs**2*(Cud8*Delta_wwpr,st-3*Cud8*Delta_wwpt,sr)+d.Gh@d.G@xCCurlyPhidst,pr-(d.G@d.G@cCqd1*wt,vs,vwpr-1/6*d.G@d.G@cCqd8*wt,vs,vwpr)-1/2*d.G@d.G@cCqd8*wt,vp,vwsr+GammadCddsv,vtpr+CddGammadsvpr,vt+2*(2/3*gp**2-gs**2)Cddprst+6*gs**2*Cddptsr;


Beta["eu"]=-2/3*gp**2*(CCurlyPhiuDelta_st,pr+2*(Cqu1*Delta_wwst,pr-CluDelta_wwst,pr+4*CuuDelta_wwst,pr-CeuDelta_wwst,pr-Cud1*Delta_stww,pr)+8/3*CuuDelta_swwt,pr)+4/9*gp**2*(CCurlyPhieDelta_pr,st+2*(CqeDelta_wwpr,st-CleDelta_wwpr,st-4*CeeDelta_prww,st+2*CeuDelta_prww,st-CedDelta_prww,st))-8*gp**2*Ceuprst+2*e.Gh@e.G@xCCurlyPhiupr,st-2*u.Gh@u.G@xCCurlyPhiest,pr+e.G@cu.G@cClequ1*vp,ws,vrwt-12*e.G@cu.G@cClequ3*vp,ws,vrwt+e.G@u.G@Clequ1*cvr,wt,vpws-12*e.G@u.G@Clequ3*cvr,wt,vpws-2*e.G@ce.G@Cluvp,wr,vwst-2*u.G@cu.G@Cqevs,wt,vwpr+GammaeCeupv,vrst+GammauCeusv,prvt+CeuGammaepvst,vr+CeuGammauprsv,vt;


Beta["ed"]=-2/3*gp**2*(CCurlyPhidDelta_st,pr+2*(Cqd1*Delta_wwst,pr-CldDelta_wwst,pr-2*CddDelta_wwst,pr-CedDelta_wwst,pr+2*Cud1*Delta_wwst,pr)-4/3*CddDelta_swwt,pr)-2/9*gp**2*(CCurlyPhieDelta_pr,st+2*(CqeDelta_wwpr,st-CleDelta_wwpr,st-4*CeeDelta_prww,st-CedDelta_prww,st+2*CeuDelta_prww,st))+4*gp**2*Cedprst+2*e.Gh@e.G@xCCurlyPhidpr,st+2*d.Gh@d.G@xCCurlyPhiest,pr-2*e.G@ce.G@Cldvp,wr,vwst-2*d.G@cd.G@Cqevs,wt,vwpr+e.G@cd.G@Cledqvp,wt,vrsw+e.G@d.G@cCledqcvr,ws,vptw+GammaeCedpv,vrst+GammadCedsv,prvt+CedGammaepvst,vr+CedGammadprsv,vt;


Beta["ud1"]=4/9*gp**2*(CCurlyPhidDelta_st,pr+2*(Cqd1*Delta_wwst,pr-CldDelta_wwst,pr-2*CddDelta_wwst,pr+2*Cud1*Delta_wwst,pr-CedDelta_wwst,pr)-4/3*CddDelta_swwt,pr)-2/9*gp**2*(CCurlyPhiuDelta_pr,st+2*(Cqu1*Delta_wwpr,st-CluDelta_wwpr,st+4*CuuDelta_wwpr,st-Cud1*Delta_prww,st-CeuDelta_wwpr,st)+8/3*CuuDelta_pwwr,st)-8/3*(gp**2*Cud1*prst-gs**2*Cud8*prst)-2*u.Gh@u.G@xCCurlyPhidpr,st+2*d.Gh@d.G@xCCurlyPhiust,pr+2/3*d.Gh@u.G@xCCurlyPhiudsr,pt+2/3*u.Gh@d.G@xCCurlyPhiudcpt,rs+1/3*(d.G@cu.G@cCquqd1*vs,wp,vrwt+4/3*d.G@cu.G@cCquqd8*vs,wp,vrwt+d.G@u.G@Cquqd1*cvt,wr,vpws+4/3*d.G@u.G@Cquqd8*cvt,wr,vpws)-d.G@cu.G@cCquqd1*ws,vp,vrwt-d.G@u.G@Cquqd1*cwt,vr,vpws-2*u.G@cu.G@Cqd1*vp,wr,vwst-2*d.G@cd.G@Cqu1*vs,wt,vwpr+GammauCud1*pv,vrst+GammadCud1*sv,prvt+Cud1*Gammaupvst,vr+Cud1*Gammadprsv,vt;


Beta["ud8"]=8/3*gs**2*CuuDelta_pwwr,st+8/3*gs**2*CddDelta_swwt,pr+4/3*gs**2*Cqu8*Delta_wwpr,st+4/3*gs**2*Cqd8*Delta_wwst,pr+2/3*gs**2*Cud8*Delta_prww,st+2/3*gs**2*Cud8*Delta_wwst,pr-4*(2/3*gp**2+gs**2)Cud8*prst+12*gs**2*Cud1*prst+4*d.Gh@u.G@xCCurlyPhiudsr,pt+4*u.Gh@d.G@xCCurlyPhiudcpt,rs+2*(d.G@cu.G@cCquqd1*vs,wp,vrwt-1/6*d.G@cu.G@cCquqd8*vs,wp,vrwt+d.G@u.G@Cquqd1*cvt,wr,vpws-1/6*d.G@u.G@Cquqd8*cvt,wr,vpws)-2*u.G@cu.G@Cqd8*vp,wr,vwst-2*d.G@cd.G@Cqu8*vs,wt,vwpr-(d.G@cu.G@cCquqd8*ws,vp,vrwt+d.G@u.G@Cquqd8*cwt,vr,vpws)+GammauCud8*pv,vrst+GammadCud8*sv,prvt+Cud8*Gammaupvst,vr+Cud8*Gammadprsv,vt;


Beta["le"]=-1/3*gp**2*CCurlyPhieDelta_st,pr-2/3*gp**2*CCurlyPhil1*Delta_pr,st+8/3*gp**2*CllDelta_prww,st+4/3*gp**2*CllDelta_pwwr,st-4/3*gp**2*Clq1*Delta_prww,st-2/3*gp**2*CqeDelta_wwst,pr+4/3*gp**2*CleDelta_prww,st+2/3*gp**2*CleDelta_wwst,pr-8/3*gp**2*CluDelta_prww,st+4/3*gp**2*CldDelta_prww,st-4/3*gp**2*CeuDelta_stww,pr+2/3*gp**2*CedDelta_stww,pr+8/3*gp**2*CeeDelta_wwst,pr-6*gp**2*Cleprst+e.G@cXiers,pt+e.G@Xiecpt,rs-e.G@e.Gh@xCCurlyPhiepr,st+2*e.Gh@e.G@xCCurlyPhil1*st,pr-4*e.G@e.G@cCeepv,rw,vtsw+e.G@e.G@cClepw,vs,vrwt-2*e.G@e.G@cCllwt,vs,pwvr-4*e.G@e.G@cCllwt,vs,prvw+e.G@e.G@cClevt,rw,pvsw+GammalClepv,vrst+GammaeClesv,prvt+CleGammalpvst,vr+CleGammaeprsv,vt;


Beta["lu"]=-1/3*gp**2*CCurlyPhiuDelta_st,pr+4/9*gp**2*CCurlyPhil1*Delta_pr,st-16/9*gp**2*CllDelta_prww,st-8/9*gp**2*CllDelta_pwwr,st+8/9*gp**2*Clq1*Delta_prww,st-2/3*gp**2*Cqu1*Delta_wwst,pr+16/9*gp**2*CluDelta_prww,st+2/3*gp**2*CluDelta_wwst,pr-8/9*gp**2*CldDelta_prww,st-8/9*gp**2*CleDelta_prww,st+2/3*gp**2*Cud1*Delta_stww,pr+2/3*gp**2*CeuDelta_wwst,pr-8/3*gp**2*CuuDelta_stww,pr-8/9*gp**2*CuuDelta_swwt,pr+4*gp**2*Cluprst-e.G@e.Gh@xCCurlyPhiupr,st-2*u.Gh@u.G@xCCurlyPhil1*st,pr-1/2*(e.G@cu.G@cClequ1*rv,ws,pvwt+12*e.G@cu.G@cClequ3*rv,ws,pvwt)-1/2*(e.G@u.G@Clequ1*cpv,wt,rvws+12*e.G@u.G@Clequ3*cpv,wt,rvws)-2*u.G@cu.G@Clq1*vs,wt,prvw-e.G@ce.G@Ceurw,pv,vwst+GammalClupv,vrst+GammauClusv,prvt+CluGammalpvst,vr+CluGammauprsv,vt;


Beta["ld"]=-1/3*gp**2*CCurlyPhidDelta_st,pr-2/9*gp**2*CCurlyPhil1*Delta_pr,st+8/9*gp**2*CllDelta_prww,st+4/9*gp**2*CllDelta_pwwr,st-4/9*gp**2*Clq1*Delta_prww,st-2/3*gp**2*Cqd1*Delta_wwst,pr+4/9*gp**2*CldDelta_prww,st+2/3*gp**2*CldDelta_wwst,pr-8/9*gp**2*CluDelta_prww,st+4/9*gp**2*CleDelta_prww,st-4/3*gp**2*Cud1*Delta_wwst,pr+2/3*gp**2*CedDelta_wwst,pr+4/3*gp**2*CddDelta_stww,pr+4/9*gp**2*CddDelta_swwt,pr-2*gp**2*Cldprst-e.G@e.Gh@xCCurlyPhidpr,st+2*d.Gh@d.G@xCCurlyPhil1*st,pr-1/2*e.G@cd.G@Cledqrv,wt,pvsw-1/2*e.G@d.G@cCledqcpv,ws,rvtw-2*d.G@cd.G@Clq1*vs,wt,prvw-e.G@ce.G@Cedrw,pv,vwst+GammalCldpv,vrst+GammadCldsv,prvt+CldGammalpvst,vr+CldGammadprsv,vt;


Beta["qe"]=1/9*gp**2*CCurlyPhieDelta_st,pr-2/3*gp**2*CCurlyPhiq1*Delta_pr,st-8/3*gp**2*Cqq1*Delta_prww,st-4/9*gp**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+4/3*gp**2*Clq1*Delta_wwpr,st-2/9*gp**2*CleDelta_wwst,pr+4/3*gp**2*CqeDelta_prww,st+2/9*gp**2*CqeDelta_wwst,pr-8/3*gp**2*Cqu1*Delta_prww,st+4/3*gp**2*Cqd1*Delta_prww,st+4/9*gp**2*CeuDelta_stww,pr-2/9*gp**2*CedDelta_stww,pr-8/9*gp**2*CeeDelta_wwst,pr+2*gp**2*Cqeprst+u.G@u.Gh@xCCurlyPhiepr,st-d.G@d.Gh@xCCurlyPhiepr,st+2*e.Gh@e.G@xCCurlyPhiq1*st,pr-1/2*d.G@e.G@cCledqpw,vs,vtwr-1/2*e.G@d.G@cCledqcvt,rw,vswp-2*e.G@ce.G@Clq1*vs,wt,vwpr-1/2*(u.G@ce.G@cClequ1*rw,vs,vtpw+12*u.G@ce.G@cClequ3*rw,vs,vtpw)-1/2*(u.G@e.G@Clequ1*cpw,vt,vsrw+12*u.G@e.G@Clequ3*cpw,vt,vsrw)-d.G@cd.G@Cedrw,pv,stvw-u.G@cu.G@Ceurw,pv,stvw+GammaqCqepv,vrst+GammaeCqesv,prvt+CqeGammaqpvst,vr+CqeGammaeprsv,vt;


Beta["qu1"]=1/9*gp**2*CCurlyPhiuDelta_st,pr+4/9*gp**2*CCurlyPhiq1*Delta_pr,st+16/9*gp**2*Cqq1*Delta_prww,st+8/27*gp**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)-8/9*gp**2*Clq1*Delta_wwpr,st-8/9*gp**2*CqeDelta_prww,st-8/9*gp**2*Cqd1*Delta_prww,st+16/9*gp**2*Cqu1*Delta_prww,st+2/9*gp**2*Cqu1*Delta_wwst,pr-2/9*gp**2*CluDelta_wwst,pr-2/9*gp**2*CeuDelta_wwst,pr-2/9*gp**2*Cud1*Delta_stww,pr+8/9*gp**2*CuuDelta_stww,pr+8/27*gp**2*CuuDelta_swwt,pr-4/3*gp**2*Cqu1*prst-8/3*gs**2*Cqu8*prst+1/3*u.G@cXiurs,pt+1/3*u.G@Xiucpt,rs+u.G@u.Gh@xCCurlyPhiupr,st-d.G@d.Gh@xCCurlyPhiupr,st-2*u.Gh@u.G@xCCurlyPhiq1*st,pr+1/3*(u.G@u.G@cCqu1*pw,vs,vrwt+4/3*u.G@u.G@cCqu8*pw,vs,vrwt)+1/3*(u.G@u.G@cCqu1*vt,rw,pvsw+4/3*u.G@u.G@cCqu8*vt,rw,pvsw)+1/3*(d.G@cu.G@cCquqd1*rw,vs,ptvw+4/3*d.G@cu.G@cCquqd8*rw,vs,ptvw)+1/3*(d.G@u.G@Cquqd1*cpw,vt,rsvw+4/3*d.G@u.G@Cquqd8*cpw,vt,rsvw)+1/2*d.G@cu.G@cCquqd1*rw,vs,vtpw+1/2*d.G@u.G@Cquqd1*cpw,vt,vsrw-2/3*(u.G@u.G@cCqq1*vt,ws,pvwr+3*u.G@u.G@cCqq3*vt,ws,pvwr)-4*u.G@u.G@cCqq1*wt,vs,prvw-2/3*u.G@u.G@cCuupv,rw,vtsw-2*u.G@u.G@cCuupv,rw,vwst-d.G@d.G@cCud1*pv,rw,stvw+GammaqCqu1*pv,vrst+GammauCqu1*sv,prvt+Cqu1*Gammaqpvst,vr+Cqu1*Gammauprsv,vt;


Beta["qd1"]=1/9*gp**2*CCurlyPhidDelta_st,pr-2/9*gp**2*CCurlyPhiq1*Delta_pr,st-8/9*gp**2*Cqq1*Delta_prww,st-4/27*gp**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+4/9*gp**2*Clq1*Delta_wwpr,st+4/9*gp**2*CqeDelta_prww,st-8/9*gp**2*Cqu1*Delta_prww,st+4/9*gp**2*Cqd1*Delta_prww,st+2/9*gp**2*Cqd1*Delta_wwst,pr-2/9*gp**2*CldDelta_wwst,pr-2/9*gp**2*CedDelta_wwst,pr+4/9*gp**2*Cud1*Delta_wwst,pr-4/9*gp**2*CddDelta_stww,pr-4/27*gp**2*CddDelta_swwt,pr+2/3*gp**2*Cqd1*prst-8/3*gs**2*Cqd8*prst+1/3*d.G@cXidrs,pt+1/3*d.G@Xidcpt,rs+u.G@u.Gh@xCCurlyPhidpr,st-d.G@d.Gh@xCCurlyPhidpr,st+2*d.Gh@d.G@xCCurlyPhiq1*st,pr+1/3*(d.G@d.G@cCqd1*pw,vs,vrwt+4/3*d.G@d.G@cCqd8*pw,vs,vrwt)+1/3*(d.G@d.G@cCqd1*vt,rw,pvsw+4/3*d.G@d.G@cCqd8*vt,rw,pvsw)+1/3*(u.G@cd.G@cCquqd1*rw,vs,vwpt+4/3*u.G@cd.G@cCquqd8*rw,vs,vwpt)+1/3*(u.G@d.G@Cquqd1*cpw,vt,vwrs+4/3*u.G@d.G@Cquqd8*cpw,vt,vwrs)+1/2*d.G@cu.G@cCquqd1*ws,rv,pvwt+1/2*u.G@d.G@Cquqd1*cpv,wt,rvws-2/3*(d.G@d.G@cCqq1*vt,ws,pvwr+3*d.G@d.G@cCqq3*vt,ws,pvwr)-4*d.G@d.G@cCqq1*wt,vs,prvw-2/3*d.G@d.G@cCddpv,rw,vtsw-2*d.G@d.G@cCddpv,rw,vwst-u.G@u.G@cCud1*pv,rw,vwst+GammaqCqd1*pv,vrst+GammadCqd1*sv,prvt+Cqd1*Gammaqpvst,vr+Cqd1*Gammadprsv,vt;


Beta["qu8"]=8/3*gs**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+2/3*gs**2*Cqu8*Delta_prww,st+2/3*gs**2*Cqd8*Delta_prww,st+4/3*gs**2*Cqu8*Delta_wwst,pr+2/3*gs**2*Cud8*Delta_stww,pr+8/3*gs**2*CuuDelta_swwt,pr-(4/3*gp**2+14*gs**2)Cqu8*prst-12*gs**2*Cqu1*prst+2*u.G@cXiurs,pt+2*u.G@Xiucpt,rs+2*(u.G@u.G@cCqu1*pw,vs,vrwt-1/6*u.G@u.G@cCqu8*pw,vs,vrwt)+2*(u.G@u.G@cCqu1*vt,rw,pvsw-1/6*u.G@u.G@cCqu8*vt,rw,pvsw)+2*(d.G@cu.G@cCquqd1*rw,vs,ptvw-1/6*d.G@cu.G@cCquqd8*rw,vs,ptvw)+2*(d.G@u.G@Cquqd1*cpw,vt,rsvw-1/6*d.G@u.G@Cquqd8*cpw,vt,rsvw)+1/2*u.G@cd.G@cCquqd8*vs,rw,vtpw+1/2*u.G@d.G@Cquqd8*cvt,pw,vsrw-4*(u.G@u.G@cCqq1*vt,ws,pvwr+3*u.G@u.G@cCqq3*vt,ws,pvwr)-4*u.G@u.G@cCuupv,rw,vtsw-d.G@d.G@cCud8*pv,rw,stvw+GammaqCqu8*pv,vrst+GammauCqu8*sv,prvt+Cqu8*Gammaqpvst,vr+Cqu8*Gammauprsv,vt;


Beta["qd8"]=8/3*gs**2*(Cqq1*Delta_pwwr,st+3*Cqq3*Delta_pwwr,st)+2/3*gs**2*Cqu8*Delta_prww,st+2/3*gs**2*Cqd8*Delta_prww,st+4/3*gs**2*Cqd8*Delta_wwst,pr+2/3*gs**2*Cud8*Delta_wwst,pr+8/3*gs**2*CddDelta_swwt,pr-(-2/3*gp**2+14*gs**2)Cqd8*prst-12*gs**2*Cqd1*prst+2*d.G@cXidrs,pt+2*d.G@Xidcpt,rs+2*(d.G@d.G@cCqd1*pw,vs,vrwt-1/6*d.G@d.G@cCqd8*pw,vs,vrwt)+2*(d.G@d.G@cCqd1*vt,rw,pvsw-1/6*d.G@d.G@cCqd8*vt,rw,pvsw)+2*(u.G@cd.G@cCquqd1*rw,vs,vwpt-1/6*u.G@cd.G@cCquqd8*rw,vs,vwpt)+2*(u.G@d.G@Cquqd1*cpw,vt,vwrs-1/6*u.G@d.G@Cquqd8*cpw,vt,vwrs)+1/2*d.G@cu.G@cCquqd8*vs,rw,pwvt+1/2*d.G@u.G@Cquqd8*cvt,pw,rwvs-4*(d.G@d.G@cCqq1*vt,ws,pvwr+3*d.G@d.G@cCqq3*vt,ws,pvwr)-4*d.G@d.G@cCddpv,rw,vtsw-u.G@u.G@cCud8*pv,rw,vwst+GammaqCqd8*pv,vrst+GammadCqd8*sv,prvt+Cqd8*Gammaqpvst,vr+Cqd8*Gammadprsv,vt;


Beta["ledq"]=-(8/3*gp**2+8*gs**2)Cledqprst-2*d.G@cXiets,pr-2*e.G@Xidcrp,st+2*e.G@d.G@cCedpv,tw,vrsw-2*e.G@d.G@cCldvr,tw,pvsw+2*e.G@d.G@cClq1*vr,ws,pvwt+6*e.G@d.G@cClq3*vr,ws,pvwt-2*e.G@d.G@cCqepw,vs,vtwr+2*d.G@cu.G@cClequ1*vs,tw,prvw+GammalCledqpv,vrst+GammaqCledqsv,prvt+CledqGammaepvst,vr+CledqGammadprsv,vt;


Beta["quqd1"]=10/3*gp*CdBu.G@st,pr-6*g*CdWu.G@st,pr-20/9*gp*CdBu.G@pt,sr+4*g*CdWu.G@pt,sr-64/9*gs*CdGu.G@pt,sr-2/3*gp*CuBd.G@pr,st-6*g*CuWd.G@pr,st+4/9*gp*CuBd.G@sr,pt+4*g*CuWd.G@sr,pt-64/9*gs*CuGd.G@sr,pt-1/2*(11/9*gp**2+3*g**2+32*gs**2)Cquqd1*prst-1/3*(-5/9*gp**2-3*g**2+64/3*gs**2)Cquqd1*srpt-4/9*(-5/9*gp**2-3*g**2+28/3*gs**2)Cquqd8*srpt+16/9*gs**2*Cquqd8*prst-2*u.G@Xidpr,st-2*d.G@Xiust,pr+4/3*(u.G@d.G@Cqd1*vr,pw,svwt+4/3*u.G@d.G@Cqd8*vr,pw,svwt+d.G@u.G@Cqu1*vt,sw,pvwr+4/3*d.G@u.G@Cqu8*vt,sw,pvwr+d.G@u.G@Cud1*pw,sv,vrwt+4/3*d.G@u.G@Cud8*pw,sv,vrwt)+8/3*(d.G@u.G@Cqq1*wt,vr,svpw-3*d.G@u.G@Cqq3*wt,vr,svpw-3*d.G@u.G@Cqq1*wt,vr,swpv+9*d.G@u.G@Cqq3*wt,vr,swpv)-4*d.G@u.G@Cud1*sw,pv,vrwt+GammaqCquqd1*pv,vrst+GammaqCquqd1*sv,prvt+Cquqd1*Gammaupvst,vr+Cquqd1*Gammadprsv,vt;


Beta["quqd8"]=8*gs*CdGu.G@st,pr-40/3*gp*CdBu.G@pt,sr+24*g*CdWu.G@pt,sr+16/3*gs*CdGu.G@pt,sr+8*gs*CuGd.G@pr,st+8/3*gp*CuBd.G@sr,pt+24*g*CuWd.G@sr,pt+16/3*gs*CuGd.G@sr,pt+8*gs**2*Cquqd1*prst+(10/9*gp**2+6*g**2+16/3*gs**2)Cquqd1*srpt+(-11/18*gp**2-3/2*g**2+16/3*gs**2)Cquqd8*prst-1/3*(5/9*gp**2+3*g**2+44/3*gs**2)Cquqd8*srpt+8*(u.G@d.G@Cqd1*vr,pw,svwt-1/6*u.G@d.G@Cqd8*vr,pw,svwt+d.G@u.G@Cqu1*vt,sw,pvwr-1/6*d.G@u.G@Cqu8*vt,sw,pvwr+d.G@u.G@Cud1*pw,sv,vrwt-1/6*d.G@u.G@Cud8*pw,sv,vrwt)+16*(d.G@u.G@Cqq1*wt,vr,svpw-3*d.G@u.G@Cqq3*wt,vr,svpw)-4*d.G@u.G@Cud8*sw,pv,vrwt+GammaqCquqd8*pv,vrst+GammaqCquqd8*sv,prvt+Cquqd8*Gammaupvst,vr+Cquqd8*Gammadprsv,vt;


Beta["lequ1"]=-(11/3*gp**2+8*gs**2)Clequ1*prst+(30*gp**2+18*g**2)Clequ3*prst+2*u.G@Xiest,pr+2*e.G@Xiupr,st+2*d.G@u.G@Cledqsv,wt,prvw+2*e.G@u.G@Ceupv,sw,vrwt+2*e.G@u.G@Clq1*vr,wt,pvsw-6*e.G@u.G@Clq3*vr,wt,pvsw-2*e.G@u.G@Cluvr,sw,pvwt-2*e.G@u.G@Cqepw,vt,svwr+GammalClequ1*pv,vrst+GammaqClequ1*sv,prvt+Clequ1*Gammaepvst,vr+Clequ1*Gammauprsv,vt;


Beta["lequ3"]=5/6*gp*CeBu.G@pr,st-3/2*g*CuWe.G@st,pr-3/2*gp*CuBe.G@st,pr-3/2*g*CeWu.G@pr,st+(2/9*gp**2-3*g**2+8/3*gs**2)Clequ3*prst+1/8*(5*gp**2+3*g**2)Clequ1*prst-1/2*u.G@e.G@Ceusw,pv,vrwt-1/2*e.G@u.G@Clq1*vr,wt,pvsw+3/2*e.G@u.G@Clq3*vr,wt,pvsw-1/2*e.G@u.G@Cluvr,sw,pvwt-1/2*e.G@u.G@Cqepw,vt,svwr+GammalClequ3*pv,vrst+GammaqClequ3*sv,prvt+Clequ3*Gammaepvst,vr+Clequ3*Gammauprsv,vt;


Beta["duql"]=-(9/2*g**2+11/6*gp**2+4*gs**2)Cduqlprst-d.G@cd.G@Cduqlsv,wp,vrwt-u.G@cu.G@Cduqlsv,wr,pvwt+2*e.G@cu.G@cCduuetv,sw,prwv+e.G@cu.G@cCduuetv,sw,pwrv+4*d.G@u.G@Cqqqlvp,wr,vwst+4*d.G@u.G@Cqqqlvp,wr,wvst-d.G@u.G@Cqqqlvp,wr,vswt-d.G@u.G@Cqqqlvp,wr,wsvt+2*d.G@e.G@cCqquewp,tv,wsrv+d.Gh@d.G@Cduqlvp,vrst+u.Gh@u.G@Cduqlvr,pvst+1/2*(u.G@u.Gh@Cduqlvs,prvt+d.G@d.Gh@Cduqlvs,prvt)+1/2*e.G@e.Gh@Cduqlvt,prsv;


Beta["qque"]=-(9/2*g**2+23/6*gp**2+4*gs**2)Cqqueprst-u.G@cu.G@Cqquerv,ws,pwvt+1/2*e.G@d.G@cCduqlwt,rv,vspw-1/2*(2*d.G@cu.G@cCduuepv,rw,vwst+d.G@cu.G@cCduuepv,rw,vswt)+1/2*(-2*u.G@e.G@Cqqqlws,vt,prwv+u.G@e.G@Cqqqlws,vt,pwrv-2*u.G@e.G@Cqqqlws,vt,wprv)+1/2*(u.G@u.Gh@Cqquevp,vrst+d.G@d.Gh@Cqquevp,vrst)-u.G@cu.G@Cqquepv,ws,rwvt+1/2*e.G@d.G@cCduqlwt,pv,vsrw-1/2*(2*d.G@cu.G@cCduuerv,pw,vwst+d.G@cu.G@cCduuerv,pw,vswt)+1/2*(-2*u.G@e.G@Cqqqlws,vt,rpwv+u.G@e.G@Cqqqlws,vt,rwpv-2*u.G@e.G@Cqqqlws,vt,wrpv)+1/2*(u.G@u.Gh@Cqquevr,vpst+d.G@d.Gh@Cqquevr,vpst)+u.Gh@u.G@Cqquevs,prvt+e.Gh@e.G@Cqquevt,prsv;


Beta["qqql"]=-(3*g**2+1/3*gp**2+4*gs**2)Cqqqlprst-4*g**2*(Cqqqlrpst+Cqqqlsrpt+Cqqqlpsrt)-4*e.G@cu.G@cCqquetv,sw,prwv+2*(d.G@cu.G@cCduqlpv,rw,vwst+d.G@cu.G@cCduqlrv,pw,vwst)+1/2*(u.G@u.Gh@Cqqqlvp,vrst+d.G@d.Gh@Cqqqlvp,vrst)+1/2*(u.G@u.Gh@Cqqqlvr,pvst+d.G@d.Gh@Cqqqlvr,pvst)+1/2*(u.G@u.Gh@Cqqqlvs,prvt+d.G@d.Gh@Cqqqlvs,prvt)+1/2*e.G@e.Gh@Cqqqlvt,prsv;


Beta["duue"]=-(2*gp**2+4*gs**2)Cduueprst-20/3*gp**2*Cduuepsrt+4*u.G@e.G@Cduqlws,vt,prwv-8*d.G@u.G@Cqquevp,wr,vwst+d.Gh@d.G@Cduuevp,vrst+u.Gh@u.G@Cduuevr,pvst+u.Gh@u.G@Cduuevs,prvt+e.Gh@e.G@Cduuevt,prsv;

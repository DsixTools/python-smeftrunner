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


#Formels...  #problem: meaning of c.c.   # i in eta5
Eta1=(3*np.trace(WC["uCurlyPhi"]@G_u.getH())+3*np.trace(WC["dCurlyPhi"]@G_d.getH())+np.trace(WC["eCurlyPhi"]@G_e.getH())+3*c*np.trace(WC["uCurlyPhi"]@G_u.getH())+3*c*np.trace(WC["dCurlyPhi"]@G_d.getH())+c*np.trace(WC["eCurlyPhi"]@G_e.getH()))/2
Eta2=-6*np.trace(WC["CurlyPhiq3"]@G_u@G_u.getH())-6*np.trace(WC["CurlyPhiq3"]@G_d@G_d.getH())-2*np.trace(WC["CurlyPhil3"]@G_e@G_e.getH())+3*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+c*np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u))
Eta3=3*np.trace(WC["CurlyPhiq1"]@G_d@G_d.getH())-3*np.trace(WC["CurlyPhiq1"]@G_u@G_u.getH())+9*np.trace(WC["CurlyPhiq3"]@G_d@G_d.getH())+9*np.trace(WC["CurlyPhiq3"]@G_u@G_u.getH())+3*np.trace(WC["CurlyPhiu"]@G_u.getH()@G_u)-3*np.trace(WC["CurlyPhid"]@G_d.getH()@G_d)-3*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+c*np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u))+np.trace(WC["CurlyPhil1"]@G_e@G_e.getH())+3*np.trace(WC["CurlyPhil3"]@G_e@G_e.getH())-np.trace(WC["CurlyPhie"]@G_e.getH()@G_e)
Eta4=12*np.trace(WC["CurlyPhiq1"]@G_d@G_d.getH())-12*np.trace(WC["CurlyPhiq1"]@G_u@G_u.getH())+12*np.trace(WC["CurlyPhiu"]@G_u.getH()@G_u)-12*np.trace(WC["CurlyPhid"]@G_d.getH()@G_d)+6*(np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u)+c*np.trace(WC["CurlyPhiud"]@G_d.getH()@G_u))+4*np.trace(WC["CurlyPhil1"]@G_e@G_e.getH())-4*np.trace(WC["CurlyPhie"]@G_e.getH()@G_e)
Eta5=j*3/2*(np.trace(G_d@WC["dCurlyPhi"].getH())-c*np.trace(G_d@WC["dCurlyPhi"].getH()))-j*3/2*(np.trace(G_u@WC["uCurlyPhi"].getH())-c*np.trace(G_u@WC["uCurlyPhi"].getH()))+j*1/2*(np.trace(G_e@WC["eCurlyPhi"].getH())-c*np.trace(G_e@WC["eCurlyPhi"].getH()))

GammaH=np.trace(3*G_u@G_u.getH()+3*G_d@G_d.getH()+G_e@G_e.getH())
Gammaq=1/2*(G_u@G_u.getH()+G_d@G_d.getH())
Gammau=G_u.getH()@G_u
Gammad=G_d.getH()@G_d
Gammal=1/2*G_e@G_e.getH()
Gammae=G_e.getH()@G_e

XiB=2/3*(WC["CurlyPhiEmptySquare"]+WC["CurlyPhiD"])+8/3*(-np.trace(WC["CurlyPhil1"])+np.trace(WC["CurlyPhiq1"])-np.trace(WC["CurlyPhie"])+2*np.trace(WC["CurlyPhiu"])-np.trace(WC["CurlyPhid"]))




#Beta function, WC as 2 dictionaries
Beta = {}
WC = {}

#beta functions
Beta["g"]=-19/6*g**3-8*g*m**2/HIGHSCALE**2*WC["CurlyPhiW"]


Beta["gp"]=41/6*gp**3-8*gp*m**2/HIGHSCALE**2*WC["CurlyPhiB"]


Beta["gs"]=-7*gs**3-8*gs*m**2/HIGHSCALE**2*WC["CurlyPhiG"]


Beta["Lambda"]=12*Lambda**2+3/4*gp**4+3/2*g**2*gp**2+9/4*g**4-3*(gp**2+3*g**2)*Lambda+4*Lambda*GammaH-4*(3*np.trace(G_d@G_d.getH()@G_d@G_d.getH()@)+3*np.trace(G_u@G_u.getH()@G_u@G_u.getH()@)+np.trace(G_e@G_e.getH()@G_e@G_e.getH()@))+4*m**2/HIGHSCALE**2*(12*WC["CurlyPhi"]+(-16*Lambda+10/3*g**2)*WC["CurlyPhiEmptySquare"]+(6*Lambda+3/2*(gp**2-g**2))*WC["CurlyPhiD"]+2*(Eta1+Eta2)+9*g**2*WC["CurlyPhiW"]+3*gp**2*WC["CurlyPhiB"]+3*g*gp*WC["CurlyPhiWB"]+4/3*g**2*(np.trace(WC["CurlyPhil3"])+3*np.trace(WC["CurlyPhiq3"])))


Beta["m**2"]=m**2*(6*Lambda-9/2*g**2-3/2*gp**2+2*GammaH+4*m**2/HIGHSCALE**2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"]))


#progress now
Beta["G_u@X"]=3/2*(G_u@G_u.getH()@G_u@-G_d@G_d.getH()@G_u@)+(GammaH-9/4*g**2-17/12*gp**2-8*gs**2)*G_u@
+2*m**2/HIGHSCALE**2*(3*WC["uCurlyPhi"]+1/2*(WC["CurlyPhiD"]-2*WC["CurlyPhiEmptySquare"])*G_u@-CCurlyPhiq1*hG_u@+3*CCurlyPhiq3*hG_u@
+G_u@CCurlyPhiuh-G_d@CCurlyPhiudh-2*(Cqu1*G_u@rpts,pt+4/3*Cqu8*G_u@rpts,pt)-Clequ1*G_e@cptrs,pt
+3*Cquqd1*G_d@crspt,pt+1/2*(Cquqd1*G_d@cpsrt,pt+4/3*Cquqd8*G_d@cpsrt,pt));


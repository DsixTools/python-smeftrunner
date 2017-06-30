# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:38:21 2017

@author: Xuanyou
"""

import numpy as np


#I want to write a class particle containing all the information of the particle

class particle:
    def __init__(self, name):
        self.name = name
        self.G = []
        self.Gh=self.G.getH()    #maybe problematic
        self.WCs = []
        
    def add_G(self,G):
        self.G.append(G)
        
    def add_WC(self,WC):
        self.WC.append(WC)





# data input       
u=particle('u')
d=particle('d')
e=particle('e')

u.add_G(np.matrix())  
d.add_G(np.matrix())
e.add_G(np.matrix())
        





#Parameters, formels...
GammaH=np.trace(3*u.G@u.Gh+3*d.G@d.Gh+e.G@e.Gh)
# and define the constant g, m, HIGHSCALE,...






#write Beta function in a dictionary
Beta = {}

Beta["g"]=-19/6*g**3-8*g*m**2/HIGHSCALE**2*WC["CurlyPhiW"];

Beta["gp"]=41/6*gp**3-8*gp*m**2/HIGHSCALE**2*WC["CurlyPhiB"];

Beta["gs"]=-7*gs**3-8*gs*m**2/HIGHSCALE**2*WC["CurlyPhiG"];

#......
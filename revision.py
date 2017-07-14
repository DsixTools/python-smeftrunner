# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

#f = open("beta.txt","r")
#f_py = open("beta_py.py", "w")

f = open("Parameter.txt","r")
f_py = open("Parameter.py", "w")

f_py.write("#this file was formed from 'revision.py'\n\n\n")

line = f.readline()
while line:
    line = line.replace('\[','')
    line = line.replace('][','_')
    line = line.replace('^','**')
    line = line.replace(']','')
    line = line.replace('[','')
    line = line.replace('m2','m**2')
    line = re.sub(r'([a-zA-Z]) ([a-zA-Z])', r'\1*\2', line)
    line = re.sub(r'([\d\)])\s*([a-zA-Z\(])', r'\1*\2', line)     #for *
    line = re.sub(r'_([a-zA-Z\*\d]+)=', r'["\1"]=', line)         #for index from beta
    line = re.sub(r'(WC)([a-zA-Z]+)', r'\1["\2"]', line)      #for index from wc
    line = re.sub(r'(G)([ude])([h]?)', r'\1_\2\3@', line)     #expression of G (big Gamma)
    line = re.sub(r'(G_[ude])[h]', r'\1.getH()', line)        #Conjugate transpose of G (dagger)
    line = re.sub(r'TrC(\w+)',r'np.trace(WC["\1"])', line)    #trace from WC
    line = re.sub(r'Tr((\w+_\w+(.getH\(\))?@)+)', r'np.trace(\1)', line)    #trace function
    line = re.sub(r'C([a-zA-Z]+\d?)\*?h([G\+\-])', r'WC["\1"].getH()@\2', line)      #conjugate transpose of WC (dagger)
    line = re.sub(r'(G_[ued])@c', r'np.conj(\1)@', line)                             #conjugate of G (*)
    line = re.sub(r'C([a-zA-Z]+\d?)\*?((np.conj\()?G_[ued]\)?)@([rpts]{4}),([rpts]{2})', r'np.einsum("\4,\5", WC["\1"], \2)', line)   #einsum function
    line = re.sub(r'(WC\["[a-zA-Z0-9]+)c"\]', r'np.conj(\1"])', line)                #conjugate of WC (*)
    
    line = re.sub(r'@([)|\+|\-|;])', r'\1', line)               #remove the odd @ 
    line = re.sub(r'\)\*(G_[ude])', r')@\1', line)             #odd * in matrix multiplication    
    line = line.replace(';', '')
    
    
    f_py.write(line)
    line=f.readline()

f.close()
f_py.close()
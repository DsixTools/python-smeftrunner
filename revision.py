# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

f = open("beta.txt","r")
f_py = open("beta_py.py", "w")

#f = open("flavor.m","r")
#f_py = open("flavor.py", "w")

f_py.write("#this file was formed from 'revision.py'\n\n\n")

line = f.readline()
while line:
    line=line.replace('\[','')
    line=line.replace('][','_')
    line=line.replace('^','**')
    line=line.replace(']','')
    line=line.replace('[','')
    line=line.replace('m2','m**2')
    line=re.sub(r'([a-zA-Z]) ([a-zA-Z])', r'\1*\2', line)
    line=re.sub(r'(\d)\s*([a-zA-Z\(])', r'\1*\2', line)     #for *
    line=re.sub(r'_([a-zA-Z\*\d]+)=', r'["\1"]=', line)         #for index from beta
    line=re.sub(r'(WC)([a-zA-Z]+)', r'\1["\2"]', line)      #for index from wc
    line=re.sub(r'(G)([ude])([h]?)', r'\2.\1\3@', line)     #expression of G (big Gamma)
    line=re.sub(r'Tr((\w+.\w+@)+)', r'np.trace(\1)', line)    #trace function 
    line=re.sub(r'@([)|\+|-])', r'\1', line)               #remove the odd @ 
        
    f_py.write(line)
    line=f.readline()

f.close()
f_py.close()
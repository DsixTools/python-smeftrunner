# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

f = open("beta.txt","r")
f_py = open("beta_py.py", "w")

#f = open("Parameter.txt","r")
#f_py = open("Parameter.py", "w")

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
    line = re.sub(r'C([a-zA-Z]+\d?)\*?((np.conj\()?G_[ued]\)?)@([rpts]{4}),([rpts]{2})', r'np.einsum("\4,\5", WC["\1"], \2)', line)   #einsum function for G
    line = re.sub(r'(WC\["[a-zA-Z0-9]+)c"\]', r'np.conj(\1"])', line)                #conjugate of WC (*)
    line = re.sub(r'C([a-zA-Z0-9]+)\*?c', r'np.conj(WC["\1"])', line)                #conjugate of WC (*)
    line = re.sub(r'WC\["([a-zA-Z0-9]+)(G_[ued])"\]\).getH\(\)(@G_[ued])?(@G_[ued].getH\(\))?', r'WC["\1"]@\2.getH()\3\4)', line)  #fix the odd expression
    line = re.sub(r'([\+|\-])([0-9]\*)?c([a-zA-Z0-9_@"\[\].\(\)]+)([\+|\-])', r'\1\2np.conj(\3)\4', line)  #deal with c.c. (odd number terms)
    line = re.sub(r'([\+|\-])([0-9]\*)?c([a-zA-Z0-9_@"\[\].\(\)]+)([\+|\-])', r'\1\2np.conj(\3)\4', line)  #deal with c.c. (even number terms)
    line = re.sub(r'C([a-zA-Z0-9]+)\*?(G_[eud](.getH\(\))?)@(G_[eud](.getH\(\))?)@([rpts]{4}),([rpts]{2})', r'np.einsum("\6,\7", WC["\1"], \2@\4)', line)    #einsum function for G@G
    line = re.sub(r'C([a-zA-Z0-9]+)\*?(G_[eud](.getH\(\))?)@(G_[eud](.getH\(\))?)@(G_[eud](.getH\(\))?)@([rptswv]{4}),([rptswv]{2})', r'np.einsum("\8,\9", WC["\1"], \2@\4@\6)', line)   #einsum function for G@G@G
    line = re.sub(r'C([a-zA-Z0-9]+)\*?(G_[ued])', r'WC["\1"]@\2', line)   #WC@G
    line = re.sub(r'@C([a-zA-Z0-9]+)([\+\-\)])', r'@WC["\1"]\2', line)    #G@WC
    line = re.sub(r'(Gamma[qudle])C([a-zA-Z0-9]+)([\+\-\)])', r'\1@WC["\2"]\3', line)   #Gamma@WC
    line = re.sub(r'C([a-zA-Z0-9]+)(Gamma[qudle])', r'WC["\1"]@\2', line)         #WC@GGamma
    line = re.sub(r'C([a-zA-Z0-9]+)\*?([rstp]{4})', r'np.einsum("\2", WC["\1"])', line)   #einsum for WC
    line = re.sub(r'C([a-zA-Z0-9]+)\*?Delta_([stprwv]{2},[prstwv]{2})', r'np.einsum("\2", WC["\1"], I3)', line)    #2DWC*kronecker delta
    line = re.sub(r'C([a-zA-Z0-9]+)\*?Delta_([stprwv]{4},[prwvst]{2})', r'np.einsum("\2", WC["\1"], I3)', line)     #2DWC*kronecker delta
    # for 4D WCs
    line = re.sub(r'(G_[eud](.getH\(\))?@G_[eud](.getH\(\))?)@xC([a-zA-Z0-9]+)\*?([prstwv]{2},[prstwv]{2})', r'np.einsum("\5", \1, WC["\4"])', line)  #einsum
    line = re.sub(r'(G_[eud](.getH\(\))?@G_[eud](.getH\(\))?)@xC([a-zA-Z0-9]+)\*?([prstwv]{4},[prstwv]{2})', r'np.einsum("\5", \1, WC["\4"])', line) 
    line = re.sub(r'(G_[eud](.getH\(\))?@G_[eud](.getH\(\))?)@x(np.conj\(WC["[a-zA-Z0-9]+"]\))([prstwv]{2},[prstwv]{2})', r'np.einsum("\5", \1, \4)', line)
    line = re.sub(r'((np.conj\()?G_[ued]\)?)@((np.conj\()?G_[ued]\)?)@C([a-zA-Z0-9]+)\*?([prstwv]{2},[prstwv]{2},[prstwv]{4})', r'np.einsum("\6", \1, \3, WC["\5"])', line)
    line = re.sub(r'((np.conj\()?G_[ued]\)?)@((np.conj\()?G_[ued]\)?)@(np.conj\(WC\["[a-zA-Z0-9]+"\]\))([prstwv]{2},[prstwv]{2},[prstwv]{4})', r'np.einsum("\6", \1, \3, \5)', line)
    line = re.sub(r'(Gamma[qudle])C([a-zA-Z0-9]+)\*?([prstwv]{2},[prstwv]{4})', r'np.einsum("\3", \1, WC["\2"])', line)
    line = re.sub(r'(WC\["[a-zA-Z0-9]+"\])@(Gamma[qudle])([prstwv]{4},[prstwv]{2})', r'np.einsum("\3", \1, \2)', line)
    line = re.sub(r'C([a-zA-Z0-9]+)\*?(Gamma[qudle])([prstwv]{4},[prstwv]{2})', r'np.einsum("\3", WC["\1"], \2)', line)
    line = re.sub(r'((np.conj\()?G_[due]\)?)@(Xi[edu])([prstwv]{2},[prstwv]{2})', r'np.einsum("\4", \1, \3)', line)
    line = re.sub(r'((np.conj\()?G_[due]\)?)@(Xi[edu])c([prstwv]{2},[prstwv]{2})', r'np.einsum("\4", \1, np.conj(\3))', line)
    line = re.sub(r'(WC\["[a-zA-Z0-9]+"\])@(G_[ued])@([prstwv]{2},[prstwv]{2})', r'np.einsum("\3", \1, \2)', line)
    line = re.sub(r'(G_[deu](.getH\(\))?@G_[deu](.getH\(\))?)@C([a-zA-Z0-9]+)\*?([prstwv]{2},[prstwv]{4})', r'np.einsum("\5", \1, WC["\4"])', line)
    
    
    line = re.sub(r'@([)|\+|\-|;])', r'\1', line)               #remove the odd @ 
    line = re.sub(r'\)\*(G_[ude])', r')@\1', line)             #odd * in matrix multiplication    
    line = line.replace(';', '')
    
    
    f_py.write(line)
    line=f.readline()

f.close()
f_py.close()
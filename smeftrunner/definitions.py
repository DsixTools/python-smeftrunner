"""Definitions of auxiliary objects and operator properties."""

import numpy as np

I3 = np.identity(3)

# names of SM parameters
SM_keys = ['g', 'gp', 'gs', 'Lambda', 'm2', 'Gu', 'Gd', 'Ge', 'Theta', 'Thetap', 'Thetas']

# names of WCs with 0, 2, or 4 fermions (i.e. scalars, 3x3 matrices, and 3x3x3x3 tensors)
WC_keys_0f = ["G", "Gtilde", "W", "Wtilde", "phi", "phiBox", "phiD", "phiG", "phiB", "phiW", "phiWB", "phiGtilde", "phiBtilde", "phiWtilde", "phiWtildeB"]
WC_keys_2f = ["uphi", "dphi", "ephi", "eW", "eB", "uG", "uW", "uB", "dG", "dW", "dB", "phil1", "phil3", "phie", "phiq1", "phiq3", "phiu", "phid", "phiud", "llphiphi"]
WC_keys_4f = ["ll", "qq1", "qq3", "lq1", "lq3", "ee", "uu", "dd", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1", "qd1", "qu8", "qd8", "ledq", "quqd1", "quqd8", "lequ1", "lequ3", "duql", "qque", "qqql", "duue"]

C_keys = SM_keys + WC_keys_0f + WC_keys_2f + WC_keys_4f

C_keys_shape = {
   'g': 1,
   'gp': 1,
   'gs': 1,
   'Lambda': 1,
   'm2': 1,
   'Gu': (3, 3),
   'Gd': (3, 3),
   'Ge': (3, 3),
   'Theta': 1,
   'Thetap': 1,
   'Thetas': 1,
   'G': 1,
   'Gtilde': 1,
   'W': 1,
   'Wtilde': 1,
   'phi': 1,
   'phiBox': 1,
   'phiD': 1,
   'phiG': 1,
   'phiB': 1,
   'phiW': 1,
   'phiWB': 1,
   'phiGtilde': 1,
   'phiBtilde': 1,
   'phiWtilde': 1,
   'phiWtildeB': 1,
   'uphi': (3,3),
   'dphi': (3,3),
   'ephi': (3,3),
   'eW': (3,3),
   'eB': (3,3),
   'uG': (3,3),
   'uW': (3,3),
   'uB': (3,3),
   'dG': (3,3),
   'dW': (3,3),
   'dB': (3,3),
   'phil1': (3,3),
   'phil3': (3,3),
   'phie': (3,3),
   'phiq1': (3,3),
   'phiq3': (3,3),
   'phiu': (3,3),
   'phid': (3,3),
   'phiud': (3,3),
   'llphiphi': (3,3),
   'll': (3,3,3,3),
   'qq1': (3,3,3,3),
   'qq3': (3,3,3,3),
   'lq1': (3,3,3,3),
   'lq3': (3,3,3,3),
   'ee': (3,3,3,3),
   'uu': (3,3,3,3),
   'dd': (3,3,3,3),
   'eu': (3,3,3,3),
   'ed': (3,3,3,3),
   'ud1': (3,3,3,3),
   'ud8': (3,3,3,3),
   'le': (3,3,3,3),
   'lu': (3,3,3,3),
   'ld': (3,3,3,3),
   'qe': (3,3,3,3),
   'qu1': (3,3,3,3),
   'qd1': (3,3,3,3),
   'qu8': (3,3,3,3),
   'qd8': (3,3,3,3),
   'ledq': (3,3,3,3),
   'quqd1': (3,3,3,3),
   'quqd8': (3,3,3,3),
   'lequ1': (3,3,3,3),
   'lequ3': (3,3,3,3),
   'duql': (3,3,3,3),
   'qque': (3,3,3,3),
   'qqql': (3,3,3,3),
   'duue': (3,3,3,3),
}

# names of Wilson coefficients with the same fermionic symmetry properties
C_symm_keys={}
# 0 0F scalar object
C_symm_keys[0] = WC_keys_0f + ['g', 'gp', 'gs', 'Lambda', 'm2', 'Theta', 'Thetap', 'Thetas']
# 1 2F general 3x3 matrix
C_symm_keys[1] = ["uphi", "dphi", "ephi", "eW", "eB", "uG", "uW", "uB", "dG", "dW", "dB", "phiud", 'Gu', 'Gd', 'Ge']
# 2 2F Hermitian matrix
C_symm_keys[2] = ["phil1", "phil3", "phie", "phiq1", "phiq3", "phiu", "phid",]
# 3 4F general 3x3x3x3 object
C_symm_keys[3] = ["ledq", "quqd1", "quqd8", "lequ1", "lequ3", "duql", "duue"]
# 4 4F two identical ffbar currents
C_symm_keys[4] = ["ll", "qq1", "qq3", "uu", "dd",]
# 5 4F two independent ffbar currents
C_symm_keys[5] = ["lq1", "lq3", "eu", "ed", "ud1", "ud8", "le", "lu", "ld", "qe", "qu1", "qd1", "qu8", "qd8",]
# 6 4F two identical ffbar currents - special case Cee
C_symm_keys[6] = ["ee",]
# 7 4F Baryon-number-violating - special case Cqque
C_symm_keys[7] = ["qque",]
# 8 4F Baryon-number-violating - special case Cqqql
C_symm_keys[8] = ["qqql",]
# 9 2F symmetric matrix
C_symm_keys[9] = ["llphiphi"]


def symmetrize_2(b):
    a = np.array(b, copy=True, dtype=complex)
    a[1,0]=a[0,1].conj()
    a[2,0]=a[0,2].conj()
    a[2,1]=a[1,2].conj()
    a.imag[0,0]=0
    a.imag[1,1]=0
    a.imag[2,2]=0
    return a

def symmetrize_4(b):
    a = np.array(b, copy=True, dtype=complex)
    a.real[0,0,1,0]=a.real[0,0,0,1]
    a.real[0,0,2,0]=a.real[0,0,0,2]
    a.real[0,0,2,1]=a.real[0,0,1,2]
    a.real[0,1,0,0]=a.real[0,0,0,1]
    a.real[0,2,0,0]=a.real[0,0,0,2]
    a.real[0,2,0,1]=a.real[0,1,0,2]
    a.real[0,2,1,0]=a.real[0,1,2,0]
    a.real[1,0,0,0]=a.real[0,0,0,1]
    a.real[1,0,0,1]=a.real[0,1,1,0]
    a.real[1,0,0,2]=a.real[0,1,2,0]
    a.real[1,0,1,0]=a.real[0,1,0,1]
    a.real[1,0,1,1]=a.real[0,1,1,1]
    a.real[1,0,1,2]=a.real[0,1,2,1]
    a.real[1,0,2,0]=a.real[0,1,0,2]
    a.real[1,0,2,1]=a.real[0,1,1,2]
    a.real[1,0,2,2]=a.real[0,1,2,2]
    a.real[1,1,0,0]=a.real[0,0,1,1]
    a.real[1,1,0,1]=a.real[0,1,1,1]
    a.real[1,1,0,2]=a.real[0,2,1,1]
    a.real[1,1,1,0]=a.real[0,1,1,1]
    a.real[1,1,2,0]=a.real[0,2,1,1]
    a.real[1,1,2,1]=a.real[1,1,1,2]
    a.real[1,2,0,0]=a.real[0,0,1,2]
    a.real[1,2,0,1]=a.real[0,1,1,2]
    a.real[1,2,0,2]=a.real[0,2,1,2]
    a.real[1,2,1,0]=a.real[0,1,2,1]
    a.real[1,2,1,1]=a.real[1,1,1,2]
    a.real[1,2,2,0]=a.real[0,2,2,1]
    a.real[2,0,0,0]=a.real[0,0,0,2]
    a.real[2,0,0,1]=a.real[0,1,2,0]
    a.real[2,0,0,2]=a.real[0,2,2,0]
    a.real[2,0,1,0]=a.real[0,1,0,2]
    a.real[2,0,1,1]=a.real[0,2,1,1]
    a.real[2,0,1,2]=a.real[0,2,2,1]
    a.real[2,0,2,0]=a.real[0,2,0,2]
    a.real[2,0,2,1]=a.real[0,2,1,2]
    a.real[2,0,2,2]=a.real[0,2,2,2]
    a.real[2,1,0,0]=a.real[0,0,1,2]
    a.real[2,1,0,1]=a.real[0,1,2,1]
    a.real[2,1,0,2]=a.real[0,2,2,1]
    a.real[2,1,1,0]=a.real[0,1,1,2]
    a.real[2,1,1,1]=a.real[1,1,1,2]
    a.real[2,1,1,2]=a.real[1,2,2,1]
    a.real[2,1,2,0]=a.real[0,2,1,2]
    a.real[2,1,2,1]=a.real[1,2,1,2]
    a.real[2,1,2,2]=a.real[1,2,2,2]
    a.real[2,2,0,0]=a.real[0,0,2,2]
    a.real[2,2,0,1]=a.real[0,1,2,2]
    a.real[2,2,0,2]=a.real[0,2,2,2]
    a.real[2,2,1,0]=a.real[0,1,2,2]
    a.real[2,2,1,1]=a.real[1,1,2,2]
    a.real[2,2,1,2]=a.real[1,2,2,2]
    a.real[2,2,2,0]=a.real[0,2,2,2]
    a.real[2,2,2,1]=a.real[1,2,2,2]
    a.imag[0,0,0,0]=0
    a.imag[0,0,1,0]=-a.imag[0,0,0,1]
    a.imag[0,0,1,1]=0
    a.imag[0,0,2,0]=-a.imag[0,0,0,2]
    a.imag[0,0,2,1]=-a.imag[0,0,1,2]
    a.imag[0,0,2,2]=0
    a.imag[0,1,0,0]=a.imag[0,0,0,1]
    a.imag[0,1,1,0]=0
    a.imag[0,2,0,0]=a.imag[0,0,0,2]
    a.imag[0,2,0,1]=a.imag[0,1,0,2]
    a.imag[0,2,1,0]=-a.imag[0,1,2,0]
    a.imag[0,2,2,0]=0
    a.imag[1,0,0,0]=-a.imag[0,0,0,1]
    a.imag[1,0,0,1]=0
    a.imag[1,0,0,2]=-a.imag[0,1,2,0]
    a.imag[1,0,1,0]=-a.imag[0,1,0,1]
    a.imag[1,0,1,1]=-a.imag[0,1,1,1]
    a.imag[1,0,1,2]=-a.imag[0,1,2,1]
    a.imag[1,0,2,0]=-a.imag[0,1,0,2]
    a.imag[1,0,2,1]=-a.imag[0,1,1,2]
    a.imag[1,0,2,2]=-a.imag[0,1,2,2]
    a.imag[1,1,0,0]=0
    a.imag[1,1,0,1]=a.imag[0,1,1,1]
    a.imag[1,1,0,2]=a.imag[0,2,1,1]
    a.imag[1,1,1,0]=-a.imag[0,1,1,1]
    a.imag[1,1,1,1]=0
    a.imag[1,1,2,0]=-a.imag[0,2,1,1]
    a.imag[1,1,2,1]=-a.imag[1,1,1,2]
    a.imag[1,1,2,2]=0
    a.imag[1,2,0,0]=a.imag[0,0,1,2]
    a.imag[1,2,0,1]=a.imag[0,1,1,2]
    a.imag[1,2,0,2]=a.imag[0,2,1,2]
    a.imag[1,2,1,0]=-a.imag[0,1,2,1]
    a.imag[1,2,1,1]=a.imag[1,1,1,2]
    a.imag[1,2,2,0]=-a.imag[0,2,2,1]
    a.imag[1,2,2,1]=0
    a.imag[2,0,0,0]=-a.imag[0,0,0,2]
    a.imag[2,0,0,1]=a.imag[0,1,2,0]
    a.imag[2,0,0,2]=0
    a.imag[2,0,1,0]=-a.imag[0,1,0,2]
    a.imag[2,0,1,1]=-a.imag[0,2,1,1]
    a.imag[2,0,1,2]=-a.imag[0,2,2,1]
    a.imag[2,0,2,0]=-a.imag[0,2,0,2]
    a.imag[2,0,2,1]=-a.imag[0,2,1,2]
    a.imag[2,0,2,2]=-a.imag[0,2,2,2]
    a.imag[2,1,0,0]=-a.imag[0,0,1,2]
    a.imag[2,1,0,1]=a.imag[0,1,2,1]
    a.imag[2,1,0,2]=a.imag[0,2,2,1]
    a.imag[2,1,1,0]=-a.imag[0,1,1,2]
    a.imag[2,1,1,1]=-a.imag[1,1,1,2]
    a.imag[2,1,1,2]=0
    a.imag[2,1,2,0]=-a.imag[0,2,1,2]
    a.imag[2,1,2,1]=-a.imag[1,2,1,2]
    a.imag[2,1,2,2]=-a.imag[1,2,2,2]
    a.imag[2,2,0,0]=0
    a.imag[2,2,0,1]=a.imag[0,1,2,2]
    a.imag[2,2,0,2]=a.imag[0,2,2,2]
    a.imag[2,2,1,0]=-a.imag[0,1,2,2]
    a.imag[2,2,1,1]=0
    a.imag[2,2,1,2]=a.imag[1,2,2,2]
    a.imag[2,2,2,0]=-a.imag[0,2,2,2]
    a.imag[2,2,2,1]=-a.imag[1,2,2,2]
    a.imag[2,2,2,2]=0
    return a

def symmetrize_5(b):
    a = np.array(b, copy=True, dtype=complex)
    a.real[0,0,1,0]=a.real[0,0,0,1]
    a.real[0,0,2,0]=a.real[0,0,0,2]
    a.real[0,0,2,1]=a.real[0,0,1,2]
    a.real[1,0,0,0]=a.real[0,1,0,0]
    a.real[1,0,0,1]=a.real[0,1,1,0]
    a.real[1,0,0,2]=a.real[0,1,2,0]
    a.real[1,0,1,0]=a.real[0,1,0,1]
    a.real[1,0,1,1]=a.real[0,1,1,1]
    a.real[1,0,1,2]=a.real[0,1,2,1]
    a.real[1,0,2,0]=a.real[0,1,0,2]
    a.real[1,0,2,1]=a.real[0,1,1,2]
    a.real[1,0,2,2]=a.real[0,1,2,2]
    a.real[1,1,1,0]=a.real[1,1,0,1]
    a.real[1,1,2,0]=a.real[1,1,0,2]
    a.real[1,1,2,1]=a.real[1,1,1,2]
    a.real[2,0,0,0]=a.real[0,2,0,0]
    a.real[2,0,0,1]=a.real[0,2,1,0]
    a.real[2,0,0,2]=a.real[0,2,2,0]
    a.real[2,0,1,0]=a.real[0,2,0,1]
    a.real[2,0,1,1]=a.real[0,2,1,1]
    a.real[2,0,1,2]=a.real[0,2,2,1]
    a.real[2,0,2,0]=a.real[0,2,0,2]
    a.real[2,0,2,1]=a.real[0,2,1,2]
    a.real[2,0,2,2]=a.real[0,2,2,2]
    a.real[2,1,0,0]=a.real[1,2,0,0]
    a.real[2,1,0,1]=a.real[1,2,1,0]
    a.real[2,1,0,2]=a.real[1,2,2,0]
    a.real[2,1,1,0]=a.real[1,2,0,1]
    a.real[2,1,1,1]=a.real[1,2,1,1]
    a.real[2,1,1,2]=a.real[1,2,2,1]
    a.real[2,1,2,0]=a.real[1,2,0,2]
    a.real[2,1,2,1]=a.real[1,2,1,2]
    a.real[2,1,2,2]=a.real[1,2,2,2]
    a.real[2,2,1,0]=a.real[2,2,0,1]
    a.real[2,2,2,0]=a.real[2,2,0,2]
    a.real[2,2,2,1]=a.real[2,2,1,2]
    a.imag[0,0,0,0]=0
    a.imag[0,0,1,0]=-a.imag[0,0,0,1]
    a.imag[0,0,1,1]=0
    a.imag[0,0,2,0]=-a.imag[0,0,0,2]
    a.imag[0,0,2,1]=-a.imag[0,0,1,2]
    a.imag[0,0,2,2]=0
    a.imag[1,0,0,0]=-a.imag[0,1,0,0]
    a.imag[1,0,0,1]=-a.imag[0,1,1,0]
    a.imag[1,0,0,2]=-a.imag[0,1,2,0]
    a.imag[1,0,1,0]=-a.imag[0,1,0,1]
    a.imag[1,0,1,1]=-a.imag[0,1,1,1]
    a.imag[1,0,1,2]=-a.imag[0,1,2,1]
    a.imag[1,0,2,0]=-a.imag[0,1,0,2]
    a.imag[1,0,2,1]=-a.imag[0,1,1,2]
    a.imag[1,0,2,2]=-a.imag[0,1,2,2]
    a.imag[1,1,0,0]=0
    a.imag[1,1,1,0]=-a.imag[1,1,0,1]
    a.imag[1,1,1,1]=0
    a.imag[1,1,2,0]=-a.imag[1,1,0,2]
    a.imag[1,1,2,1]=-a.imag[1,1,1,2]
    a.imag[1,1,2,2]=0
    a.imag[2,0,0,0]=-a.imag[0,2,0,0]
    a.imag[2,0,0,1]=-a.imag[0,2,1,0]
    a.imag[2,0,0,2]=-a.imag[0,2,2,0]
    a.imag[2,0,1,0]=-a.imag[0,2,0,1]
    a.imag[2,0,1,1]=-a.imag[0,2,1,1]
    a.imag[2,0,1,2]=-a.imag[0,2,2,1]
    a.imag[2,0,2,0]=-a.imag[0,2,0,2]
    a.imag[2,0,2,1]=-a.imag[0,2,1,2]
    a.imag[2,0,2,2]=-a.imag[0,2,2,2]
    a.imag[2,1,0,0]=-a.imag[1,2,0,0]
    a.imag[2,1,0,1]=-a.imag[1,2,1,0]
    a.imag[2,1,0,2]=-a.imag[1,2,2,0]
    a.imag[2,1,1,0]=-a.imag[1,2,0,1]
    a.imag[2,1,1,1]=-a.imag[1,2,1,1]
    a.imag[2,1,1,2]=-a.imag[1,2,2,1]
    a.imag[2,1,2,0]=-a.imag[1,2,0,2]
    a.imag[2,1,2,1]=-a.imag[1,2,1,2]
    a.imag[2,1,2,2]=-a.imag[1,2,2,2]
    a.imag[2,2,0,0]=0
    a.imag[2,2,1,0]=-a.imag[2,2,0,1]
    a.imag[2,2,1,1]=0
    a.imag[2,2,2,0]=-a.imag[2,2,0,2]
    a.imag[2,2,2,1]=-a.imag[2,2,1,2]
    a.imag[2,2,2,2]=0
    return a

def symmetrize_6(b):
    a = np.array(b, copy=True, dtype=complex)
    a.real[0,0,1,0]=a.real[0,0,0,1]
    a.real[0,0,2,0]=a.real[0,0,0,2]
    a.real[0,0,2,1]=a.real[0,0,1,2]
    a.real[0,1,0,0]=a.real[0,0,0,1]
    a.real[0,1,1,0]=a.real[0,0,1,1]
    a.real[0,1,2,0]=a.real[0,0,1,2]
    a.real[0,2,0,0]=a.real[0,0,0,2]
    a.real[0,2,0,1]=a.real[0,1,0,2]
    a.real[0,2,1,0]=a.real[0,0,1,2]
    a.real[0,2,1,1]=a.real[0,1,1,2]
    a.real[0,2,2,0]=a.real[0,0,2,2]
    a.real[0,2,2,1]=a.real[0,1,2,2]
    a.real[1,0,0,0]=a.real[0,0,0,1]
    a.real[1,0,0,1]=a.real[0,0,1,1]
    a.real[1,0,0,2]=a.real[0,0,1,2]
    a.real[1,0,1,0]=a.real[0,1,0,1]
    a.real[1,0,1,1]=a.real[0,1,1,1]
    a.real[1,0,1,2]=a.real[0,1,2,1]
    a.real[1,0,2,0]=a.real[0,1,0,2]
    a.real[1,0,2,1]=a.real[0,1,1,2]
    a.real[1,0,2,2]=a.real[0,1,2,2]
    a.real[1,1,0,0]=a.real[0,0,1,1]
    a.real[1,1,0,1]=a.real[0,1,1,1]
    a.real[1,1,0,2]=a.real[0,1,1,2]
    a.real[1,1,1,0]=a.real[0,1,1,1]
    a.real[1,1,2,0]=a.real[0,1,1,2]
    a.real[1,1,2,1]=a.real[1,1,1,2]
    a.real[1,2,0,0]=a.real[0,0,1,2]
    a.real[1,2,0,1]=a.real[0,1,1,2]
    a.real[1,2,0,2]=a.real[0,2,1,2]
    a.real[1,2,1,0]=a.real[0,1,2,1]
    a.real[1,2,1,1]=a.real[1,1,1,2]
    a.real[1,2,2,0]=a.real[0,1,2,2]
    a.real[1,2,2,1]=a.real[1,1,2,2]
    a.real[2,0,0,0]=a.real[0,0,0,2]
    a.real[2,0,0,1]=a.real[0,0,1,2]
    a.real[2,0,0,2]=a.real[0,0,2,2]
    a.real[2,0,1,0]=a.real[0,1,0,2]
    a.real[2,0,1,1]=a.real[0,1,1,2]
    a.real[2,0,1,2]=a.real[0,1,2,2]
    a.real[2,0,2,0]=a.real[0,2,0,2]
    a.real[2,0,2,1]=a.real[0,2,1,2]
    a.real[2,0,2,2]=a.real[0,2,2,2]
    a.real[2,1,0,0]=a.real[0,0,1,2]
    a.real[2,1,0,1]=a.real[0,1,2,1]
    a.real[2,1,0,2]=a.real[0,1,2,2]
    a.real[2,1,1,0]=a.real[0,1,1,2]
    a.real[2,1,1,1]=a.real[1,1,1,2]
    a.real[2,1,1,2]=a.real[1,1,2,2]
    a.real[2,1,2,0]=a.real[0,2,1,2]
    a.real[2,1,2,1]=a.real[1,2,1,2]
    a.real[2,1,2,2]=a.real[1,2,2,2]
    a.real[2,2,0,0]=a.real[0,0,2,2]
    a.real[2,2,0,1]=a.real[0,1,2,2]
    a.real[2,2,0,2]=a.real[0,2,2,2]
    a.real[2,2,1,0]=a.real[0,1,2,2]
    a.real[2,2,1,1]=a.real[1,1,2,2]
    a.real[2,2,1,2]=a.real[1,2,2,2]
    a.real[2,2,2,0]=a.real[0,2,2,2]
    a.real[2,2,2,1]=a.real[1,2,2,2]
    a.imag[0,0,0,0]=0
    a.imag[0,0,1,0]=-a.imag[0,0,0,1]
    a.imag[0,0,1,1]=0
    a.imag[0,0,2,0]=-a.imag[0,0,0,2]
    a.imag[0,0,2,1]=-a.imag[0,0,1,2]
    a.imag[0,0,2,2]=0
    a.imag[0,1,0,0]=a.imag[0,0,0,1]
    a.imag[0,1,1,0]=0
    a.imag[0,1,2,0]=-a.imag[0,0,1,2]
    a.imag[0,2,0,0]=a.imag[0,0,0,2]
    a.imag[0,2,0,1]=a.imag[0,1,0,2]
    a.imag[0,2,1,0]=a.imag[0,0,1,2]
    a.imag[0,2,1,1]=a.imag[0,1,1,2]
    a.imag[0,2,2,0]=0
    a.imag[0,2,2,1]=a.imag[0,1,2,2]
    a.imag[1,0,0,0]=-a.imag[0,0,0,1]
    a.imag[1,0,0,1]=0
    a.imag[1,0,0,2]=a.imag[0,0,1,2]
    a.imag[1,0,1,0]=-a.imag[0,1,0,1]
    a.imag[1,0,1,1]=-a.imag[0,1,1,1]
    a.imag[1,0,1,2]=-a.imag[0,1,2,1]
    a.imag[1,0,2,0]=-a.imag[0,1,0,2]
    a.imag[1,0,2,1]=-a.imag[0,1,1,2]
    a.imag[1,0,2,2]=-a.imag[0,1,2,2]
    a.imag[1,1,0,0]=0
    a.imag[1,1,0,1]=a.imag[0,1,1,1]
    a.imag[1,1,0,2]=a.imag[0,1,1,2]
    a.imag[1,1,1,0]=-a.imag[0,1,1,1]
    a.imag[1,1,1,1]=0
    a.imag[1,1,2,0]=-a.imag[0,1,1,2]
    a.imag[1,1,2,1]=-a.imag[1,1,1,2]
    a.imag[1,1,2,2]=0
    a.imag[1,2,0,0]=a.imag[0,0,1,2]
    a.imag[1,2,0,1]=a.imag[0,1,1,2]
    a.imag[1,2,0,2]=a.imag[0,2,1,2]
    a.imag[1,2,1,0]=-a.imag[0,1,2,1]
    a.imag[1,2,1,1]=a.imag[1,1,1,2]
    a.imag[1,2,2,0]=-a.imag[0,1,2,2]
    a.imag[1,2,2,1]=0
    a.imag[2,0,0,0]=-a.imag[0,0,0,2]
    a.imag[2,0,0,1]=-a.imag[0,0,1,2]
    a.imag[2,0,0,2]=0
    a.imag[2,0,1,0]=-a.imag[0,1,0,2]
    a.imag[2,0,1,1]=-a.imag[0,1,1,2]
    a.imag[2,0,1,2]=-a.imag[0,1,2,2]
    a.imag[2,0,2,0]=-a.imag[0,2,0,2]
    a.imag[2,0,2,1]=-a.imag[0,2,1,2]
    a.imag[2,0,2,2]=-a.imag[0,2,2,2]
    a.imag[2,1,0,0]=-a.imag[0,0,1,2]
    a.imag[2,1,0,1]=a.imag[0,1,2,1]
    a.imag[2,1,0,2]=a.imag[0,1,2,2]
    a.imag[2,1,1,0]=-a.imag[0,1,1,2]
    a.imag[2,1,1,1]=-a.imag[1,1,1,2]
    a.imag[2,1,1,2]=0
    a.imag[2,1,2,0]=-a.imag[0,2,1,2]
    a.imag[2,1,2,1]=-a.imag[1,2,1,2]
    a.imag[2,1,2,2]=-a.imag[1,2,2,2]
    a.imag[2,2,0,0]=0
    a.imag[2,2,0,1]=a.imag[0,1,2,2]
    a.imag[2,2,0,2]=a.imag[0,2,2,2]
    a.imag[2,2,1,0]=-a.imag[0,1,2,2]
    a.imag[2,2,1,1]=0
    a.imag[2,2,1,2]=a.imag[1,2,2,2]
    a.imag[2,2,2,0]=-a.imag[0,2,2,2]
    a.imag[2,2,2,1]=-a.imag[1,2,2,2]
    a.imag[2,2,2,2]=0
    return a

def symmetrize_7(b):
    a = np.array(b, copy=True, dtype=complex)
    a[1,0,0,0]=a[0,1,0,0]
    a[1,0,0,1]=a[0,1,0,1]
    a[1,0,0,2]=a[0,1,0,2]
    a[1,0,1,0]=a[0,1,1,0]
    a[1,0,1,1]=a[0,1,1,1]
    a[1,0,1,2]=a[0,1,1,2]
    a[1,0,2,0]=a[0,1,2,0]
    a[1,0,2,1]=a[0,1,2,1]
    a[1,0,2,2]=a[0,1,2,2]
    a[2,0,0,0]=a[0,2,0,0]
    a[2,0,0,1]=a[0,2,0,1]
    a[2,0,0,2]=a[0,2,0,2]
    a[2,0,1,0]=a[0,2,1,0]
    a[2,0,1,1]=a[0,2,1,1]
    a[2,0,1,2]=a[0,2,1,2]
    a[2,0,2,0]=a[0,2,2,0]
    a[2,0,2,1]=a[0,2,2,1]
    a[2,0,2,2]=a[0,2,2,2]
    a[2,1,0,0]=a[1,2,0,0]
    a[2,1,0,1]=a[1,2,0,1]
    a[2,1,0,2]=a[1,2,0,2]
    a[2,1,1,0]=a[1,2,1,0]
    a[2,1,1,1]=a[1,2,1,1]
    a[2,1,1,2]=a[1,2,1,2]
    a[2,1,2,0]=a[1,2,2,0]
    a[2,1,2,1]=a[1,2,2,1]
    a[2,1,2,2]=a[1,2,2,2]
    return a

def symmetrize_8(b):
    a = np.array(b, copy=True, dtype=complex)
    a[1,0,0,0]=a[0,0,1,0]
    a[1,0,0,1]=a[0,0,1,1]
    a[1,0,0,2]=a[0,0,1,2]
    a[1,1,0,0]=a[0,1,1,0]
    a[1,1,0,1]=a[0,1,1,1]
    a[1,1,0,2]=a[0,1,1,2]
    a[2,0,0,0]=a[0,0,2,0]
    a[2,0,0,1]=a[0,0,2,1]
    a[2,0,0,2]=a[0,0,2,2]
    a[2,0,1,0]=a[1,2,0,0]+a[1,0,2,0]-a[0,2,1,0]
    a[2,0,1,1]=a[1,2,0,1]+a[1,0,2,1]-a[0,2,1,1]
    a[2,0,1,2]=a[1,2,0,2]+a[1,0,2,2]-a[0,2,1,2]
    a[2,1,0,0]=a[0,2,1,0]+a[0,1,2,0]-a[1,2,0,0]
    a[2,1,0,1]=a[0,2,1,1]+a[0,1,2,1]-a[1,2,0,1]
    a[2,1,0,2]=a[0,2,1,2]+a[0,1,2,2]-a[1,2,0,2]
    a[2,1,1,0]=a[1,1,2,0]
    a[2,1,1,1]=a[1,1,2,1]
    a[2,1,1,2]=a[1,1,2,2]
    a[2,2,0,0]=a[0,2,2,0]
    a[2,2,0,1]=a[0,2,2,1]
    a[2,2,0,2]=a[0,2,2,2]
    a[2,2,1,0]=a[1,2,2,0]
    a[2,2,1,1]=a[1,2,2,1]
    a[2,2,1,2]=a[1,2,2,2]
    return a

def symmetrize_9(b):
    a = np.array(b, copy=True, dtype=complex)
    a[1,0]=a[0,1]
    a[2,0]=a[0,2]
    a[2,1]=a[1,2]
    return a

def symmetrize(C):
    C_symm = {}
    for i, v in C.items():
        if i in C_symm_keys[0] + C_symm_keys[1] + C_symm_keys[3]:
            C_symm[i] = v # nothing to do
        elif i in C_symm_keys[2]:
            C_symm[i] = symmetrize_2(C[i])
        elif i in C_symm_keys[4]:
            C_symm[i] = symmetrize_4(C[i])
        elif i in C_symm_keys[5]:
            C_symm[i] = symmetrize_5(C[i])
        elif i in C_symm_keys[6]:
            C_symm[i] = symmetrize_6(C[i])
        elif i in C_symm_keys[7]:
            C_symm[i] = symmetrize_7(C[i])
        elif i in C_symm_keys[8]:
            C_symm[i] = symmetrize_8(C[i])
        elif i in C_symm_keys[9]:
            C_symm[i] = symmetrize_9(C[i])
    return C_symm

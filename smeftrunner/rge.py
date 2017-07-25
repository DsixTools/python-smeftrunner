import numpy
from . import beta
from copy import deepcopy
from math import pi, log

def smeft_evolve_leadinglog(C_in, HIGHSCALE, t_in, t_out):
    C_out = deepcopy(C_in)
    b = beta.beta(C_in, HIGHSCALE)
    for k, C in C_out.items():
        C_out[k] = C + b[k]/(16*pi**2)*log(abs(t_out/t_in))
    return C_out

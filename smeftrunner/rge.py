import numpy
from . import beta
from copy import deepcopy
from math import pi, log
from scipy.integrate import odeint

def smeft_evolve_leadinglog(C_in, scale_high, scale_in, scale_out):
    C_out = deepcopy(C_in)
    b = beta.beta(C_in, HIGHSCALE=scale_high)
    for k, C in C_out.items():
        C_out[k] = C + b[k]/(16*pi**2)*log(scale_out/scale_in)
    return C_out

def smeft_evolve(C_in, scale_high, scale_in, scale_out, **kwargs):
    def func(y, t0):
        return beta.beta_array(C=beta.C_array2dict(y.view(complex)),
                               HIGHSCALE=scale_high).view(float)/(16*pi**2)
    y0 = beta.C_dict2array(C_in).view(float)
    sol = odeint(func=func, y0=y0, t=(log(scale_in), log(scale_out)), **kwargs)
    return beta.C_array2dict(sol[1].view(complex))

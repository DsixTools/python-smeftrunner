from . import rge
from . import io
import pylha

class SMEFT(object):
    """Parameter point in the Standard Model Effective Field Theory."""

    def __init__(self):
        self.C_in = None
        self.scale_in = None

    def set_initial(self, C_in, scale_in):
        self.C_in = C_in
        self.scale_in = scale_in

    def load_initial(self, streams):
        d = {}
        for stream in streams:
            s = io.load(stream)
            if 'BLOCK' not in s:
                raise ValueError("No BLOCK found")
            d.update(s['BLOCK'])
        d = {'BLOCK': d}
        C = io.wc_lha2dict(d)
        sm = io.sm_lha2dict(d)
        C.update(sm)
        self.C_in = C

    def dump(self, C_out, stream=None, fmt='lha'):
        sm = io.sm_dict2lha(C_out)['BLOCK']
        wc = io.wc_dict2lha(C_out)['BLOCK']
        wc.update(sm)
        return pylha.dump({'BLOCK': wc}, fmt=fmt, stream=stream)

    def rgevolve(self, scale_out, **kwargs):
        self._check_initial()
        return rge.smeft_evolve(C_in=self.C_in,
                            HIGHSCALE=self.scale_in,
                            scale_in=self.scale_in,
                            scale_out=scale_out,
                            **kwargs)

    def rgevolve_leadinglog(self, scale_out):
        self._check_initial()
        return rge.smeft_evolve_leadinglog(C_in=self.C_in,
                            HIGHSCALE=self.scale_in,
                            scale_in=self.scale_in,
                            scale_out=scale_out)

    def _check_initial(self):
        if self.C_in is None:
            raise Exception("You have to specify the initial conditions first.")
        if self.scale_in is None:
            raise Exception("You have to specify the initial scale first.")

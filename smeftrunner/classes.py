from . import rge

class SMEFT(object):
    """Parameter point in the Standard Model Effective Field Theory."""
    def __init__(self, C_in, scale_in):
        self.C_in = C_in
        self.scale_in = scale_in
        self.cache = {}

    def rgevolve(self, scale_out, **kwargs):
        return rge.smeft_evolve(C_in=self.C_in,
                            HIGHSCALE=self.scale_in,
                            scale_in=self.scale_in,
                            scale_out=scale_out,
                            **kwargs)

    def rgevolve_leadinglog(self, scale_out):
        return rge.smeft_evolve_leadinglog(C_in=self.C_in,
                            HIGHSCALE=self.scale_in,
                            scale_in=self.scale_in,
                            scale_out=scale_out)

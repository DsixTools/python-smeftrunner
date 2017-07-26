"""Defines the SMEFT class that provides the main API to smeftrunner."""

from . import rge
from . import io
import pylha

class SMEFT(object):
    """Parameter point in the Standard Model Effective Field Theory."""

    def __init__(self):
        """Initialize the SMEFT instance."""
        self.C_in = None
        self.scale_in = None
        self.scale_high = None

    def set_initial(self, C_in, scale_in, scale_high):
        r"""Set the initial values for parameters and Wilson coefficients at
        the scale `scale_in`, setting the new physics scale $\Lambda$ to
        `scale_high`."""
        self.C_in = C_in
        self.scale_in = scale_in
        self.scale_high = scale_high

    def load_initial(self, streams):
        """Load the initial values for parameters and Wilson coefficients from
        one or several files.

        `streams` should be a tuple of file-like objects strings."""
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
        """Return a string representation of the parameters and Wilson
        coefficients `C_out` in DSixTools output format. If `stream` is
        specified, export it to a file. `fmt` defaults to `lha` (the SLHA-like
        DSixTools format), but can also be `json` or `yaml` (see the
        pylha documentation)."""
        sm = io.sm_dict2lha(C_out)['BLOCK']
        wc = io.wc_dict2lha(C_out)['BLOCK']
        wc.update(sm)
        return pylha.dump({'BLOCK': wc}, fmt=fmt, stream=stream)

    def rgevolve(self, scale_out, **kwargs):
        """Solve the SMEFT RGEs from the initial scale to `scale_out`.
        Returns a dictionary with parameters and Wilson coefficients at
        `scale_out`. Additional keyword arguments will be passed to
        the ODE solver `scipy.integrate.odeint`."""
        self._check_initial()
        return rge.smeft_evolve(C_in=self.C_in,
                            scale_high=self.scale_high,
                            scale_in=self.scale_in,
                            scale_out=scale_out,
                            **kwargs)

    def rgevolve_leadinglog(self, scale_out):
        """Compute the leading logarithmix approximation to the solution
        of the SMEFT RGEs from the initial scale to `scale_out`.
        Returns a dictionary with parameters and Wilson coefficients.
        Much faster but less precise that `rgevolve`.
        """
        self._check_initial()
        return rge.smeft_evolve_leadinglog(C_in=self.C_in,
                            scale_high=self.scale_high,
                            scale_in=self.scale_in,
                            scale_out=scale_out)

    def _check_initial(self):
        """Check if initial values and scale as well as the new physics scale
        have been set."""
        if self.C_in is None:
            raise Exception("You have to specify the initial conditions first.")
        if self.scale_in is None:
            raise Exception("You have to specify the initial scale first.")
        if self.scale_high is None:
            raise Exception("You have to specify the high scale first.")

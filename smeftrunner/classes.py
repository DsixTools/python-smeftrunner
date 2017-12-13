"""Defines the SMEFT class that provides the main API to smeftrunner."""

from . import rge
from . import io
from . import definitions
import pylha
import wcxf
from collections import OrderedDict
from math import sqrt
import ckmutil.phases, ckmutil.diag

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
        C = definitions.symmetrize(C)
        self.C_in = C

    def set_initial_wcxf(self, wc):
        """Load the initial values for Wilson coefficients from
        wcxf.WC instance.

        Note that Standard Model parameters have to be provided separately
        and are assumed to be in the weak basis used for the Warsaw basis as
        defined in WCxf, i.e. in the basis where the down-type and charged
        lepton mass matrices are diagonal."""
        if wc.eft != 'SMEFT':
            raise ValueError("Wilson coefficients use wrong EFT.")
        if wc.basis != 'Warsaw':
            raise ValueError("Wilson coefficients use wrong basis.")
        C = wcxf.translators.smeft.wcxf2arrays(wc.dict)
        keys_dim5 = ['llphiphi']
        keys_dim6 = list(set(definitions.WC_keys_0f + definitions.WC_keys_2f + definitions.WC_keys_4f) - set(keys_dim5))
        for k in keys_dim5:
            if k in C:
                C[k] = C[k]*self.scale_high
        for k in keys_dim6:
            if k in C:
                C[k] = C[k]*self.scale_high**2
        C = definitions.symmetrize(C)
        self.C_in.update(C)

    def load_wcxf(self, stream):
        """Load the initial values for Wilson coefficients from
        a file-like object or a string in WCxf format.

        Note that Standard Model parameters have to be provided separately
        and are assumed to be in the weak basis used for the Warsaw basis as
        defined in WCxf, i.e. in the basis where the down-type and charged
        lepton mass matrices are diagonal."""
        wc = wcxf.WC.load(stream)
        self.set_initial_wcxf(wc)

    def dump(self, C_out, scale_out=None, stream=None, fmt='lha', skip_redundant=True):
        """Return a string representation of the parameters and Wilson
        coefficients `C_out` in DSixTools output format. If `stream` is
        specified, export it to a file. `fmt` defaults to `lha` (the SLHA-like
        DSixTools format), but can also be `json` or `yaml` (see the
        pylha documentation)."""
        C = OrderedDict()
        if scale_out is not None:
            C['SCALES'] = {'values': [[1, self.scale_high], [2, scale_out]]}
        else:
            C['SCALES'] = {'values': [[1, self.scale_high]]}
        sm = io.sm_dict2lha(C_out)['BLOCK']
        C.update(sm)
        wc = io.wc_dict2lha(C_out, skip_redundant=skip_redundant)['BLOCK']
        C.update(wc)
        return pylha.dump({'BLOCK': C}, fmt=fmt, stream=stream)

    def get_wcxf(self, C_out, scale_out):
        """Return the Wilson coefficients `C_out` as a wcxf.WC instance.

        Note that the Wilson coefficients are rotated into the Warsaw basis
        as defined in WCxf, i.e. to the basis where the down-type and charged
        lepton mass matrices are diagonal."""
        C = self.rotate_defaultbasis(C_out)
        d = wcxf.translators.smeft.arrays2wcxf(C)
        basis = wcxf.Basis['SMEFT', 'Warsaw']
        d = {k: v for k, v in d.items() if k in basis.all_wcs and v != 0}
        keys_dim5 = ['llphiphi']
        keys_dim6 = list(set(definitions.WC_keys_0f + definitions.WC_keys_2f
                             + definitions.WC_keys_4f) - set(keys_dim5))
        for k in d:
            if k.split('_')[0] in keys_dim5:
                d[k] = d[k] / self.scale_high
        for k in d:
            if k.split('_')[0] in keys_dim6:
                d[k] = d[k] / self.scale_high**2
        d = wcxf.WC.dict2values(d)
        wc = wcxf.WC('SMEFT', 'Warsaw', scale_out, d)
        return wc

    def dump_wcxf(self, C_out, scale_out, fmt='yaml', stream=None, **kwargs):
        """Return a string representation of the Wilson coefficients `C_out`
        in WCxf format. If `stream` is specified, export it to a file.
        `fmt` defaults to `yaml`, but can also be `json`.

        Note that the Wilson coefficients are rotated into the Warsaw basis
        as defined in WCxf, i.e. to the basis where the down-type and charged
        lepton mass matrices are diagonal."""
        wc = self.get_wcxf(C_out, scale_out)
        return wc.dump(fmt=fmt, stream=stream, **kwargs)

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

    def rotate_defaultbasis(self, C):
        """Rotate all parameters to the basis where the running down-type quark
        and charged lepton mass matrices are diagonal and where the running
        up-type quark mass matrix has the form V.S, with V unitary and S real
        diagonal, and where the CKM and PMNS matrices have the standard
        phase convention."""
        v = sqrt(2*C['m2'].real/C['Lambda'].real)
        Mep = v/sqrt(2) * (C['Ge'] - C['ephi'] * v**2/self.scale_high**2/2)
        Mup = v/sqrt(2) * (C['Gu'] - C['uphi'] * v**2/self.scale_high**2/2)
        Mdp = v/sqrt(2) * (C['Gd'] - C['dphi'] * v**2/self.scale_high**2/2)
        Mnup = -v**2 * C['llphiphi']
        UeL, Me, UeR = ckmutil.diag.msvd(Mep)
        UuL, Mu, UuR = ckmutil.diag.msvd(Mup)
        UdL, Md, UdR = ckmutil.diag.msvd(Mdp)
        Unu, Mnu = ckmutil.diag.mtakfac(Mnup)
        UuL, UdL, UuR, UdR = ckmutil.phases.rephase_standard(UuL, UdL, UuR, UdR)
        Unu, UeL, UeR = ckmutil.phases.rephase_pmns_standard(Unu, UeL, UeR)
        return definitions.flavor_rotation(C, Uq=UdL, Uu=UuR, Ud=UdR, Ul=UeL, Ue=UeR)

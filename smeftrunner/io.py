import numpy as np
from smeftrunner import beta
from collections import OrderedDict, defaultdict

def lhamatrix(values, shape):
    """Return a matrix given a list of values of the form
    [[1, 1, float], [1, 2, float], ...]
    referring to the (1,1)-element etc.
    `shape` is the shape of the final matrix. All elements not provided
    will be assumed to be zero. Also works for higher-rank tensors."""
    M = np.zeros(shape)
    for v in values:
        M[tuple([i-1 for i in v[:-1]])] = v[-1]
    return M

def sm_lha2dict(lha):
    """Convert a dictionary returned by pylha from a DSixTools SM input file
    into a dictionary of SM values."""
    d = OrderedDict()
    v = dict(lha['BLOCK']['GAUGE']['values'])
    d['g'] = v[1]
    d['gp'] = v[2]
    d['gs'] = v[3]
    v = dict(lha['BLOCK']['SCALAR']['values'])
    d['Lambda'] = v[1]
    d['m2'] = v[2]
    d['Gu'] = lhamatrix(lha['BLOCK']['GU']['values'], (3,3))
    if 'IMGU' in lha['BLOCK']:
        d['Gu'] = d['Gu'] + 1j*lhamatrix(lha['BLOCK']['IMGU']['values'], (3,3))
    d['Gd'] = lhamatrix(lha['BLOCK']['GD']['values'], (3,3))
    if 'IMGD' in lha['BLOCK']:
        d['Gd'] = d['Gd'] + 1j*lhamatrix(lha['BLOCK']['IMGD']['values'], (3,3))
    d['Ge'] = lhamatrix(lha['BLOCK']['GE']['values'], (3,3))
    if 'IMGE' in lha['BLOCK']:
        d['Ge'] = d['Ge'] + 1j*lhamatrix(lha['BLOCK']['IMGE']['values'], (3,3))
    # thetas default to 0
    if 'THETA' in lha['BLOCK']:
        v = dict(lha['BLOCK']['THETA']['values'])
        d['Theta'] = v.get(1, 0)
        d['Thetap'] = v.get(2, 0)
        d['Thetas'] = v.get(3, 0)
    else:
        d['Theta'] = 0
        d['Thetap'] = 0
        d['Thetas'] = 0
    return d

# dictionary necessary for translating to DSixTools IO format
WC_dict_0f = OrderedDict([
('G', ('WC1', 1)),
('Gtilde', ('WC1', 2)),
('W', ('WC1', 3)),
('Wtilde', ('WC1', 4)),
('phi', ('WC2', 1)),
('phiBox', ('WC3', 1)),
('phiD', ('WC3', 2)),
('phiG', ('WC4', 1)),
('phiB', ('WC4', 2)),
('phiW', ('WC4', 3)),
('phiWB', ('WC4', 4)),
('phiGtilde', ('WC4', 5)),
('phiBtilde', ('WC4', 6)),
('phiWtilde', ('WC4', 7)),
('phiWtildeB', ('WC4', 8)),
])

def wc_lha2dict(lha):
    """Convert a dictionary returned by pylha from a DSixTools WC input file
    into a dictionary of Wilson coefficients."""
    C = OrderedDict()
    # try to read all WCs with 0, 2, or 4 fermions; if not found, set to zero
    for k, (block, i) in WC_dict_0f.items():
        try:
            C[k] = dict(lha['BLOCK'][block]['values'])[i]
        except KeyError:
            C[k] = 0
    for k in beta.WC_keys_2f:
        try:
            C[k] = lhamatrix(lha['BLOCK']['WC' + k.upper()]['values'], (3,3))
        except KeyError:
            C[k] = np.zeros((3,3))
        try: # try to add imaginary part
            C[k] = C[k] + 1j*lhamatrix(lha['BLOCK']['IMWC' + k.upper()]['values'], (3,3))
        except KeyError:
            pass
    for k in beta.WC_keys_4f:
        try:
            C[k] = lhamatrix(lha['BLOCK']['WC' + k.upper()]['values'], (3,3,3,3))
        except KeyError:
            C[k] = np.zeros((3,3,3,3))
        try: # try to add imaginary part
            C[k] = C[k] + 1j*lhamatrix(lha['BLOCK']['IMWC' + k.upper()]['values'], (3,3,3,3))
        except KeyError:
            pass
    return C

def wc_dict2lha(wc):
    """Convert a dictionary returned by pylha from a DSixTools WC input file
    into a dictionary of Wilson coefficients."""
    d = OrderedDict()
    for name, (block, i) in WC_dict_0f.items():
        if block not in d:
            d[block] = defaultdict(list)
        if wc[name] != 0:
            d[block]['values'].append([i, wc[name]])
    for name in beta.WC_keys_2f:
        reblock = 'WC'+name.upper()
        imblock = 'IMWC'+name.upper()
        if reblock not in d:
            d[reblock] = defaultdict(list)
        if imblock not in d:
            d[imblock] = defaultdict(list)
        for i in range(3):
            for j in range(3):
                if wc[name][i, j].real != 0:
                    d[reblock]['values'].append([i+1, j+1, float(wc[name][i, j].real)])
                if wc[name][i, j].imag != 0:
                    d[imblock]['values'].append([i+1, j+1, float(wc[name][i, j].imag)])
    for name in beta.WC_keys_4f:
        reblock = 'WC'+name.upper()
        imblock = 'IMWC'+name.upper()
        if reblock not in d:
            d[reblock] = defaultdict(list)
        if imblock not in d:
            d[imblock] = defaultdict(list)
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        if wc[name][i, j, k, l].real != 0:
                            d[reblock]['values'].append([i+1, j+1, k+1, l+1, float(wc[name][i, j, k, l].real)])
                        if wc[name][i, j, k, l].imag != 0:
                            d[imblock]['values'].append([i+1, j+1, k+1, l+1, float(wc[name][i, j, k, l].imag)])
    # remove empty blocks
    empty = []
    for block in d:
        if d[block] == {}:
            empty.append(block)
    for block in empty:
        del d[block]
    return {'BLOCK': d}

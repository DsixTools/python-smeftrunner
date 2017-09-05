# python-smeftrunner

A Python package for the renormalization group (RG) evolution in the Standard Model Effective Field Theory (SMEFT).

This is a Python implementation of the SMEFTrunner module of the [DSixTools](https://dsixtools.github.io/) Mathematica package by Alejandro Celis, Javier Fuentes-Martín, Avelino Vicente, and Javier Virto ([arXiv:1704.04504](https://arxiv.org/abs/1704.04504)).

The renormalization group equations have been calculated in arXiv:1308.2627, arXiv:1310.4838, and arXiv:1312.2014 by Rodrigo Alonso, Elizabeth Jenkins, Aneesh Manohar, and Michael Trott.

The Python package was written by Xuanyou Pan and David Straub.

## Installation

The package requires Python version 3.5 or above as well as `numpy` and `scipy`, which are best installed using the system's package manager or a Python distribution like [Anaconda](https://docs.continuum.io/anaconda/).

With these prerequisites, the package can be installed simply with

```bash
python3 -m pip install smeftrunner
```

## Usage

The main interface is the `SMEFT` class that corresponds to a point in SMEFT parameter space and can be instantiated as

```python
from smeftrunner import SMEFT
smeft = SMEFT()
```

As input to the RG evolution, the values of all Standard Model (SM) parameters and SMEFT Wilson coefficients, as well as the initial scale and the new physics scale Λ (which can but don't have to coincide) have to be specified. The initial values can be read from a `DSixTools` input file:

```python
with open('my_input_file.dat', 'r') as f:
  smeft.load_initial((f,))
```

Note that the argument must always be a tuple; multiple input files can be specified in this way and will be read in turn (e.g. one file with SM parameters, one with Wilson coefficients):

```python
with open('my_sm_input.dat', 'r') as f1:
  with open('my_wc_input.dat', 'r') as f2:
    smeft.load_initial((f1, f2,))
```
The order of reading in the files is irrelevant.


The scales can simply be specified as

```python
smeft.scale_in = 1e4
smeft.scale_high = 1e4
```

Note that all dimensionful parameters are in units of GeV. The RGEs can now be solved numerically using e.g.

```python
C_out = smeft.rgevolve(scale_out=160)
```

The result can be exported to a `DSixTools` output file using

```python
smeft.dump(C_out, open('my_output_file.dat', 'w'))
```

Alternatively to the numerical solution of the RGEs, the leading logarithmic approximation can be accessed using

```python
C_out = smeft.rgevolve_leadinglog(scale_out=160)
```

This is much faster but less precise than the exact solution.

from setuptools import setup, find_packages

setup(name='smeftrunner',
      version='0.1',
      author='Xuanyou Pan, David M. Straub',
      author_email='xuanyou.pan@tum.de, david.straub@tum.de',
      url='https://github.com/DsixTools/smeftrunner',
      description='A Python package for the renormalization group evolution in the Standard Model Effective Field Theory (SMEFT).',
      long_description="""A Python package for the renormalization group
      evolution in the Standard Model Effective Field Theory (SMEFT).
      Based on the SMEFTrunner module of the DSixTools Mathematica package
      by Alejandro Celis, Javier Fuentes-Martín, Avelino Vicente,
      and Javier Virto (arXiv:1704.04504). RGEs based on arXiv:1308.2627,
      arXiv:1310.4838, and arXiv:1312.2014 by Rodrigo Alonso,
      Elizabeth Jenkins, Aneesh Manohar, and Michael Trott.""",
      license='MIT',
      packages=find_packages(),
      package_data={
      'smeftrunner':['tests/data/*',
              ]
      },
      install_requires=['scipy', 'pylha', 'pyyaml'],
    )

from setuptools import setup, find_packages

setup(name='smeftrunner',
      version='0.1',
      author='David M. Straub',
      author_email='david.straub@tum.de',
      url='https://github.com/DavidMStraub/smeftrunner',
      description='A Python package for the renormalization group evolution in the Standard Model Effective Field Theory (SMEFT).',
      license='MIT',
      packages=['smeftrunner'],
      package_data={
      'smeftrunner':['tests/data/*',
              ]
      },
      install_requires=['scipy', 'pylha', 'pyyaml'],
    )

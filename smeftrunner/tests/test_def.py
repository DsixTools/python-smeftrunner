import unittest
import numpy as np
import numpy.testing as npt
from smeftrunner import definitions

class TestSymm(unittest.TestCase):
    def test_keys(self):
        # check no parameter or WC was forgotten in the C_symm_keys lists
        self.assertEqual(
          set(definitions.C_keys),
          set([c for cs in definitions.C_symm_keys.values() for c in cs])
        )

# -*- coding: utf-8 -*-

from kata import mycalc

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertEqual(mycalc.power_by_2(5), 25)


if __name__ == '__main__':
    unittest.main()

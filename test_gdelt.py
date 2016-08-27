"""Unit testing and doc test testing for gdelt.py"""

import gdelt
import unittest
import doctest


class MyAppUnitTestCase(unittest.TestCase):
    """Unit tests for gdelt functions."""

    def test_get_URLs(self):
        assert gdelt.get_URLs()[-5:-1] == ['1983.zip', '1982.zip', '1981.zip', '1980.zip']

    def test_process_URL(self):
        self.assertEqual(gdelt.process_URL('20160818.export.CSV.zip'), 'http://data.gdeltproject.org/events/20160818.export.CSV.zip')

    def test_get_URLs_len(self):
        self.assertEqual(len(gdelt.get_URLs()[-6:-1]), 5)


def load_tests(loader, tests, ignore):
    """Also run our doctests and file-based doctests.

    This function name, ``load_tests``, is required.
    """

    tests.addTests(doctest.DocTestSuite(gdelt))
    tests.addTests(doctest.DocFileSuite("gdeltdoctests.txt"))
    return tests


if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()
import new_leap_year
from unittest import TestCase


class TestPrestupnyRok (TestCase):
    def test_valid_leap(self):
        leap = new_leap_year.leap_year(2000)
        self.assertIsNotNone(leap)
        self.assertTrue(leap)

    def test_valid_leap_not_100(self):
        leap = new_leap_year.leap_year(1996)
        self.assertIsNotNone(leap)
        self.assertTrue(leap)

    def test_invalid_leap_100(self):
        leap = new_leap_year.leap_year(1900)
        self.assertIsNotNone(leap)
        self.assertFalse(leap)

    def test_invalid_leap(self):
        leap = new_leap_year.leap_year(1998)
        self.assertIsNotNone(leap)
        self.assertFalse(leap)

    def test_invalid_string(self):
        leap = new_leap_year.leap_year("ahoj")
        self.assertIsNotNone(leap)
        self.assertFalse(leap)

    def test_invalid_float(self):
        leap = new_leap_year.leap_year(1003.20)
        self.assertIsNotNone(leap)
        self.assertFalse(leap)
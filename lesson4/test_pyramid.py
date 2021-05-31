import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
import pyramid
from unittest import TestCase


class TestPyramid(TestCase):
    def test_valid_5_normal_false(self):
        res = pyramid.create_pyramid(5, "normal", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*", "**", "***", "****", "*****"]
        )

    def test_valid_5_reversed_false(self):
        res = pyramid.create_pyramid(5, "reversed", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*****", "****", "***", "**", "*"]
        )

    def test_valid_5_normal_true(self):
        res = pyramid.create_pyramid(5, "normal", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["    *     ", "   * *    ", "  * * *   ", " * * * *  ", "* * * * * "]
        )

    def test_valid_5_reversed_true(self):
        res = pyramid.create_pyramid(5, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["* * * * * ", " * * * *  ", "  * * *   ", "   * *    ", "    *     "]
        )

    def test_invalid_float_reversed_true(self):
        self.assertRaises(
            TypeError, pyramid.create_pyramid,
            5.0, "normal", True
        )

    def test_invalid_reversed_not_bool(self):
        self.assertRaises(
            TypeError, pyramid.create_pyramid,
            5, "normal", 31
        )

    def test_invalid_second_parameter(self):
        self.assertRaises(
            TypeError, pyramid.create_pyramid,
            5, "notnormal", True
        )

    def test_valid_0_reversed_true(self):
        res = pyramid.create_pyramid(0, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            []
        )


class TestPyramid2(TestCase):
    def test_valid_5_normal_false(self):
        res = pyramid.create_pyramid_2(5, "normal", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*", "**", "***", "****", "*****"]
        )

    def test_valid_5_reversed_false(self):
        res = pyramid.create_pyramid_2(5, "reversed", False)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["*****", "****", "***", "**", "*"]
        )

    def test_valid_5_normal_true(self):
        res = pyramid.create_pyramid_2(5, "normal", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["    *     ", "   * *    ", "  * * *   ", " * * * *  ", "* * * * * "]
        )

    def test_valid_5_reversed_true(self):
        res = pyramid.create_pyramid_2(5, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            ["* * * * * ", " * * * *  ", "  * * *   ", "   * *    ", "    *     "]
        )

    def test_invalid_float_reversed_true(self):
        self.assertRaises(
            TypeError, pyramid.create_pyramid_2,
            5.0, "normal", True
        )

    def test_invalid_reversed_not_bool(self):
        self.assertRaises(
            TypeError, pyramid.create_pyramid_2,
            5, "normal", 31
        )

    def test_invalid_second_parameter(self):
        self.assertRaises(
            TypeError, pyramid.create_pyramid_2,
            5, "notnormal", True
        )

    def test_valid_0_reversed_true(self):
        res = pyramid.create_pyramid_2(0, "reversed", True)
        self.assertIsInstance(res, list)
        self.assertEqual(
            res,
            []
        )
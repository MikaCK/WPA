import du_random_text
from unittest import TestCase


class TestRandomText(TestCase):
    def test_generation_of_text(self):
        result = du_random_text.random_text(400)
        print(len(result))
        print(result)
        self.assertEqual(len(result), 400)

    def test_string_dlzka(self):
        self.assertRaises(
            TypeError, du_random_text.random_text, "20"
        )

    def test_float_dlzka(self):
        #result = du_random_text.random_text(10.4)
        self.assertRaises(
            TypeError, du_random_text.random_text, 10.4
        )

class TestDigitsDivisibleBy2(TestCase):
    def test_empty_input(self):
        result = du_random_text.digits_divisible_by_2("")
        self.assertEqual(result, [])

    def test_valid_input(self):
        result = du_random_text.digits_divisible_by_2("9ru nifq[ 039r 23[913 413123 1231 d hf q3 jfo;qj 3u9")
        self.assertEqual(result, [0, 2, 4])

    def test_int_input(self):
        #result = du_random_text.digits_divisible_by_2(12339423423)
        self.assertRaises(
            TypeError, du_random_text.digits_divisible_by_2, 12339423423
        )

    def test_float_input(self):
        #result = du_random_text.digits_divisible_by_2(10.5)
        self.assertRaises(
            TypeError, du_random_text.digits_divisible_by_2, 10.5
        )

# doplnit asserty, skontrolovat vysledky
# a doplnit dalsie testy, ktore vam napadnu

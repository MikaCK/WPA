import du_word_count
from unittest import TestCase


class TestWordCount(TestCase):
    def test_valid_input(self):
        expected_dict = {"ahoj": 1, "svet": 2, "dnes": 2, "hori": 1, "a": 1, "je": 1, "krasne": 1}
        result = du_word_count.word_count(["ahoj", "svet", "dnes", "svet", "hori", "a", "dnes", "je", "krasne"])
        self.assertDictEqual(result, expected_dict)

    def test_string_input(self):
        #result = du_word_count.word_count("ahoj svet dnes svet hori a dnes je krasne")
        self.assertRaises(
            TypeError, du_word_count.word_count, "ahoj svet dnes svet hori a dnes je krasne"
        )

    def test_int_input(self):
        #result = du_word_count.word_count(34234234)
        self.assertRaises(
            TypeError, du_word_count.word_count, 34234234
        )



# doplnit asserty, skontrolovat vysledky
# a doplnit dalsie testy, ktore vam napadnu


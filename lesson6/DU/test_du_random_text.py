import du_random_text
import string
from unittest import TestCase


class TestRandomText(TestCase):
    def test_generation_of_text(self):
        result = du_random_text.random_text(400)
        print(len(result))
        print(result)
        self.assertEqual(len(result), 400)
        # tu by sa dalo este eventualne doplnit kontrola kazdeho znaku, ci je
        # z rozsahu aky potrebujeme, ak by niekto prerabal funkciu
        # nech ho upozorni, ze tam dal nepovoleny znak
        # for znak in result:
        #     self.assertIn(znak, f"{string.ascii_letters} 1234567890")

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


# Zase ak ta zaujma output, pri testovanie je to ok, v 'ostrej' prevadzke sa
# snazime printy nepouzivat, zbytocne to spamuje

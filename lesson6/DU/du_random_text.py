import random
import string
from typing import List

def random_text(dlzka: int) -> str:
    """ Returns random string of 'dlzka'

    :param dlzka:  int   length of string
    :return: str  string of given  length
    """
    return "".join(random.choices(f"{string.ascii_letters} 1234567890", k=dlzka))


def digits_divisible_by_2(text: str) -> List[int]:
    """ Returns list of integers that are divisible by 2
    from given text

    :param text: str   text to go through
    :return: list  containing all numbers divisible by 2
    """
    number_list = [int(number) for number in text if number.isdigit() and int(number) % 2 == 0]
    return (list(set(number_list)))

# medzi funkciami a if-om by mali byt podla PEP8 2 medzery, inak nic hrozne 
if __name__ == "__main__":
    rnd_text = (random_text(250))
    print(rnd_text)
    print(digits_divisible_by_2(rnd_text))


# Uloha:
# Doplnit definiciu funkcie  digits_divisible_by_2()
# dopisat testy do  test_du_random_text.py


# mozno by som este validoval, ci su vstupy spravne
# aj ak chcem int, validoval by som ci som int zadal
# ak nie, nechat to spadnut, pripadne dat nejaku message
# zavisi od toho na co sa vo finale bude program vyuzivat

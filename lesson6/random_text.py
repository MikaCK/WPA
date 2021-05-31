import random
import string


def random_text(dlzka: int) -> str:
    return "".join(random.choices(f"{string.ascii_letters}1234567890", k=dlzka))
    #string.ascii_letters
    #chcem aj cislice
    #"" aj medzery


if __name__== "__main__":
    rnd_text = random_text(250)
    print(rnd_text)
    number_list = [int(number) for number in rnd_text if number.isdigit() and int(number) % 2 == 0]
    print(number_list)
import urllib.request
import ssl
from typing import Dict


def word_count(text: list) -> Dict[str, int]:
    """ Function counts number of words in text
    and returns dictionary in the form of :
    {"word1": 43, "word2": 3, "word3": 4}

    :param text: list   text that is used to go through parsed as list
    :return: Dict[str, int]   dictionary with keys defined as strings and values as integers
    """
    if not isinstance(text, list):
        raise TypeError("Input has to be a list")


    #parsed_text al. text = data.split(" ")  #and before or after get rid of diacritics
    word_freq = {}
    for word in text:
        if word in word_freq:
            count = word_freq.get(word)
            word_freq[word] = count + 1
        else:
            word_freq[word] = 1
#    print(word_freq)
#    printy v ramci funkcie nepozivaj.. pripadne si ich vzdy nakonci
#    zakomentuj
    return word_freq


if __name__ == "__main__":
    data = str(
        urllib.request.urlopen(
            "https://raw.githubusercontent.com/tomaspekarovic/PythonAcademy3/main/Lekcia6/scratch.txt",
            context = ssl._create_unverified_context()
        ).read().decode("utf-8"))

    # v data mate text.... opravit si ho, vysekat spatne znaky
    # data = "More importantly, a towel has immense psychological value."

    parsed_text = []  # tu si treba upravit data (ktore su str) do tvaru aby boli list, ktory vyzaduje funkcia
    data = data.replace(",", "").replace(".", "").replace("\n", "").replace(";", "").replace(":", "")\
        .replace("\"", "").replace("(", "").replace(")", "").replace("?", "").replace("—", "").replace("-", "")
    parsed_text = data.split(" ")
    print(word_count(parsed_text))


    # dostanem vypis
# or data instead of parsed_text
# + doplnit testy funkcie



def leap_year(year):
    """Function for leap year validation



    :param year: int year
    :return:  bool True/False

    """
    if isinstance(year, int):
        return False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
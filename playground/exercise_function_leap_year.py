def leap_year(year:int) -> bool:
    """Funcktion for checking leap year

    :param year: int year
    :return: true/false

    """
    if(year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
        return True
    else:
        return False


year: int = int(input("Zadaj rok:"))
leap: bool = leap_year(year)

if leap == True:
    print (f"Rok {year} je prestupny")
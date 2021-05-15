

year = input("Insert start year: ")
yearUntil = input("Insert end year: ")
year = int(year)
yearUntil = int(yearUntil)

if year > yearUntil:
    print("your starting year is greater than the end year")

while year <= yearUntil:

    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        print("Rok " + str(year) + " je prestupny")
    else:
        print("Rok " + str(year) + " je neprestupny")

    year = year + 1


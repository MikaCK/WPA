year = int(input("Zadaj rok:"))
end_year = year+10

while year <= end_year:
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        print("Rok " + str(year) + " je prestupny")

    year = year + 1
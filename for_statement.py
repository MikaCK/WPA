year = input("Insert start year: ")
year_until = input("Insert end year: ")
year = int(year)
year_until = int(year_until)

if year > year_until:
    print("your starting year is greater than the end year")

for year in range (year, year_until):

    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        print("Rok " + str(year) + " je prestupny")



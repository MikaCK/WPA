

year = input("Insert start year: ")
yearUntil = input("Insert end year: ")
year = int(year)
yearUntil = int(yearUntil)
# premenne sa podla PEP8 oznacuju vsetko malym a
# oddelene _ , tj.  year_until
# je to len konvencia, v starsich knizniciach sa najde aj
# camelCase ale je lepsie drzat sa PEP8 ak teda
# nedoplnam starsie kniznice, kde je vsetko camelCase

# pekne pouzitie podmienky na osetrenie vstupov
if year > yearUntil:
    print("your starting year is greater than the end year")

# pointou bolo pouzit for, ale toto je tiez validne
while year <= yearUntil:

    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        # ak je rok delitelny 400 je delitelny aj 4
        # takze druha zatvorka staci aby mala validaciu na 'or' year % 400
        # takto to zle nieje, ale je to zbytocne mierne narocnejsie
        # na vypocet a rychlost
        print("Rok " + str(year) + " je prestupny")
    else:
        print("Rok " + str(year) + " je neprestupny")

    year = year + 1

# v zadani sme sa bavili iba o vypisani prestupnych rokov, takze ten 1 print je
# tam zbytocny

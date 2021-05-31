
rok = int
zoznam_rokov = range(1983, 2020)
lp_compre = [rok for rok in zoznam_rokov if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0]
print(lp_compre)

#leap_year = []
#for rok in zoznam_rokov:
    #if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        #leap_year.append(rok)
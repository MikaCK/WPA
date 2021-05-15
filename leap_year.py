year = input("Input year: ")
year = int(year)
if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
         print("prestupny")
      else:
         print ("neprestupny")
    else:
       print ("prestupny")
else:
 print("neprestupny")






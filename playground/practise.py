# command = ""
# started = False
#
# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "stop":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped...")
#     elif command == "help":
#         print("""
#     start - to start the car
#     stop - to stop the car
#     quit - to quit
#     """)
#     elif command == "quit":
#         break
#     else:
#       print("Sorry, I don't understand that")

# prices = [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total:{total}")

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

# numbers = [1, 1, 1, 1, 5]
# for x_count in numbers:
#     output = ""
#     for count in range(x_count):
#         output += "x"
#     print(output)

# numbers = [3, 6, 2, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# phone = input("Phone:")
# digits_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
# }
# output = ""
# for char in phone:
#     digits_mapping.get(char, "!")
#     output += digits_mapping.get (char, "!") + " "
# print(output)

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "😒",
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
#
# for i in range(1, 11):
#     print("{:3} {:4} {:5} {:6}". format(i, i * i, i ** 3, i ** 4))





#!MARCO!
# n = int(input('zadaj pocet: '))
#
# for i in range(n):
#     print(' '*(n-1-i) + '*'*(2*i+1))
#
# for i in range(n):
#     print(' '*i + '*'*(2*n-2*i-1))


n = int(input('zadaj cislo: '))
sucin = 1
for i in range(1, n + 1):
    sucin = sucin * i                  # alebo  sucin *= i
print('{}! = {}'.format(n, sucin))



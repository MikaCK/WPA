import random

rows = int(input("Zadaj pocet riadkov:"))
cols = int(input("Zadak pocet stlpcov"))

min_ = int(input("Zadaj minimalnu hodnotu"))
max_ = int(input("Zadaj maximalnu hodnotu"))

def generate_matrix(rows, cols,min_, max_):
    outer_list = []
    for _ in range(rows):
     inner_list = []
     for _ in range(cols):
      inner_list.append(random.randint(min_, max_))
    outer_list.append(inner_list)
    return outer_list

matrix = generate_matrix(rows, cols, min_, max_)
for inner in matrix:
    for item in inner:
        print(f"{item:>10}", end="")
    print()


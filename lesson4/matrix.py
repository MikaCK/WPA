import random


rows = int(input("Zadaj pocet riadkov: "))
cols = int(input("Zadaj pocet stlpcov: "))

min_ = int(input("Zadaj minimalnu hodnotu: "))
max_ = int(input("Zadaj maximalnu hodnotu: "))

# rows = 2; cols = 5; min_ = 1; max_ = 5
# x x x x x
# x x x x x

# [x x x x x]
# [x x x x x]

# [
#     [x x x x x]
#     [x x x x x]
# ]
def generate_matrix(rows, cols, min_, max_):
    outer_list = []
    for _ in range(rows):
        inner_list = []   # inner_list = list()
        for _ in range(cols):
            inner_list.append(random.randint(min_, max_))
        outer_list.append(inner_list)
    return outer_list


matrix = generate_matrix(rows, cols, min_, max_)
for inner in matrix:
    for item in inner:
        print(f"{item:>10}", end="")
    print()


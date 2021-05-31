from typing import List


def create_pyramid(base: int, orientation: str, center: bool) -> List[str]:
    """ vyrobi pyramidu na zaklade vstupov
    :param base: int  pocet * zakladne
    :param orientation: str reversed, normal
    :param center: bool  true / false
    :return: list  s riadkami pyramidy
    """
    if not isinstance(base, int) or not isinstance(orientation, str) \
            or not isinstance(center, bool) or orientation not in ['normal', 'reversed']:
        raise TypeError("Input parameters are: base: int, orientation: str[normal, reversed], center: bool")
    pyramid = []


    for i in range(base):
        if orientation == "normal":
            row = "*"*(i+1)
        else:
            row = "*" * (base - i)

        pyramid.append(row)

    print(f"Center: {center}")
    if center:
        for idx, value in enumerate(pyramid):
            centered = ""
            for char in value:
                centered += f"{char} "
            print(f"CENTERED: {centered}")
            pyramid[idx] = f"{centered:^{base*2}}"
            print(f"PYRAMID[idx] = '{pyramid[idx]}'")
    return pyramid

if __name__ == "__main__":
    pyramida = create_pyramid(5, "reversed", True)
    print(f"PYRAMIDA: {pyramida}")

    print()
    for x in pyramida:
        print(x)
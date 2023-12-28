import unittest
from math import sqrt

def find_hypotenuse(a,b):
    if (a == 0 or b == 0):
        raise Exception('A side cannot be equal to 0')
    return sqrt(a**2 + b**2)


if __name__ == "__main__":
    a = 4
    b = 3
    h = find_hypotenuse(a, b)
    print(f'Find hypotenuse')
    print(f'a:{a}, b:{b}')
    print(f"Hypotenuse {h}")



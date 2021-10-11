"""
Name: Madeleine Ellegard
lab7.py
"""
import math


def cash_conversion():
    ui = eval(input("enter in an integer: "))
    print('${:.2f}'.format(ui))


def encode():
    word = input("enter in a secret word: ")
    key = eval(input("enter in the key number: "))
    acc = " "
    for c in word:
        i = ord(c)
        i = i + key
        new_char = chr(i)
        acc = acc + new_char
    print(acc)


def sphere_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return surface_area


def sphere_volume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume


def sum_n(n):
    acc = 0
    for c in range(n):
        acc = acc + (c + 1)
    return acc


def sum_n_cubes(n):
    acc = 0
    for c in range(n):
        acc = acc + c ** 2
    return acc


def encode_better():
    m = input("Enter in a message: ")
    k = input("encode it: ")
    acc = " "
    for i in range(len(m)):
        c = ord(m[i])
        key = ord(k[i])
        c = (c + key) - 97
        acc += chr(c)
    print(acc)


def main():
    cash_conversion()
    encode()
    print(sphere_area(2))
    print(sphere_volume(5))
    print(sum_n(10))
    print(sum_n_cubes(10))
    encode_better()


main()

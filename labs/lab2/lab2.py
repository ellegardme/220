"""
Name: Madeleine Ellegard
lab2.py

Problem: to do basic math equations in python

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_three():
    acc = 0
    u = eval(input("Enter an upper bound: "))
    for x in range(0, u, 3):
        acc = acc + x
    print(acc)


sum_of_three()


def multiplication_table():
    for h in range(1, 11):
        for s in range(1, 11):
            print(h * s, end=" ")
        print()


multiplication_table()


def triangle_area():
    a = eval(input("Enter side a: "))
    b = eval(input("Enter side b: "))
    c = eval(input("Enter side c: "))
    y = (a + b + c) / 2
    area = math.sqrt(y * (y - a) * (y - b) * (y - c))
    print(area)


triangle_area()


def sumSquares():
    acc = 0
    x = eval(input("Enter a lower range: "))
    y = eval(input("Enter an upper range: "))
    for x in range(x, y + 1):
        acc = acc + (x * x)
    print(acc)


sumSquares()


def power():
    acc = 1
    base = eval(input("Enter a base: "))
    exp = eval(input("Enter an exponent: "))
    for x in range(exp):
        acc = acc * base
    print(base, "^", exp, "=", acc)


power()

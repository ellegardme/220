"""
Name: Madeleine Ellegard
lab3.py

Problem: to practice using for loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    amount = eval(input("how many grades are you entering? "))
    acc = 0
    for n in range(1, amount + 1):
        grade = (eval(input("Enter your grade on HW" + str(n) + ": ")))
        acc = acc + grade
    acc = acc / amount
    print("Your average grade is", acc)


average()


def tip_jar():
    acc = 0
    for n in range(5):
        tip = eval(input("How much are you donating? "))
        acc = acc + tip
    print("You have $", acc, "in tips")


tip_jar()


def newton():
    x = eval(input("enter in a number: "))
    refine = eval(input("enter in the number to refine: "))
    approx = x / 2
    for n in range(refine):
        approx = (approx + (x / approx)) / 2
    print(approx)


newton()


def sequence():
    terms = eval(input("Enter in the number of terms in the series: "))
    for x in range(1, terms + 1):
        print(1 + (x // 2 * 2))


sequence()


def pi():
    n = eval(input("Enter in the amount of terms in the series: "))
    acc = 1
    for x in range(n):
        numer = 2 + (x // 2 * 2)
        denom = 1 + ((x + 1) // 2 * 2)
        frac = numer / denom
        acc = acc * frac
    print(acc)


pi()

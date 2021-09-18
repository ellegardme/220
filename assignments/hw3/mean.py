"""
Name: Madeleine Ellegard
mean.py

Problem: To practice math loops

Certification of Authenticity:
I certify that this assignment is entirely my own work.

What will the program do?
Calculate three different means from a set of number
What will be the inputs and outputs?
Inputs will be numbers and outputs will be means of those numbers
What is a step-by-step list of what the program must do, aka an algorithm?
    Ask users how many inputs
    Use a loop to allow the user enter in the amount of inputs
    Calculate the RMS mean:
    Calculate the harmonic mean:
    Calculate the geometric mean:
    Print rounded answers
"""
import math


def main():
    num = eval(input("enter the values to be entered: "))
    acc = 0
    denom = 0
    geo = 1
    for n_n in range(num):
        questions = eval(input("enter value " + str(n_n + 1) + ": "))
        numerator = num
        denom = denom + (1 / questions)
        acc = acc + questions ** 2
        rms_average = round(math.sqrt(acc / num), 3)
        harmonic_mean = round((numerator / denom), 3)
        geo = geo * questions
        geometric_mean = round(geo ** (1 / num), 3)
    print(rms_average)
    print(harmonic_mean)
    print(geometric_mean)


if __name__ == "__main__":
    main()

"""
Name: Madeleine Ellegard
lab9.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import math

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])


def writeSumOfSquares():
    infile = input("What is the name of the input file? ")
    readfile = open(infile, "r")
    writefile = open("outfile.txt", "w")
    for line in readfile:
        nums = line.split()
        toNumbers(nums)
        squareEach(nums)
        summation = sumList(nums)
        writefile.write("Sum of squares = " + str(summation) + "\n")


def starter():
    weight = eval(input("Enter in the player's weight: "))
    numWins = eval(input("Enter in the player's wins: "))
    if 150 <= weight < 160 and numWins >= 5:
        print("Starter")
    elif weight > 199 or numWins > 20:
        print("Starter")
    else:
        print("He is not a starter")


def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(str(year) + " is a leap year")
    else:
        print(str(year) + " is not a leap year")


def circleoverlap():
    win = GraphWin("Circle", 400, 400)
    # circle 1
    p1 = win.getMouse()
    p2 = win.getMouse()
    r1 = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    c1 = Circle(p1, r1)
    c1.draw(win)

    # circle 2
    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    c2 = Circle(p3, r2)
    c2.draw(win)

    if math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2) <= r1 + r2:
        text_space = Point(200, 350)
        txt = Text(text_space, "It overlaps")
        txt.draw(win)
    else:
        text_space2 = Point(200, 350)
        txt2 = Text(text_space2, "It  doesn't overlap")
        txt2.draw(win)

    win.getMouse()
    win.close()


def main():
    addTen([2, 5, 6])
    squareEach([4, 7, 8])
    sumList([34, 6, 78])
    toNumbers([5, 34, 1])
    writeSumOfSquares()
    starter()
    leapYear(2100)
    circleoverlap()
    pass


main()

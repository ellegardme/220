"""
Name: Madeleine Ellegard
lab4.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move the rectangle")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the rectangle
    for i in range(num_clicks):
        user_click = win.getMouse()
        # builds a circle
        shape = Rectangle(Point(user_click.x - 10, user_click.y - 10), Point(user_click.x + 10, user_click.y + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    inst_pt = Point(width / 2, 10)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    point1 = win.getMouse()
    point2 = win.getMouse()

    rect = Rectangle(point1, point2)
    rect.setFill("blue")
    rect.draw(win)

    length = abs(point2.getX() - point1.getX())
    width = abs(point2.getY() - point1.getY())
    area = length * height
    perimeter = 2 * (length + width)

    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "The area is: " + str(area))
    instructions.draw(win)

    inst_pt = Point(width / 2, 10)
    instructions = Text(inst_pt, "The perimeter is: " + str(perimeter))
    instructions.draw(win)

    inst_pt = Point(50, 50)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    point1 = win.getMouse()
    point2 = win.getMouse()

    x1 = point1.getX()
    x2 = point2.getX()
    y1 = point1.getY()
    y2 = point2.getY()

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    cir = Circle(point1, d)
    cir.setFill("orange")
    cir.draw(win)

    inst_pt = Point(width / 2, 10)
    instructions = Text(inst_pt, "The radius is: " + str(d))
    instructions.draw(win)

    inst_pt = Point(width / 2, 50)
    instructions = Text(inst_pt, "Click again to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def pi2():
    i = eval(input("Enter in n: "))
    acc = 0
    for n in range(i):
        num = 4
        denom = 1 + (2 * i)
        frac = (num / denom) * ((-1) ** i)
        acc = acc + frac
    print(acc)
    print(math.pi - acc)


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()

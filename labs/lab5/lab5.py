"""
Name: <your name goes here – first and last>
<ProgramName>.py
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()

    s1 = Line(point1, point2)
    s2 = Line(point2, point3)
    s3 = Line(point3, point1)

    l1 = math.sqrt((point2.getX() - point1.getX()) ** 2 + (point2.getY() - point1.getY()) ** 2)
    l2 = math.sqrt((point3.getX() - point2.getX()) ** 2 + (point3.getY() - point2.getY()) ** 2)
    l3 = math.sqrt((point3.getX() - point1.getX()) ** 2 + (point3.getY() - point1.getY()) ** 2)

    s1.draw(win)
    s2.draw(win)
    s3.draw(win)

    perimeter = l1 + l2 + l3
    txt_perimeter = Text(Point(win_width / 2, 50), "The perimeter is: " + str(perimeter))
    txt_perimeter.draw(win)

    s = (l1 + l2 + l3) / 2
    area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))

    txt = Text(Point(win_width / 2, 10), "The area is: " + str(area))
    txt.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    """Create code to allow a user to color a shape by entering rgb amounts"""

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_box = Entry(Point(win_width / 2 - 20, win_height / 2 + 40), 3)
    red_box.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_box = Entry(Point(win_width / 2 - 20, win_height / 2 + 70), 3)
    green_box.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_box = Entry(Point(win_width / 2 - 20, win_height / 2 + 100), 3)
    blue_box.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    win.getMouse()
    for i in range(5):
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)
        win.getMouse()

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    ui = input("Enter in a string: ")
    print(ui[0])
    print([ui[-1]])
    print(ui[2:6])
    print(ui[0] + ui[-1])
    print(ui[0:3] * 10)
    for c in ui:
        print(c)
    print(len(ui))


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)

    x = values[0] + values[2]
    print(x)

    x = values[1] * 5
    print(x)

    x = values[2:5]
    print(x)

    x = [values[2], values[3], values[0]]
    print(x)

    x = [values[2], values[0], float(values[5])]
    print(x)

    x = values[0] + values[2] + eval(values[5])
    print(x)

    x = len(values)
    print(x)


def another_series():
    amount = eval(input("enter in the number of terms: "))
    acc = 0
    for i in range(amount):
        acc = 2 + (2 * (i % 3))
        print(acc, end=" ")
    sum_num = acc + amount
    print("sum = ", sum_num)


def main():
    # target()
    triangle()
    color_shape()
    process_string()
    process_list()
    another_series()

    pass


main()

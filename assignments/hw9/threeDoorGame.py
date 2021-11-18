"""
Name: Madeleine Ellegard
threeDoorGame.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with Logan
"""
from button import Button
from graphics import Point, Text, Rectangle, GraphWin
from random import randint


def main():
    # The window set up
    width = 600
    height = 600
    win = GraphWin("Three Button Game", width, height)

    # Text Boxes
    message_pt = Point(width / 2, 50)
    message = Text(message_pt, "I have a secret door")
    message.draw(win)
    message_pt2 = Point(width / 2, 550)
    message2 = Text(message_pt2, "click to choose my door")
    message2.draw(win)

    # Doors
    door1 = Button(Rectangle(Point(50, 300), Point(200, 400)), Text(Point(125, 350), "Door 1"))
    Button.draw(door1, win)
    door2 = Button(Rectangle(Point(225, 300), Point(375, 400)), Text(Point(300, 350), "Door 2"))
    Button.draw(door2, win)
    door3 = Button(Rectangle(Point(400, 300), Point(550, 400)), Text(Point(475, 350), "Door 3"))
    Button.draw(door3, win)

    user_click = win.getMouse()
    lst = door1, door2, door3
    correct = randint(0, 2)
    for i in range(len(lst)):
        if lst[i].is_clicked(user_click):
            if i == correct:
                lst[i].color_button("green")
                message.setText("You Win!")
                message2.setText("click to close")
            else:
                lst[i].color_button("red")
                message.setText("You Lost!")
                message2.setText("door" + str(correct + 1) + " is my secret door")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()

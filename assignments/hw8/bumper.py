"""
Name: Madeleine Ellegard
bumper.py

Problem: To make a bumper car game

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with
"""
import time

import graphics
from random import randint
from math import sqrt


def get_random(move_amount):
    random = randint(0 - move_amount, move_amount)
    return random


def get_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = [r, g, b]
    return rgb


def did_collide(circle_ball1, circle_ball2):
    r1 = circle_ball1.getRadius()
    r2 = circle_ball2.getRadius()
    if r1 + r2 == 0 or r1 + r2 == 10:
        return True


def hit_vertical(circle_ball, window):
    down = circle_ball.getCenter().getY() + circle_ball.getRadius()
    up = circle_ball.getCenter().getY() - circle_ball.getRadius()
    if down >= window.getHeight() or up <= 0:
        return True


def hit_horizontal(circle_ball, window):
    side1 = circle_ball.getCenter().getX() + circle_ball.getRadius()
    side2 = circle_ball.getCenter().getX() - circle_ball.getRadius()
    if side1 >= window.getWidth() or side2 <= 0:
        return True



def main():
    # window set up
    w = 400
    h = 400
    win = graphics.GraphWin("Bumper", w, h)

    # circle
    circle_one = graphics.Circle(graphics.Point(200, 200), 10)
    circle_two = graphics.Circle(graphics.Point(100, 200), 10)
    circle_one.draw(win)
    circle_two.draw(win)

    # loop
    is_moving = True
    dx = get_random(10)
    dy = get_random(10)
    dxx = get_random(10)
    dyy = get_random(10)
    while is_moving:
        graphics.time.sleep(.1)
        circle_one.move(dx, dy)
        circle_one.setFill(get_random_color())
        circle_two.move(dxx, dyy)
        circle_one.setFill(get_random_color())
        if hit_vertical(circle_one, win):
            circle_one.move(dx, (dy * (-1)))
            circle_two.move(dxx, (dy * (-1)))
        if hit_horizontal(circle_two, win):
            circle_one.move(dx * (- 1), dy)
            circle_two.move(dxx * (-1), dyy)
        if did_collide(circle_one, circle_two):
            circle_one.move(dx * (- 1), dy)
            circle_two.move(dxx * (-1), dyy)


    win.getMouse()
    win.close()


if __name__ == '__main__':

    main()

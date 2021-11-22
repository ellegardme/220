"""
Name: Madeleine Ellegard
lab12.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def find_and_remove_first(lst, value):
    try:
        i = lst.index(value)
        lst[i] = "madeleine"
    except:
        pass


def read_data(filename):
    f = open(filename, "r")
    data = f.read()
    data = data.split()
    return data


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if i == search_val:
            return True
        i += 1
    return False


def good_input():
    x = eval(input("enter in a number between 1 and 10: "))
    while not x >= 1 and x <= 10:
        x = eval(input("enter a correct number: "))
        return x


def num_digits():
    num = eval(input("enter in a number: "))
    while num >= 1:
        digits = 0
        while not num == 0:
            num //= 10
            digits += 1
        print("There were " + str(digits) + " in your statement")
        num = eval(input("enter in a number: "))


def high_lo_game():
    secret = randint(1, 100)
    guess = 1
    num = eval(input("Please guess a number: "))
    while (not secret == num) and (not guess == 7):
        guess += 1
        if num > secret:
            print("too high")
        else:
            print("too low")
        num = eval(input("Please guess a number: "))
    if secret == num:
        print("You won in " + str(guess) + " guesses")
    else:
        print("Sorry, you lose. The number was " + str(secret))


def main():
    find_and_remove_first([1, 2, 5, 8, 6], 2)
    read_data("dataSorted.txt")
    is_in_linear(2, "dataSorted.txt")
    good_input()
    num_digits()
    high_lo_game()
    pass


main()

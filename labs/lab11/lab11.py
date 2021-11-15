"""
Name: Madeleine Ellegard
lab11.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint


def words(itn):
    infile = open(itn, "r")
    contents = infile.read()
    return contents.split("\n")


def random_word(lst):
    return lst[randint(0, len(lst) - 1)]


def fill(word, letters):
    secret = ["_"] * len(word)
    for letter in letters:
        for i in range(len(word)):
            if letter == word[i]:
                secret[i] = letter
    return "".join(secret)


def won(word, letters):
    x = fill(word, letters)
    if word == x:
        print("You won!")
        return True


def play():
    w = words("wordlist.txt")
    secret = random_word(w)
    incorrect = 0
    guesses = []
    while incorrect <= 7 and not won(secret, guesses):
        display = fill(secret, guesses)
        print(display)
        print(guesses)
        letter = input("Enter in a guess: ")
        while letter in guesses:
            letter = input("Guess a different letter: ")
        guesses.append(letter)
        if letter not in secret:
            incorrect += 1


def main():
    play()
    pass


main()

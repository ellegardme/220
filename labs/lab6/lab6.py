"""
Name: Madeleine Ellegard
lab6.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input("Enter in a first and last name separated by a space: ")
    txt = name.split(" ")
    print(txt[1] + ", " + txt[0])


def company_name():
    domain = input("Enter in a domain name: ")
    name = domain.split(".")
    print(name[1])

def initials():
    i = 0
    amount = eval(input("How many students are you entering? "))
    for i in range(amount):
        student_first = input("Enter the name of student " + str(i + 1) + ": ")
        student_last = input("Enter " + student_first + "'s " + "last name: ")
        print(student_first + "'s initials are " + (student_first[0] + student_last[0]).upper())

def names():
    names_input = input("Enter in a list of names separated by a comma: ")
    names_input = names_input.split(", ")
    print("The initials are:", end=" ")
    for i in names_input:
        y = i.split(" ")
        print((y[0][0] + y[1][0]).upper(), end=" ")

def thirds():
    sentence = input("Enter in a sentence: ")
    for i in range(2, len(sentence), 3):
        print(sentence[i], end="")

def word_average():
    acc = 0
    sentence = input("Enter in a sentence: ")
    sentence = sentence.split(" ")
    for word in sentence:
        acc = acc + len(word)
        average = acc / len(sentence)
    print(average)

def pig_latin():
    sentence = input("Enter in a sentence: ")
    sentence = sentence.split(" ")
    for word in sentence:
        pig = word[1:] + word[0] + "ay"
        print(pig, end=" ")

def main():
    name_reverse()
    company_name()
    initials()
    thirds()
    names()
    word_average()
    pig_latin()

main()

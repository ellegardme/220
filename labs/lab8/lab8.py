"""
Name: Madeleine Ellegard
lab8.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    i = 1
    for line in infile:
        words = line.split()
        for word in words:
            outfile.write(str(i) + " " + word + "\n")
            i += 1
    infile.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        parts = line.split()
        wage = float(parts[2])
        wage += 1.65
        wage = wage * float(parts[3])
        outfile.write(parts[0] + " " + parts[1] + " " + parts[2] + " " + str(wage) + "\n")


def calc_check_sum(isbn_str):
    acc = 0
    for i in range(10):
        pos = 10 - i
        acc += int(isbn_str[0]) * pos
    return acc


def send_message(fn, friend):
    infile = open(fn, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(line + "\n")


def send_safe_message(fn, friend, key):
    infile = open(fn, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode(line, key))


def send_uncrackable_message(fn, friend, pad):
    padfile = open(pad, "r")
    key = padfile.read()
    infile = open(fn, "r")
    outfile = open(friend + ".txt", "w+")
    for line in infile:
        outfile.write(encode_better(line, key))


def main():
    number_words("walrus.txt", "count.txt")
    hourly_wages("hourly_wages.txt", "new_wages.txt")
    calc_check_sum("0072946520")
    send_message("message.txt", "laura")
    send_safe_message("secret_message.txt", "liz", 5)
    send_uncrackable_message("safest_message.txt", "grace", "pad.txt")

    # add other function calls here
    pass


main()

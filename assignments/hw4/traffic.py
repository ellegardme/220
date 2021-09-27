"""
Name: Madeleine Ellegard
traffic.py

Problem: To survey the amount of cars that travel on roads

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    amount = eval(input("How many roads were surveyed? "))
    acc = 1
    time = 1
    for i in range(amount):
        days = eval(input("How many days was road 1 surveyed? "))
        for days in range(amount):
            cars = eval(input("How many cars traveled on day? "))
            acc = acc + cars
            print("Road", time, "average vehicles per day: ", cars)
        print(cars)
    print(days)
    print(days)


main()

"""
Name: Madeleine Ellegard
traffic.py

Problem: To survey the amount of cars that travel on roads

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with Addison McFee.
"""


def main():
    amount = eval(input("How many roads were surveyed? "))
    acc = 0
    for i in range(amount):
        days = eval(input("How many days was road " + str(i + 1) + " surveyed? "))
        total = 0
        for j in range(days):
            cars = eval(input("How many cars traveled on day " + str(j + 1) + " ? "))
            total = total + cars
        road_average = total / days
        print("Road " + str(i + 1) + " average vehicles per day: ", round(road_average, 2))
        acc = acc + total
    print("Total number of vehicles traveled on all roads: ", acc)
    car_average = acc / amount
    print("Average number of vehicles per road: ", round(car_average, 2))


if __name__ == '__main__':
    main()

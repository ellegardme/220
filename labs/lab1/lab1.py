"""
Name: <Madeleine Ellegard>
labl.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval (input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    made = eval(input("Enter the shots made: "))
    total = eval(input("Enter total shots made: "))
    percentage = (made / total) * 100
    print("Percentage = ", percentage)


def coffee():
    pounds = eval(input("Enter the number of pounds purchased: "))
    total = (10.50 * pounds) + (0.86 * pounds) + 1.50
    print("Total cost: ", total)

def kilometers_to_miles():
    km = eval(input("Enter the amount of kilometers traveled: "))
    convert = km / 1.61
    print("Total miles: ", convert)



calc_rec_area()
calc_volume()
shooting_percentage()
coffee()
kilometers_to_miles()
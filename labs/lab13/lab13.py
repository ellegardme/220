"""
Name: Madeleine Ellegard
lab13.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def is_in_binary(search_val, values):
    mid = values[len(values) / 2]
    while not mid == search_val and len(values) != 1:
        if search_val > mid:
            values = values[mid]
        else:
            values = values[0: mid]
        mid = values[len(values)//2]
    if len(values) == 1 and values[0] != search_val:
        return False
    else:
        return True


def selection_sort(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i + 1, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = j
            values[i], values[pos] = values[pos], values[1]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    return dx * dy


def rect_sort(rectangles):
    dict = {}
    areas = []
    for rectangle in rectangles:
        dict[calc_area(rectangle)] = rectangle
        areas.append(calc_area(rectangle))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dict[areas[i]]


def star_find(filename):
    file = open(filename, "r")
    signals = file.read().split() # a list of strings (range)
    found = []
    for i in range(len(signals)):
        if (4000 =< signals[i] =< 5000):
            found.append(signals[i])
        if len(found) >= 5:
            break
        print(found)
        if len(found) != 5:
            print("we didn't find 5")
        else:
            print(found.append(signals[i]))





def main():
    is_in_binary(2, [4, 6, 7, 2, 5])
    selection_sort([4, 6, 7, 3, 2])
    star_find("signals.txt")

main()

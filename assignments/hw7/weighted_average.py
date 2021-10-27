"""
Name: Madeleine Ellegard
weighted_average.py

Problem: To compute the students weighted average

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with Laura
"""


def weighted_average(in_file_name, out_file_name):
    class_acc = 0
    class_size = 0
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w+")
    for line in infile:
        new_line = line.split(': ')
        numbers = new_line[1].split(" ")
        avg_acc = 0
        weight_acc = 0
        for i in range(0, len(numbers) - 1, 2):
            weight = int(numbers[i])
            score = int(numbers[i + 1])
            avg = weight * score
            avg_acc += avg
            weight_acc += weight
        if weight_acc > 100:
            outfile.write(str(new_line[0]) + "'s average: Error: The weights are more than 100." + "\n")
        elif weight_acc < 100:
            outfile.write(str(new_line[0]) + "'s average: Error: The weights are less than 100." + "\n")
        elif weight_acc == 100:
            class_size += 1
            class_acc += avg_acc
            div_avg_acc = avg_acc / 100
            outfile.write(str(new_line[0]) + "'s average: " + str(round(div_avg_acc, 1)) + "\n")
    class_avg = class_acc / 100
    outfile.write("Class average: " + str(round(class_avg / class_size, 1)))


if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")

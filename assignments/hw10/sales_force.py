"""
Name: Madeleine Ellegard
sales_force.py

Problem:

Certification of Authenticity:
I certify that this assignment is entirely my own work, but I discussed it with
"""
from sales_person import *


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        lines = file.readlines()
        for i in range(len(lines)):
            fields = lines[i].split(",")
            person = SalesPerson(fields[0], fields[1])
            sales = fields[2].split()
            for sale in sales:
                person.enter_sale(sale)
            self.sales_people.append(person)
        file.close()

    def quota_report(self, quota):
        report = []
        for i in range(len(self.sales_people)):
            report.append([self.sales_people[i].get_id(), self.sales_people[i].get_name(),
                           self.sales_people[i].total_sales(), self.sales_people[i].total_sales() > quota])

    def top_seller(self):
        top = self.sales_people[0]
        top_list = []
        for i in range(1, len(self.sales_people) - 1):
            if self.sales_people[i].compare_to(top) < 0:
                top = self.sales_people[i]
                top_list = []
            elif self.sales_people[i].compare_to(top) == 0:
                top_list.append(self.sales_people[i])
        top_list.append(top)

    def individual_sales(self, employee_id):
        return self.sales_people.append(employee_id)

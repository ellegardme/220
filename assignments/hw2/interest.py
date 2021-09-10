"""
Name: Madeleine Ellegard
interest.py

Problem: To compute the monthly  interest of a credit card statement

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    rate = eval(input("Enter in the annual interest rate: "))
    days = eval(input("Enter in the number of days in the billing cycle: "))
    previous_balance = eval(input("Enter in the your previous net balance: "))
    payment = eval(input("Enter in the payment amount: "))
    payment_day = eval(input("Enter that day of the billing cycle in which the payment was made: "))
    net_balance = previous_balance * days
    sub = days - payment_day
    net_pay = payment * sub
    total = net_balance - net_pay
    change = total / days
    month = rate / 12
    charge = (month * change) / 100
    print(round(charge, 2))


if __name__ == "__main__":
    main()

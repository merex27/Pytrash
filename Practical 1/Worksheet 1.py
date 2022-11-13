import sys

from operator import length_hint


# 1


def sayName():
    print("Igor")

# 2


def sayHello2():
    print("Hello\nWorld")

# 3


def euros2pounds():
    euros = float(input("Enter amount of Euros: "))
    if euros < 0:
        print("Value cant be negative.")
        sys.exit(0)

    pounds = round((euros / 1.17), 2)

    print(f"{euros} euros is {pounds} pounds.")

# 4


def sumDifference():
    first = float(input("Enter first number:"))
    second = float(input("Enter second number:"))
    sum = first + second
    difference = first - second

    print(f"The sum is: {sum} and the difference is: {difference}")

# 5


def changeCounter():
    one_p = int(input("Enter amount of one pence coins: "))
    two_p = int(input("Enter amount of two pence coins: "))
    three_p = int(input("Enter amount of three pence coins: "))
    if one_p < 0 or two_p < 0 or three_p < 0:
        print("Value cant be negative.")
        sys.exit(0)

    total = float((one_p * 1 + two_p * 2 + three_p * 3) / 100)

    print(f"You have: {total} pounds")

# 6


def tenHellos():
    for i in range(10):
        print("Hello world")

# 7


def countTo():
    number = int(input("Enter whole number: "))
    for i in range(1, number + 1):
        print(i)

# 8


def zoomZoom():
    zoomer = int(input("How many zooms?: "))
    for i in range(1, zoomer + 1):
        print("zoom", i)

# 9


def weightsTable():
    lst = list(range(0, 110, 10))
    for kg in lst:
        pounds = kg * 2.2
        print(f"{kg} kg is {pounds:.2f} pounds.")

# 10


def futureValue():
    amount = float(input("Enter initial investment : "))
    years = int(input("Enter number of years: "))
    if years < 0:
        print("Value cant be negative.")
        sys.exit(0)

    interest = 0.035

    print(f"\nAmount invested is: {amount}")

    for i in range(1, years + 1):
        amount = amount + (amount * interest)
        print(f"Year {i}: {amount:.2f}")
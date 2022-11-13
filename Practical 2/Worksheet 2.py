import math
import sys

from operator import length_hint

# 1


def circumferenceOfCircle():
    radius = float(input("Enter radius of a circle: "))
    if radius < 0:
        print("Value cant be negative.")
        sys.exit(0)
    radius = 2 * math.pi * radius

    print(f"The circumference of a circle is {radius}")

# 2


def areaOfCircle():
    radius = float(input("Enter radius of a circle: "))
    if radius < 0:
        print("Value cant be negative.")
        sys.exit(0)
    area = math.pi * radius ** 2

    print(f"Area of a circle is {area}")

# 3


def costPizza():
    diameter = float(input("Enter diameter of a math.pizza (cm): "))
    if diameter < 0:
        print("Value cant be negative")
        sys.exit(0)

    area = math.pi * (diameter / 2) ** 2
    cost = area * 1.5 / 100

    print(f"Pizza costs {cost:.2f} pounds.")

# 4


def slopeOfLine():
    x1 = float(input("Enter value of x1: "))
    x2 = float(input("Enter value of x2: "))
    y1 = float(input("Enter value of x1: "))
    y2 = float(input("Enter value of x1: "))
    slope = (y2 - y1) / (x2 - x1)

    print(f"The Slope of the line is {slope}")

# 5


def distanceBetweenPoints():
    x1 = float(input("Enter value of x1: "))
    x2 = float(input("Enter value of x2: "))
    y1 = float(input("Enter value of x1: "))
    y2 = float(input("Enter value of x1: "))
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2).real

    print(f"The Distance between points is {distance}")

# 5'


def distanceBetweenPointsV2():
    x1 = float(input("Enter value of x1: "))
    x2 = float(input("Enter value of x2: "))
    y1 = float(input("Enter value of x1: "))
    y2 = float(input("Enter value of x1: "))
    x = (x1, x2)
    y = (y1, y2)
    distance = math.dist(x, y)

    print(f"The distance between points is {distance}")

# 6


def travelStatistics():
    speed = float(input("Enter average speed (km/h): "))
    time = float(input("Enter duration of a travel (hours): "))
    if time < 0:
        print("Value cant be negative.")
        sys.exit(0)

    distance = speed * time
    fuel = distance / 5

    print(
        f"Traveled {distance} kilometers and used {fuel:.2f} liters of fuel.")

# 7


def sumOfSquares():
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i ** 2

    print(f"The sum of squares is: {sum}")

# 8


def averageOfNumbers():
    amount = int(input("Enter n: "))
    if amount <= 0:
        print("Value cant be negative or 0.")
        sys.exit(0)

    list = []
    for i in range(1, amount + 1):
        print("Enter number", i, end=" ")
        list.append(float(input()))
    average = (sum(list) / amount)

    print(f"The average of numbers is {average}")

# 9


def fibonacci():
    n = int(input("Enter n: "))
    if n <= 0:
        print("Value cant be negative or 0.")
        sys.exit(0)

    a = 0
    b = 1
    c = 0
    i = 0

    for i in range(1, n):
        c = a + b
        a = b
        b = c

    print(f"Term number {i} has value of {c}")

# 10
# Ghetto


def selectCoins():
    pence = int(input("Enter amount of pence: "))
    if pence < 0:
        print("Value cant be negative.")
        sys.exit(0)

    two_P = (pence // 200)
    pence = (pence % 200)

    one_P = (pence // 100)
    pence = (pence % 100)

    fifty_p = (pence // 50)
    pence = (pence % 50)

    twenty_p = (pence // 20)
    pence = (pence % 20)

    ten_p = (pence // 10)
    pence = (pence % 10)

    five_p = (pence // 5)
    pence = (pence % 5)

    two_p = (pence // 2)
    pence = (pence % 2)

    one_p = (pence // 1)
    pence = (pence % 1)

    print(f"{two_P} Two pounds\n{one_P} One pounds\n{fifty_p} Fifty pence\n{twenty_p} Twenty pence\n{ten_p} Ten pence\n{five_p} Five pence\n{two_p} Two pence\n{one_p} One pence\n")
import os
import re
import string
import sys

from operator import length_hint
from graphics import *

# 1


def personalGreeting():
    name = input(str("Enter your name. "))

    print(f"Hello {name}, nice to see you!")

# 2


def formalName():
    given_name = input(str("Enter your given name. "))
    family_name = input(str("Enter your family name. "))
    given_name = given_name[0].upper()

    print(f"{given_name}. {family_name}")

# 3


def kilos2pounds():
    lst = list(range(0, 110, 10))
    for kg in lst:
        pounds = float(kg * 2.2)
        print(f"{kg}kg is {pounds:.1f}lbs")


# 4

def generateEmail():
    given_name = input("En/ter your given name: ")
    familyNam = input("Enter your family name: ")
    year = input("Enter when you started uni (YYYY): ")

    print(
        f"{familyNam[:4].lower()}.{given_name[:1].lower()}.{year[2:4]}@myport.ac.uk")

# 5


def gradeTest():
    grade = "FFFFCCBBAAA"
    score = int(input("Enter your score: "))
    if score < 0 or score > 10:
        print("Please enter a value between 0 and 10.")
        sys.exit()

    print(f"Your grade is {grade[score]}")

# 5 '


def gradeTest():
    score = input(str("What score did you got (value between 0 and 10): "))
    if score < 0 or score > 10:
        print("Please enter a value between 0 and 10.")
        sys.exit()

    match score:
        case "10" | "9" | "8":
            print("A")
        case "7" | "6":
            print("B")
        case "5" | "4":
            print("C")
        case "3" | "2" | "1" | "0":
            print("F")

# 6


def graphicLetters():
    word = input("Enter a word: ")

    win = GraphWin("Letters", 500, 500)
    win.setCoords(0, 0, 500, 500)

    for i in range(len(word)):
        click = win.getMouse()
        letter = Text(click, word[i])
        letter.setSize(30)
        letter.draw(win)

    win.getMouse()

# 7


def singASong():
    word = input("Enter a word: ")
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    if rows < 1 or columns < 1:
        print("Value can not be negative.")
        sys.exit()

    for i in range(rows):
        for j in range(columns):
            print(f"{word}", end=" ")
        print("")

# 8


def exchangeTable():
    euros = []
    for i in range(0, 20):
        euros.append(i)
    pounds = []
    for euro in euros:
        pounds = euro * 0.86
        print(f"{euro:>2} EUR is {pounds:>5.2f} GBP")

# 9


def makeInitialism():
    phrase = input("Enter a phrase: ")

    words = phrase.split()
    for word in words:
        print(f"{word[0].upper()}", end="")
    print(".")

# 10


def nameToNumber():
    name = input("Enter your name: ")

    numbers = [0] + list(string.ascii_lowercase)
    print(numbers)
    sum = 0
    for letter in name:
        sum = sum + numbers.index(letter)
    print(f"You name is worth {sum}")

# 11


def fileInCaps():
    os.chdir("Practical 4")
    file = open(name, "r")

    name = input("Enter a name of the file: ")

    for line in file:
        print(line.upper(), end="")
    file.close()

# 12


def rainfallChart():
    os.chdir("Practical 4")
    file = open("rainfall.txt", "r")

    cities = []
    numbers = []
    for line in file:
        for city in (re.findall(r"[A-Z][a-z]+", line)):
            cities.append(city)
        for number in (re.findall(r"\d+", line)):
            numbers.append(int(number))
    file.close()

    for i in range(len(cities)):
        drops = numbers[i]
        print(f"{cities[i]:12}: {'*' * drops}")

# (with graphical interface)


def graphicalRainfallChart():
    os.chdir("Practical 4")
    file = open("rainfall.txt", "r")

    cities = []
    numbers = []
    for line in file:
        for city in (re.findall(r"[A-Z][a-z]+", line)):
            cities.append(city)
        for number in (re.findall(r"\d+", line)):
            numbers.append(int(number))
    file.close()

    win = GraphWin("Rainfall", 1000, 500)
    win.setCoords(0, 0, 500, 500)

    x_axis = Line(Point(50, 50), Point(475, 50))
    x_axis.draw(win)

    period_x = 400 / 9
    for i in range(9):
        x = 90 + period_x * i
        x_line = Line(Point(x, 50), Point(x, 40))
        x_line.draw(win)
        x_text = Text(Point(x, 30), cities[i])
        x_text.setSize(10)
        x_text.draw(win)

    y_axis = Line(Point(50, 50), Point(50, 425))
    y_axis.draw(win)

    periodY = 500 / 7
    for i in range(6):
        y = 50 + (periodY * i)
        y_line = Line(Point(50, y), Point(40, y))
        y_line.draw(win)
        y_text = Text(Point(25, y), i * 10)
        y_text.draw(win)

    for i in range(9):
        height = 50 + (numbers[i] / 10) * periodY
        bl = 80 + period_x * i
        br = 100 + period_x * i
        bar = Rectangle(Point(bl, 50), Point(br, height))
        bar.setFill("#1974D2")
        bar.draw(win)

    win.getMouse()
    
# 13


def rainfallInInches():
    os.chdir("Practical 4")
    file = open("rainfall.txt", "r")

    cities = []
    millimeters = []
    inches = []
    for line in file:
        for city in (re.findall(r"[A-Z][a-z]+", line)):
            cities.append(city)
        for number in (re.findall(r"\d+", line)):
            millimeters.append(int(number))
    file.close()

    file = open("fall.txt", "w")
    for i in range(len(cities)):
        millimeter = millimeters[i]
        inches.append(millimeter / 25.4)
        print(f"{cities[i]} {inches[i]:.2f}", file=file)
    file.close()

# 14


def wc():
    os.chdir("Practical 4")
    name = input("Enter a name of the file: ")
    data = open(name).read()

    lines = re.findall(r"\n", data)
    words = re.findall(r"[A-z]+", data)
    numbers = re.findall(r"[+-]?([0-9]*[.])?[0-9]+", data)
    characters = re.findall(r".", data)

    print(f"Lines: {len(lines) + 1}\nWords: {len(words) + len(numbers)}\nCharacters: {len(characters)}")
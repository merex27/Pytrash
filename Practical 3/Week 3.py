import math
import sys

from operator import length_hint
from graphics import *

# 1


def drawStickFigure():
    win = GraphWin("Stick figure", 250, 250)
    win.setCoords(0, 0, 200, 200)

    head = Circle(Point(100, 150), 20)
    body = Line(Point(100, 130), Point(100, 80))
    arm_l = Line(Point(100, 120), Point(80, 95))
    arm_r = Line(Point(100, 120), Point(120, 95))
    leg_l = Line(Point(100, 80), Point(80, 40))
    leg_r = Line(Point(100, 80), Point(120, 40))

    head.draw(win)
    body.draw(win)
    arm_l.draw(win)
    arm_r.draw(win)
    leg_l.draw(win)
    leg_r.draw(win)

    win.getMouse()

# 2


def drawCircle():
    radius = int(input("Enter radius: "))
    if radius < 0:
        print("Value can not be negative.")
        sys.exit(0)

    window = radius * 1.2
    win = GraphWin("Circle", window, window)
    win.setCoords(0, 0, window * 2, window * 2)

    circle = Circle(Point(window, window), radius)
    circle.draw(win)
    circle.setWidth(1)

    win.getMouse()

# 3


def drawArcheryTarget():
    radius = int(input("Enter radius: "))

    window = radius * 1.2
    win = GraphWin("Target", window, window)
    win.setCoords(0, 0, window * 2, window * 2)

    blue = Circle(Point(window, window), radius)
    blue.draw(win)
    blue.setWidth(1)
    blue.setFill("#1974D2")
    blue.setWidth(1)

    red = Circle(Point(window, window), radius / 3 * 2)
    red.draw(win)
    red.setFill("#FD3A4A")
    red.setWidth(1)

    yellow = Circle(Point(window, window), radius / 3)
    yellow.draw(win)
    yellow.setFill("#FFF44F")
    yellow.setWidth(1)

    win.getMouse()

# 4


def drawRectangle():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    if height >= 200 or width >= 200:
        print("Please enter a number below 200.")
        sys.exit(0)

    if height < 0 or width < 0:
        print("Value can not be negative.")
        sys.exit(0)

    win = GraphWin("Rectangle", 200, 200)
    win.setCoords(0, 0, 200, 200)

    rectangle = Rectangle(Point(100 - width / 2, 100 - height / 2),
                          Point(100 + width / 2, 100 + height / 2))
    rectangle.setFill("#000000")
    rectangle.draw(win)

    win.getMouse()

# 5


def blueCircle():
    radius = 50
    win = GraphWin("Blue circle", 500, 500)
    win.setCoords(0, 0, 500, 500)

    centre = win.getMouse()
    circle = Circle(centre, radius)
    circle.setFill("#1974D2")
    circle.draw(win)

    win.getMouse()

# 6


def drawLine():
    win = GraphWin("Draw line(s)", 500, 500)
    win.setCoords(0, 0, 500, 500)

    for i in range(10):
        print("Choose starting point.")
        p1 = win.getMouse()
        print("Choose ending point.")
        p2 = win.getMouse()

        line = Line(p1, p2)
        line.draw(win)

    win.getMouse()

# 7


def tenStrings():
    win = GraphWin("Ten strings", 500, 500)
    win.setCoords(0, 0, 500, 500)

    message = Text(Point(250, 475), "Enter a string and click.")
    message.draw(win)
    textbox = Entry(Point(250, 450), 15)
    textbox.draw(win)

    for i in range(10):
        location = win.getMouse()
        text = Text(location, textbox.getText())
        text.draw(win)

    win.getMouse()

# 8


def tenColouredRectangles():
    win = GraphWin("Ten coloured rectangles", 500, 500)
    win.setCoords(0, 0, 500, 500)

    message = Text(Point(250, 475),
                   "Type a color of a rectangle and select two points.")
    message.draw(win)
    textbox = Entry(Point(250, 450), 15)
    textbox.setText("blue")
    textbox.draw(win)

    for i in range(10):
        p1 = win.getMouse()
        p2 = win.getMouse()
        rectangle = Rectangle(p1, p2)
        rectangle.setFill(textbox.getText())
        rectangle.draw(win)

    win.getMouse()

# 9


def fiveClickStickFigure():
    win = GraphWin("Five click stick figure", 500, 500)
    win.setCoords(0, 0, 500, 500)

    print("Click 2 times to select centre of a head and radius.")
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)
    head = Circle(p1, radius)
    head.draw(win)

    print("Click to select length of body.")
    p3 = win.getMouse()
    pelvis = Point(p1.getX(), p3.getY())
    body = Line(Point(p1.getX(), p1.getY() - radius), pelvis)
    body.draw(win)

    print("Click to select height and length of arms.")
    p4 = win.getMouse()
    arms_length = p1.getX() - p4.getX()
    arms = Line(p4, Point(p1.getX() + arms_length, p4.getY()))
    arms.draw(win)

    print("Click to select where to place a foot.")
    p5 = win.getMouse()
    foot_length = p1.getX() - p5.getX()
    foot_l = Line(p5, pelvis)
    foot_r = Line(Point(pelvis.getX() + foot_length, p5.getY()), pelvis)
    foot_l.draw(win)
    foot_r.draw(win)

    win.getMouse()

# 10


def plotRainfall():
    win = GraphWin("Rainfall", 500, 500)
    win.setCoords(0, 0, 500, 500)

    message = Text(Point(
        250, 475), "Enter amount of rainfall for each day (in mm) and click mouse to enter.")
    message.draw(win)
    textbox = Entry(Point(250, 450), 15)
    textbox.draw(win)

    x_axis = Line(Point(50, 50), Point(475, 50))
    x_axis.draw(win)

    period_x = 400 / 7
    for i in range(7):
        x = 90 + period_x * i
        x_line = Line(Point(x, 50), Point(x, 40))
        x_line.draw(win)
        x_text = Text(Point(x, 30), i + 1)
        x_text.draw(win)

    y_axis = Line(Point(50, 50), Point(50, 425))
    y_axis.draw(win)

    periodY = 500 / 7
    for i in range(6):
        y = 50 + (periodY * i)
        y_line = Line(Point(50, y), Point(40, y))
        y_line.draw(win)
        y_text = Text(Point(25, y), i * 100)
        y_text.draw(win)

    for i in range(7):
        win.getMouse()
        height = 50 + (int(textbox.getText()) / 100) * periodY
        bl = 80 + period_x * i
        br = 100 + period_x * i
        bar = Rectangle(Point(bl, 50), Point(br, height))
        bar.setFill("#1974D2")
        bar.draw(win)

    win.getMouse()
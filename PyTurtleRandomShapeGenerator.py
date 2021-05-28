import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
screen.colormode(255)


class Bob:
    def __init__(self, name):
        self.name = name
        self.name = turtle.Turtle()
        self.name.speed(50)
        self.name.pu()


    def circle(self, color, radius, x, y):
        self.name.goto(x, y)
        self.name.pd()
        self.name.fillcolor(color)
        self.name.begin_fill()
        self.name.circle(radius)
        self.name.end_fill()
        self.name.pu()
        self.name.home()


    def square(self, color, size, x, y):
        self.name.goto(x, y)
        self.name.pd()
        self.name.fillcolor(color)
        self.name.begin_fill()
        for i in range(0, 4):
            self.name.fd(size)
            self.name.rt(90)
        self.name.end_fill()
        self.name.pu()
        self.name.home()


    def triangle(self, color, size, x, y):
        self.name.goto(x, y)
        self.name.pd()
        self.name.fillcolor(color)
        self.name.begin_fill()
        for i in range(0, 3):
            self.name.fd(size)
            self.name.rt(120)
        self.name.end_fill()
        self.name.pu()
        self.name.home()


    def star(self, color, size, x, y):
        self.name.goto(x, y)
        self.name.pd()
        self.name.fillcolor(color)
        self.name.begin_fill()
        for i in range(0, 5):
            self.name.fd(size)
            self.name.rt(144)
        self.name.end_fill()
        self.name.pu()
        self.name.home()


bob1 = Bob('bob')
for i in range(0, random.randint(50, 100)):
    a = random.randint(0, 3)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if a == 0:
        bob1.circle((r, g, b), random.randint(50, 150), random.randint(-1000, 1000), random.randint(-500, 500))
    elif a == 1:
        bob1.square((r, g, b), random.randint(50, 150), random.randint(-1000, 1000), random.randint(-500, 500))
    elif a == 2:
        bob1.star((r, g, b), random.randint(50, 150), random.randint(-1000, 1000), random.randint(-500, 500))
    else:
        bob1.triangle((r, g, b), random.randint(50, 150), random.randint(-1000, 1000), random.randint(-500, 500))

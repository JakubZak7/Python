import turtle

pen = turtle.Turtle()
pen.speed(5)

def draw_square(length):

    for _ in range(4):
        pen.forward(length)
        pen.right(90)

    pen.penup()
    pen.goto(-150,100)
    pen.pendown()

def draw_triangle(lenght):
    for _ in range(3):
        pen.forward(lenght)
        pen.right(120)

    pen.penup()
    pen.goto(-250, 100)
    pen.pendown()

def draw_rectangle(lenght_a,lenght_b):
    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)

    pen.penup()
    pen.goto(-450, 100)
    pen.pendown()

pen.hideturtle()
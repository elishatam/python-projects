import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(3):
        some_turtle.forward(100)
        some_turtle.right(120)


def draw_shape():
    window = turtle.Screen()
    window.bgcolor("grey")

    """turtle = Python standard library
    Turtle = class. = Neatly packaged box that puts things together very well.
    turtle.Turtle() is running a function "def __init__" which creates space in memory for a new instance of Turtle (brad)
    brad can now access all of the other methods inside class Turtle (i.e. def forward, def right)
    """
    #Create turtle Brad - Draw a Square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    draw_square(brad)

    #Create turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.color("red")
    angie.circle(100)

    #Create turtle Beth - Draws a triangle
    beth = turtle.Turtle()
    draw_triangle(beth)

    window.exitonclick()

draw_shape()
"""Draw a cat in a field."""


__author__ = "730569615"

import random
from turtle import Turtle, colormode, tracer, update, Screen, done 
colormode(255)
screen = Screen()
screen.setup(750, 750)


def main() -> None:
    """The entrypoint of my scene."""
    # TODO: Declare your Turtle variable(s) here.
    # TODO: Call the procedures you define and pass your Turtle(s) as an argument.

    tracer(0, 0)  # Disable delay in tracing

    tsunami: Turtle = Turtle()
    tsunami.speed(0)

    sky = 200
    y = 370
    for i in range(35):
        grass_row(tsunami, y, (90, 120, sky))
        sky -= 2
        y -= 15

    grass = 230
    y = -370
    for i in range(20):
        grass_row(tsunami, y, (90, grass, 5))
        grass -= 5
        y += 15

    draw_tsunami(tsunami, 100, -150)

    """Uses random to draw clouds at random locations in the sky within a given range."""
    cloud(tsunami, random.randrange(-350, 350), random.randrange(100, 250))
    cloud(tsunami, random.randrange(-350, 350), random.randrange(100, 250))
    cloud(tsunami, random.randrange(-350, 350), random.randrange(100, 250))
    cloud(tsunami, random.randrange(-350, 350), random.randrange(100, 250))
    cloud(tsunami, random.randrange(-350, 350), random.randrange(100, 250))
    cloud(tsunami, random.randrange(-350, 350), random.randrange(100, 250))

    update()  # Now update the rendering
    done()


def triangle(turtle: Turtle, x: float, y: float, starth: float, length: float, color: tuple[float, float, float], fill: bool) -> None:
    """Draws a triangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(starth)
    turtle.color(color)
    turtle.pendown()
    if fill is True:
        turtle.begin_fill()
    i = 0
    while i < 3:
        turtle.forward(length)
        turtle.right(120)
        i += 1
    if fill is True:
        turtle.end_fill()


def circle_set(turtle: Turtle, x: float, y: float, radius: float, color: tuple[float, float, float], fill: bool) -> None:
    """Draws a triangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.pendown()
    if fill is True:
        turtle.begin_fill()
    turtle.circle(radius)
    if fill is True:
        turtle.end_fill()


def draw_tsunami(turtle: Turtle, x: float, y: float) -> None:
    """Draw a picture of Tsunami. This function is broken down into subfunctions."""
    triangle(turtle, x + 25, y + 75, 30, 20, (0, 0, 0), True)
    triangle(turtle, x - 25, y + 75, 30 - 180, 20, (0, 0, 0), True)
    triangle(turtle, x + 30, y + 70, 30, 10, (255, 192, 203), True)
    triangle(turtle, x - 30, y + 70, 30 - 180, 10, (255, 192, 203), True)
    triangle(turtle, x - 5, y + 30, 0, 7, (255, 192, 203), True)
    circle_set(turtle, x, y, 45, (0, 0, 0), True)
    circle_set(turtle, x, y - 125, 65, (0, 0, 0), True)
    circle_set(turtle, x + 30, y - 130, 15, (0, 0, 0), True)
    circle_set(turtle, x - 30, y - 130, 15, (0, 0, 0), True)


def grass_row(turtle: Turtle, y: float, color: tuple[float, float, float]) -> None:
    """Draw a row of grass."""
    x = -360
    for i in range(100):
        triangle(turtle, x, y, 180, 30, color, True)
        x += 10


def cloud(turtle: Turtle, x: float, y: float) -> None:
    """Draw a cloud."""
    a = x
    b = x
    for i in range(5):
        circle_set(turtle, a, y, 25, (255, 255, 255), True)
        a += 15
    y += 15
    for i in range(3):
        circle_set(turtle, b + 15, y, 25, (255, 255, 255), True)
        b += 15
    y -= 30
    for i in range(3):
        circle_set(turtle, x + 15, y, 25, (255, 255, 255), True)
        x += 15


if __name__ == "__main__":
    main()
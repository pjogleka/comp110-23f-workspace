from turtle import Turtle, colormode, done
colormode(255)

"""
leo: Turtle = Turtle()
leo.penup()
leo.color(0, 100, 0)
leo.goto(-50, 50)
leo.pendown()
leo.speed(10)
leo.begin_fill()
for i in range(3):
    leo.forward(100)
    leo.right(120)
leo.end_fill()
done()
"""

bob: Turtle = Turtle()

bob.color(0,0,0)
bob.penup()
bob.goto(-50, 50)
bob.pendown()
bob.speed(20)
side = 100
for i in range(40):
    side *= .97
    bob.forward(side)
    bob.right(122)
done()


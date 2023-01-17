from random import randint
import turtle


def mountaint(length, t):
    angle = randint(50, 80)
    len = randint(40, 100)
    if t.xcor() < 500:
        t.left(angle)
        t.forward(4*length)
        t.right(2*angle)
        t.forward(length/2)
        t.right(180 - 2*angle)
        t.forward(length/2)
        t.right(2*angle)
        t.forward(length/2)
        t.right(180 - 2*angle)
        t.forward(length/2)
        t.right(2*angle)
        t.forward(4*length)
        t.left(angle)
        mountaint(len, t)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.up()
    t.goto(-470, -400)
    t.down()
    t.color("black", "black")
    mountaint(120, t)
    myWin.exitonclick()


main()

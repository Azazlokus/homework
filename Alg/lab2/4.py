import turtle


def mink(length, n, t):
    if n == 0:
        t.forward(length)
    else:
        mink(length, n-1, t)
        t.left(90)
        mink(length, n-1, t)
        t.right(90)
        mink(length, n-1, t)
        t.right(90)
        mink(length, n-1, t)
        mink(length, n-1, t)
        mink(length, n-1, t)
        t.left(90)
        mink(length, n-1, t)
        t.left(90)
        mink(length, n-1, t)
        t.right(90)
        mink(length, n-1, t)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    mink(10, 3, t)
    myWin.exitonclick()


main()

import turtle


def tree(branchLen, t, width):
    t.width(width)
    if branchLen > 5 and width > 0:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t, width - 1)
        t.left(40)
        tree(branchLen - 15, t, width - 1)
        t.right(20)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(100, t, 5)
    myWin.exitonclick()


main()

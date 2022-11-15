import turtle


def tree(branchLen, t, width):
    t.width(width)
    if branchLen > 5 and width > 0:
        if branchLen - 15 <= 5 or width == 1:
            t.color("green")
        t.forward(branchLen)
        t.right(20)
        tree(branchLen - 15, t, width - 1)
        t.left(40)
        tree(branchLen - 15, t, width - 1)
        t.right(20)
        t.backward(branchLen)
        t.color("brown")


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(100, t, 7)
    myWin.exitonclick()


main()

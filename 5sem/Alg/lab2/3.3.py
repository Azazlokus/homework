import turtle
from random import randint


def tree(branchLen, t, width):
	t.width(width)
	angle = randint(15, 40)
	if branchLen > 5 and width > 0:
		if branchLen - 15 <= 5 or width == 1:
			t.color("green")
		t.forward(branchLen)
		t.right(angle)
		tree(branchLen - 15, t, width - 1)
		t.left(2*angle)
		tree(branchLen - 15, t, width - 1)
		t.right(angle)
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
	tree(90, t, 7)
	myWin.exitonclick()


main()

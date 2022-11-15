import sympy as sp
from math import tan


def f(x):
	rez = tan(x**2)/(x + 1)
	return rez


def diff(i, z):
	x = sp.symbols('x')
	func = sp.tan(x**2)/(x + 1)
	yprime = sp.diff(func, x, z)
	yprime = yprime.subs({x: i})
	return yprime.n()


def get_max(z):
	lst = []
	for i in x:
		lst.append(diff(i, z))
	return max(lst)


def trap(y):
	rez = (y[0] + y[-1])/2
	for i in range(1, len(y)-1):
		rez += y[i]
	rez *= h
	return rez

def simp(y):
	rez = y[0] + y[-1]
	for i in range(1, len(y)-1):
		if (i % 2 == 0):
			rez += 2*y[i]
		else:
			rez += 4*y[i]
	rez *= h/3
	return rez

def drob(y):
	rez = y[0] + y[-1]
	for i in range(1, len(y)-1):
		if (i % 3 == 0):
			rez += 2*y[i]
		else:
			rez += 3*y[i]
	rez *= 3*h/8
	return rez

a, b = 0, 1

y_text = "tg(x^2)/(x+1)"

n = int(input("n: "))
h = (b-a)/n

k = a
x = [a]
for i in range(1, n):
	k += h
	x.append(k)
x.append(b)
y_rez = [f(i) for i in x]

rez_trap = trap(y_rez)
r_trap = -(b-a)/12 * (h**2) * get_max(2)
print("y = ", y_text, " [", a, ", ", b, "]", sep="")
print("Трапеция")
print("y =", rez_trap, "r =", r_trap)

if (n % 2 == 0):
	rez_simp = simp(y_rez)
	r_simp = -(b-a)/180 * (h**4) * get_max(4)
	print("Симпсон")
	print("y =", rez_simp, "r =", r_simp)

if (n % 3 == 0):
	rez_drob = drob(y_rez)
	r_drob = -(b-a)/80 * (h**4) * get_max(4)
	print("3/8")
	print("y =", rez_drob, "r =", r_drob)

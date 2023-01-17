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


a, b = 0, 1
n = 30
h = (b-a)/n
k = a
x = [a]
for i in range(1, n):
	k += h
	x.append(k)
x.append(b)
y_rez = [f(i) for i in x]
trap_h = trap(y_rez)
n *= 2
h = (b-a)/n
k = a
x = [a]
for i in range(1, n):
	k += h
	x.append(k)
x.append(b)
y_rez = [f(i) for i in x]
trap_h_double = trap(y_rez)
eps = 1e-5
n = int(n / 2)
while (abs(trap_h_double - trap_h) >= eps):
	n += 1
	h = (b-a)/n
	k = a
	x = [a]
	for i in range(1, n):
		k += h
		x.append(k)
	x.append(b)
	y_rez = [f(i) for i in x]
	trap_h = trap(y_rez)

	n *= 2
	h = (b-a)/n
	k = a
	x = [a]
	for i in range(1, n):
		k += h
		x.append(k)
	x.append(b)
	y_rez = [f(i) for i in x]
	trap_h_double = trap(y_rez)
	n = int(n / 2)

print(trap_h, trap_h_double)
print(n, 2*n)
print(abs(trap_h_double - trap_h))






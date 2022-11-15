from math import sin
import matplotlib.pyplot as plt
import sympy as sp


def L3(x):
	rez_l = []
	for i in range(6):
		rez = 1
		for j in range(6):
			if i != j:
				rez *= (x-x_lst[j])/(x_lst[i]-x_lst[j])
		rez *= y(x_lst[i])
		rez_l.append(rez)
	return sum(rez_l)


def diff4(i):
	x = sp.symbols('x')
	func = sp.sin(x)**2 + sp.sin(x) + x
	yprime = sp.diff(func, x, 4)
	yprime = yprime.subs({x: i})
	return yprime.n()


def y(x): return sin(x)**2 + sin(x) + x


length = [i/10 for i in range(-20, 31)]

x_lst = [length[0], length[10], length[20], length[30], length[40], length[-1]]
y_rez = [y(x) for x in length]


interp = []
for i in length:
	interp.append(L3(i))

R_teor = []
for x in length:
	R_teor.append(
		abs(diff4(x) / 24 * (x-x_lst[0]) * (x-x_lst[1]) * (x-x_lst[2]) * (x-x_lst[3]) * (x-x_lst[4]) * (x-x_lst[5])))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(length, y_rez)
plt.plot(length, interp)
plt.minorticks_on()
plt.grid(True)
plt.subplot(1, 2, 2)
plt.plot(length, R_teor)
plt.minorticks_on()
plt.grid(True)
plt.show()
plt.close()

from math import sin
import matplotlib.pyplot as plt


def cube(x: list, j: int):
	rez = []
	for i in range(10):
		val = ai[j+1] + bi[j]*(x[-1]-x[i]) +(ci[j+1]*(x[-1]-x[i])**2)/2 + (di[j]*(x[-1] - x[i])**3)/6
		rez.append(val)
	return rez


def y(x): return sin(x)**2 + sin(x) + x


length = [i/1000 for i in range(-2000, 2001, 50)]
x_lst = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
y_rez = [y(x) for x in length]
index_count = len(x_lst)

h = x_lst[1] - x_lst[0]
alpha, beta, gamma = h, 4*h, h

ai = [y(x) for x in x_lst]

fii = []
for i in range(1, index_count-1):
	rez = 6 * ((ai[i+1] - ai[i])/h - (ai[i]-ai[i-1])/h)
	fii.append(rez)

pi, qi = [0], [0]
for i in range(1, index_count-1):
	rez = -gamma/(beta + alpha * pi[i-1])
	pi.append(rez)
	rez = (fii[i-1] - alpha*qi[i-1])/(beta+alpha*pi[i-1])
	qi.append(rez)

ci = [0]
j = 0
for i in range(index_count-1, 1, -1):
	rez = pi[i-1] * ci[j]+ qi[i-1]
	ci.append(rez)
	j += 1
ci.append(0)
ci.reverse()

di = []
for i in range(1, index_count):
	rez = (ci[i-1]-ci[i])/h
	di.append(rez)

bi = []
for i in range(1, index_count):
	rez = (ai[i-1]-ai[i])/h - ci[i]*h/2 - (ci[i-1]-ci[i])*h/6
	bi.append(rez)

interp = []
j = 0
for i in range(len(x_lst)-1):
	x = length[i*10:i*10+11]
	interp += cube(x, j)
	j += 1
interp += [ai[-1]]

R_prac = []
for i in range(len(interp)):
    R_prac.append(abs(y_rez[i] - interp[i]))
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(length, y_rez, color="blue")
plt.plot(length, interp, color="red", linewidth=1)
plt.grid(True)
plt.minorticks_on()
plt.subplot(1, 2, 2)
plt.plot(length, R_prac)
plt.grid(True)
plt.minorticks_on()
plt.show()
plt.close()


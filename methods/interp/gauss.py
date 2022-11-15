from math import sin
import matplotlib.pyplot as plt


def gauss(x):
    t = (x - x_lst[0])/h
    rez = y_rez[0] + delta_y0 * t + delta2_y0*t*(t-1)/2
    return rez


y = lambda x: sin(x)**2 + sin(x) + x


length = [i/10 for i in range(-20, 1)]
x_lst = [length[0], length[10], length[-1]]
y_rez = [y(x) for x in length]

h = abs(x_lst[0] - x_lst[1])
delta_y0 = y_rez[10] - y_rez[0]
delta__y1 = y_rez[-1] - y_rez[10]
delta2_y0 = delta__y1 - delta_y0


interp = []
for x in length:
    interp.append(gauss(x))

R_prac = []
for i in range(len(interp)):
    R_prac.append(abs(y_rez[i] - interp[i]))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(length, y_rez)
plt.plot(length, interp)
plt.grid(True)
plt.minorticks_on()
plt.subplot(1, 2, 2)
plt.plot(length, R_prac)
plt.grid(True)
plt.minorticks_on()
plt.show()
plt.close()

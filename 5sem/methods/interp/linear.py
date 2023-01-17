from math import sin
import matplotlib.pyplot as plt


def linear(x:list, y:list):
	rez = []
	for i in range(10):
		val = y[-1] + (x[-1]-x[i])*(y[0]-y[-1])/(x[-1]-x[0])
		rez.append(val)
	return rez


	

def y(x): return sin(x)**2 + sin(x) + x


length = [i/1000 for i in range(-2000, 2001, 50)]
x_lst = [-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2]
y_rez = [y(x) for x in length]
interp = []

for i in range(len(x_lst)-1):
	y = y_rez[i*10:i*10+11]
	x = length[i*10:i*10+11]
	interp += linear(x, y)
interp += [y[-1] + (x[-1]-x[-1])*(y[0]-y[-1])/(x[-1]-x[0])]

	
    
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

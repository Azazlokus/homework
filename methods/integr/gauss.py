from math import tan


def f(x):
	rez = tan(x**2)/(x + 1)
	return rez

def gauss():
	rez = 0
	for i in range(n):
		rez += A[i]*y_rez[i]
	rez *= (b-a)/2
	return rez

a, b = 0, 1

y_text = "tg(x^2)/(x+1)"

n = 7

t1, t7 = -0.94910791, 0.94910791
t2, t6 = -0.74153119, 0.74153119
t3, t5 = -0.40584515, 0.40584515
t4 = 0
t = [t1, t2, t3, t4, t5, t6, t7]
A1 = A7 = 0.12948496
A2 = A6 = 0.27970540
A3 = A5 = 0.38183006
A4 = 0.41795918
A = [A1, A2, A3, A4, A5, A6, A7]

x = []
for i in range(n):
	temp = (b+a)/2 + (b-a)/2*t[i]
	x.append(temp)

y_rez = [f(i) for i in x]

rez_gauss = gauss()
print("y = ", y_text, " [", a, ", ", b, "]", sep="")
print("Гаусс")
print("y =", rez_gauss)



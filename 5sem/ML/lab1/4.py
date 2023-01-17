import math
import matplotlib.pyplot as plt

x=[]
for i in range(-400, 400):
	x.append(i/10)
y = []
for i in x:
	y.append(math.log((i*i+1)*math.exp(-(abs(i)/10)), (1+math.tan(1/(1+math.sin(i)**2)))))
plt.plot(x, y)
plt.grid(True)
plt.show()
plt.close()

from cProfile import label
import matplotlib.pyplot as plt
import numpy as np


T1 = lambda N: N*N-N-10
T2 = lambda N: 4*N+40

x = np.linspace(-10, 10)
plt.plot(x, T1(x), label="T1")
plt.plot(x, T2(x), label="T2")
plt.grid(True)
plt.legend()
plt.show()
plt.close()


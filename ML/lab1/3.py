import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-7, 7, 20)
y = lambda x: x*x-x-6
plt.plot(x, y(x))
plt.xticks([i for i in range(-7, 8)])
plt.grid(True)
plt.show()
plt.close()

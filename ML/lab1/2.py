import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, AutoMinorLocator
import numpy as np


x = np.linspace(1, 4, 10)
y = lambda x: np.log(x)
plt.plot(x, y(x), color="blue", label="Синяя линия")

x = np.linspace(0, 4)
y = lambda x: np.sin(x)+2.5
plt.plot(x, y(x), color="red", label="Красная линия")

x = np.linspace(0, 2, num=10)
y = lambda x: x*x
plt.scatter(x, y(x))

plt.subplot().xaxis.set_minor_locator(AutoMinorLocator())
plt.subplot().xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))
plt.tick_params(axis="both", which="minor", labelcolor="grey", labelsize=6)
plt.xticks([i for i in range(0, 5)])
plt.yticks([i for i in range(0, 5)])

plt.grid(True, linestyle="--")
plt.title("Элементы изображения")
plt.xlabel("Подпись оси ОХ")
plt.ylabel("Подпись оси OY")
plt.legend()

plt.show()
plt.close()

import matplotlib.pyplot as plt
import numpy as np


dates = ["2016-10-03", "2016-10-04", "2016-10-05", "2016-10-06", "2016-10-07"]
scores = [772.5, 776.42, 776.49, 776.85, 775.1]
plt.subplot().spines["left"].set_color("red")
plt.subplot().spines["top"].set_color("red")
plt.plot(dates, scores, color="red", marker="o")
plt.minorticks_on()
plt.grid(True, which="major", color="red")
plt.grid(True, which="minor", linestyle="--")
plt.yticks([i for i in np.arange(772.5, 777.1, 0.5)])
plt.title("Closing stock value of Alphabet Inc.")
plt.xlabel("Date")
plt.ylabel("Closing value")
plt.show()
plt.close()

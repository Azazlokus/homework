import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


scores_bar = [0.29, 0.02, 0.18, 0.27, 0.08]
tick_bar = [1.65, 2.75, 3.85, 4.95, 6.05]
plt.bar(tick_bar, scores_bar, 1.1, color="pink")

scores_plot = [0.0015, 0.0065, 0.01, 0.015, 0.02, 0.05, 0.085, 0.15, 0.18, 0.12,
               0.07, 0.1, 0.18, 0.24, 0.25, 0.24, 0.18, 0.08, 0.035, 0.015, 0.009, 0.007, 0.005]
tick_plot = [-1, -0.5, -0.3, -0.1, 0, 0.45, 0.75, 1.1, 1.65, 2.2,
             2.75, 3.3, 3.95, 4.4, 4.7, 4.95, 5.5, 6.1, 6.6, 7.1, 7.65, 8, 8.2]
y_line = interp1d(tick_plot, scores_plot, kind="cubic")
x_line = np.linspace(tick_plot[0], tick_plot[-1], num=100, endpoint=True)
plt.plot(x_line, y_line(x_line), color="red")

plt.xlabel("petal_length")
plt.xticks([i*2 for i in range(5)])
plt.show()
plt.close()

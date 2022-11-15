import matplotlib.pyplot as plt


plt.title("Display marker")
plt.plot([1, 4, 5, 6, 7], [2, 6, 3, 6, 3], color="red",
         linestyle='-.', marker="o", markeredgecolor="blue", markerfacecolor="blue")
plt.yticks([i for i in range(1, 9)])
plt.xticks([i for i in range(1, 9)])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
plt.close()

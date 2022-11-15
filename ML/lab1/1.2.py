import matplotlib.pyplot as plt


plt.title("Two or more lines with different widths and colors with suitable legends")
plt.plot([10, 20, 30], [20, 40, 10], color="blue",
         linewidth=3, label="line1-width-3")
plt.plot([10, 20, 30], [40, 10, 30], color="red",
         linewidth=5, label="line1-width-5")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
plt.close()

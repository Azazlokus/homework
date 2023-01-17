import matplotlib.pyplot as plt


plt.title("Plot with two or more lines with different styles")
plt.plot([10, 20, 30], [20, 40, 10], color="blue",
         linewidth=3, linestyle='--', label="line1-dotted")
plt.plot([10, 20, 30], [40, 10, 30], color="red",
         linewidth=5, linestyle=":", label="line1-dashed")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
plt.close()

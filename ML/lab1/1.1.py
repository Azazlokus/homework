import matplotlib.pyplot as plt


plt.title("Draw a line")
plt.plot([0.0, 48.0], [0.0, 150.0])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xticks([i for i in range(0, 51, 10)])
plt.yticks([i for i in range(0, 161, 20)])
plt.show()
plt.close()

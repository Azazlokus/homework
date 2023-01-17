import matplotlib.pyplot as plt


plt.plot([3, 4, 6, 7, 9], [2, 6, 11, 20, 23], "ro")
plt.plot([2, 3, 5, 6, 8], [1, 5, 10, 18, 20], "b*")
plt.yticks([5*i for i in range(7)])
plt.xticks([2*i for i in range(6)])
plt.show()
plt.close()

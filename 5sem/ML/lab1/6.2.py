import matplotlib.pyplot as plt


fig = plt.figure()
plt.plot([0.0, 100.0], [0.0, 200.0])
plt.xlabel("x")
plt.ylabel("y")
fig.add_axes([0.6, 0.5, 0.17, 0.15])
plt.plot([0.0, 100.0], [0.0, 200.0])
plt.xlabel("x")
plt.ylabel("y")
plt.show()
plt.close()

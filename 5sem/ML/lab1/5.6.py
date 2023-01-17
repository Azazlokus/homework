import matplotlib.pyplot as plt
import numpy as np


g = ["G1", "G2", "G3", "G4", "G5"]
men = [22, 30, 33, 30, 25]
women = [25, 32, 30, 35, 30]
glen = np.arange(len(g))
plt.bar(glen-0.2, men, 0.4, color="green", label="Men")
plt.bar(glen+0.2, women, 0.4, color="red", label="Women")
plt.title("Scores by person")
plt.xlabel("Person")
plt.ylabel("Scores")
plt.xticks(glen, g)
plt.legend()
plt.show()
plt.close()

import matplotlib.pyplot as plt


languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
scores = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(languages, scores, color="blue")
plt.minorticks_on()
plt.grid(True, which="major", color="red")
plt.grid(True, which="minor", linestyle="--")
plt.title(
    "Popularity of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.show()
plt.close()

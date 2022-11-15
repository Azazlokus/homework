import matplotlib.pyplot as plt


languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
scores = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
explode = [0.1, 0, 0, 0, 0, 0]
plt.pie(scores, labels=languages, autopct="%1.1f%%", explode=explode,
        wedgeprops={"ls": "-", "edgecolor": "black"})
plt.show()
plt.close()

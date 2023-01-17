import string
import numpy as np

table = np.genfromtxt("ABBREV.csv", delimiter=";",
                      dtype=None, names=True, encoding="utf8")
names = table["Shrt_Desc"]
Energ_Kcal = table["Energ_Kcal"]
Sugar_Tot = table["Sugar_Tot"]
Protein = table["Protein"]
Vit_C = table["Vit_C"]

index_Energ_Kcal = np.argmax(Energ_Kcal[::-1])
index_Sugar_Tot = np.argmin(Sugar_Tot)
index_Protein = np.argmax(Protein)
index_Vit_C = np.argmax(Vit_C)

print("The most high-calorie: " + names[len(table) - index_Energ_Kcal])
print("The most useful in terms of sugar content: " + names[index_Sugar_Tot])
print("The most protein-pumped: " + names[index_Protein])
print("The richest in vitamin C: " + names[index_Vit_C])

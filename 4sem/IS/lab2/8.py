from random import randint


list = [randint(-5, 15) for i in range(11)]
print("Список: ", list)
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
    else:
        unique_list.remove(i)

for i in unique_list:
    print(i, end=" ")

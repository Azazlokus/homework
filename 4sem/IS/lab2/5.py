from random import randint


list = [randint(-5, 15) for i in range(11)]
print("Список: ", list)
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        print(list[i], end=" ")

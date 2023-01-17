from random import randint


list = [randint(-5, 15) for i in range(11)]
print("Список: ", list)
for i in range(len(list)):
    if ((list[i] >= 0 and list[i+1] >= 0) or
            (list[i] < 0 and list[i+1] < 0)):
        print(list[i], list[i+1])
        break

from random import randint


n = int(input("Введите кол-во элементов в списке: "))
list = [randint(-5, 15) for i in range(n)]
print("Список: ", list)
for i in range(1, len(list), 2):
    list[i-1], list[i] = list[i], list[i-1]
print(list)

from random import randint


lst = [randint(0, 10) for i in range(10)]
print("Список: ", *lst)

print("Обычное решение")
for i in lst:
    if i < 5:
        print(i, end=" ")

print("\nРешение через функцию filter")
print(*list(filter(lambda x: x < 5, lst)))

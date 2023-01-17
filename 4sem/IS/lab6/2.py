from random import randint


lst = [randint(0, 10) for i in range(10)]
print("Список: ", *lst)

print("Обычное решение")
for i in lst:
    print(i / 2, end=" ")

print("\nРешение через функцию map")
print(*list(map(lambda x: x / 2, lst)))

from random import randint


lst = [randint(0, 30) for i in range(10)]
print("Список: ", *lst)

print("Обычное решение")
for i in lst:
    if i > 17:
        print(i / 2, end=" ")

print("\nРешение через функцию map и filter")
print(*list(map(lambda x: x / 2, filter(lambda x: x > 17, lst))))

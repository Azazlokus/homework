from random import randint

numbers = [randint(-50, 20) for x in range(10)]
print("Список:", *numbers)
print("Отсортированный список:", *sorted(numbers, key=lambda x: -abs(x)))

number = input("Введите 3-значное число: ")
if (int(number[0]) + int(number[2]))/2 == int(number[1]):
    print("Вы ввели красивое число")
else:
    print("Жаль, вы ввели обычное число")

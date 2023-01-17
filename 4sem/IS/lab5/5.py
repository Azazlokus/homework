def palindrome(line):
    if line.lower().replace(" ", "") == line[::-1].lower().replace(" ", ""):
        return "Палиндром"
    else:
        return "Не палиндром"


line = input("Введите строку: ")
print(palindrome(line))

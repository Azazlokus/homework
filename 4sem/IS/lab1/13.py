n = int(input("Введите длину: "))
m = int(input("Введите ширину: "))
symb = input("Введите символ: ")

print(symb * m)
for i in range(n-2):
    print(symb + " " * (m-2) + symb)
print(symb * m)

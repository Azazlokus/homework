n = int(input("Введите число: "))
count = 1
rows = 1

while count <= n:
    for i in range(1, rows+1):
        if count <= n:
            print(count, end=" ")
            count += 1
    rows += 1
    print()

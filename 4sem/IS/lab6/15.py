from random import randint


rows = int(input("Кол-во строк: "))
colunms = int(input("Кол-во столбцов: "))

table = []
for i in range(rows):
    temp = []
    for j in range(colunms):
        temp.append(randint(0, 10))
    table.append(temp)

print("Созданная таблица")
for row in table:
    print(*row)

print(any([0 in row for row in table]))

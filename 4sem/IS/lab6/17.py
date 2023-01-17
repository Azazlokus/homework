rows = int(input("Кол-во строк и столбцов: "))

table = []
for i in range(rows):
    nums = list(map(int, input().split()))
    table.append(nums[:rows])

res_sum = sum(table[0])
if all(sum(x) == res_sum for x in table) and all(sum(x) == res_sum for x in list(zip(*table))):
    print("YES")
else:
    print("NO")

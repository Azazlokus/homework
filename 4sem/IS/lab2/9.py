n = 8
x = []
y = []

for i in range(n):
    print(i + 1, "пара")
    x.append(int(input("x: ")))
    y.append(int(input("y: ")))

print("X: ", x)
print("Y: ", y)

flag = True
for i in range(n):
    for j in range(i + 1, n):
        if (x[i] == x[j] or y[i] == y[j] or
                abs(x[i] - x[j]) == abs(y[i] - y[j])):
            flag = False

if flag:
    print("NO")
else:
    print("YES")

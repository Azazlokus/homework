numbers = [int(s) for s in input().split()]
num_before = set()
for num in numbers:
    if num in num_before:
        print("YES")
    else:
        print("NO")
        num_before.add(num)

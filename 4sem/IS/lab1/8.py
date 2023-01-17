height = input()
count = 0
min_height = 200
max_height = 140
while height != "!":
    if int(height) >= 150 and int(height) <= 190:
        count += 1
        min_height = min(int(height), min_height)
        max_height = max(int(height), max_height)
    height = input()
print(count)
print(min_height, max_height)

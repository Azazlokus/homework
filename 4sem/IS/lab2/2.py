line = input()
l = len(line) + 1
part_1 = line[:l//2]
part_2 = line[l//2:]
new_line = part_2 + part_1
print(new_line)

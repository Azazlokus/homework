line = input()
first_h = line.find("h")
second_h = line.rfind("h") + 1
a = line[:first_h]
b = line[first_h:second_h]
c = line[second_h:]
new_line = a + b[::-1] + c
print(new_line)

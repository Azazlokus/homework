line = input()
first_f = line.find("f")
second_f = line.rfind("f")
if first_f == second_f and first_f >= 0:
    print(first_f)
elif second_f >= 0:
    print(first_f, second_f)

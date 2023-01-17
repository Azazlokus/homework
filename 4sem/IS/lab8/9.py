with open("input.txt", "r") as in_file:
    data = in_file.read().split()

data_int = [int(i) for i in data]

plus = []
minus = []
zeros = []

for num in data_int:
    if num > 0:
        plus.append(num)
    elif num < 0:
        minus.append(num)
    else:
        zeros.append(num)

with open("output.txt", "w") as out_file:
    out_file.write(str(len(data_int)) + "\n1 " + str(len(plus)) +
                   " -1 " + str(len(minus)) + " 0 " + str(len(zeros)))

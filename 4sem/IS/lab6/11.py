def print_opertion_table(operation, num_rows=9, num_colunms=9):
    for row in range(1, num_rows + 1):
        for colunm in range(1, num_colunms + 1):
            print(operation(row, colunm), end="\t")
        print()


print_opertion_table(lambda x, y: x * y)

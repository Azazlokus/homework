def reverse():
    with open("input.dat", "rb") as in_file:
        data = in_file.read()
    with open("output.dat", "wb") as out_file:
        out_file.write(data[::-1])


reverse()

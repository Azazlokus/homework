def alphabet():
    a = ord('а')
    for i in range(32):
        yield chr(a + i)


for letter in alphabet():
    print(letter, end=" ")

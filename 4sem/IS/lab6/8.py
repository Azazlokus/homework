alphabet = (chr(ord('а') + i) for i in range(32))
for i in range(32):
    print(next(alphabet), end=" ")

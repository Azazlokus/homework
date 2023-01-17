n = int(input("Число строк: "))
unique_words = set()
for line in range(n):
    str = input().split()
    for word in str:
        if word[-1] == ".":
            word = word[:-1]
        unique_words.add(word)
print(len(unique_words))

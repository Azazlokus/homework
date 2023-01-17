num = int(input())

words = {}
for i in range(num):
    line = input().split()
    for word in line:
        words[word] = words.get(word, 0) + 1
lst = [(-pair[1], pair[0]) for pair in words.items()]
sorted_words = [pair[1] for pair in sorted(lst)]
print("Output:")
for word in sorted_words:
    print(word)

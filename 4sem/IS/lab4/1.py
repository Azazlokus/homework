line = input().split()
words = {}
for word in line:
    words[word] = words.get(word, 0) + 1

print(words)

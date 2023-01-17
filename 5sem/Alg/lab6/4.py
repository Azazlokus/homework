word = input("word: ")
similar_words = input("similar words: ").split()

words = {}
for word_s in similar_words:
    m = len(word)
    n = len(word_s)
    lookup = [[0]*(n+1) for _ in range(m+1)]
    max = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word[i-1] == word_s[j-1]:
                lookup[i][j] = lookup[i-1][j-1] + 1
                if lookup[i][j] > max:
                    max = lookup[i][j]
    words[word_s] = max
keys_words = list(words.keys())
sorted_tuple = sorted(words.items(), key=lambda x: -x[1])
print("answer: ", sorted_tuple[0][0])

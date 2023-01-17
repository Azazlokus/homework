from sys import stdin


words = []
for word in stdin.read().replace('.', '').split():
    words.append(word)

selected_words = list(filter(lambda x: x[1].istitle(), enumerate(words)))
sorted_words = sorted(selected_words, key=lambda x: x[1])

result = []
unique_words = set()
for pair in sorted_words:
    if pair[1] not in unique_words:
        result.append(pair)
        unique_words.add(pair[1])

for pair in result:
    print(pair[0], ' - ', pair[1])

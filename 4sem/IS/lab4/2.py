synonyms = {}

num = int(input())
for i in range(num):
    first_word, second_word = input().split()
    synonyms[first_word] = second_word
    synonyms[second_word] = first_word

print(synonyms[input()])

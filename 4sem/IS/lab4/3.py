num = int(input())
voting = {}

for i in range(num):
    name, votes = input().split()
    voting[name] = voting.get(name, 0) + int(votes)

voting = dict(sorted(voting.items()))
print("Output: ")
for key, value in voting.items():
    print(key, value)

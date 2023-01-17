from HashTable2 import HashTable

H = HashTable()
line = input().split()
for word in line:
	if H[word] == None:
		H[word] = 1
	else:
		H[word] += 1
	print(H[word])
	

	

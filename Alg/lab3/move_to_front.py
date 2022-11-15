from UnordredList import UnorderedList


def move_to_front(n: int):
	rez = UnorderedList()
	for _ in range(n):
		line = input()
		if (rez.search(line)):
			rez.remove(line)
			rez.add(line)
		else:
			rez.add(line)
	print(rez)


move_to_front(5)

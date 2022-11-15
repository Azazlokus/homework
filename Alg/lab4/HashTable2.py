from UnordredList import UnorderedList


class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def get_nearest_prime(self, start, stop, step=1):
		start = self.size
		lst = [2, 3, 5]
		for i in range(start, stop, step):
			for j in lst:
				if i % j == 0:
					break
			else:
				lst.append(i)
		return lst[-1]

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = UnorderedList()
			self.data[hashvalue] = UnorderedList()
			self.slots[hashvalue].append(key)
			self.data[hashvalue].append(data)
		else:
			if self.slots[hashvalue].search(key):
				idx = self.slots[hashvalue].index(key)
				self.data[hashvalue].pop(idx)
				self.data[hashvalue].insert(idx, data)
			else:
				self.slots[hashvalue].append(key)
				self.data[hashvalue].append(data)

		if (self.__len__()/self.size > 0.7):
			last_size = self.size
			self.size = self.get_nearest_prime(self.size, 2*self.size)
			self.slots += [None] * (self.size - last_size)
			self.data += [None] * (self.size - last_size)

	def hashfunction(self, key, size):
		if isinstance(key, str):
			key = len(key)
		return key % size

	def rehash(self, oldhash, size):
		return (oldhash + 1) % size

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while not found and not stop:
			if self.slots[position] != None:
				if self.slots[position].search(key):
					found = True
					idx = self.slots[position].index(key)
					data = self.data[position].pop(idx)
					self.data[position].insert(idx, data)
			
			position = self.rehash(position, len(self.slots))	
			if position == startslot:
				stop = True
					
		if (self.__len__()/self.size > 0.7):
			last_size = self.size
			self.size = self.get_nearest_prime(self.size, 2*self.size)
			self.slots += [None] * (self.size - last_size)
			self.data += [None] * (self.size - last_size)
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)

	def __len__(self):
		count = 0
		for i in range(self.size):
			if self.slots[i] != None:
				count += 1
		return count

	def __contains__(self, item):
		found = False
		for i in range(self.size):
			if self.data[i] != None and self.data[i].search(item):
				found = True
				break
		return found
	
	def __delitem__(self, key):
		idxList = -1
		idxItem = -1
		for i in range(self.size):
			if self.slots[i] != None and self.slots[i].search(key):
				idxList = i
				idxItem = self.slots[i].index(key)
				break
		if idxItem >= 0:
			self.slots[idxList].pop(idxItem)
			self.data[idxList].pop(idxItem)
			if self.slots[idxList].size() == 0:
				self.slots[idxList] = None
				self.data[idxList] = None
		
		if self.__len__()/self.size < 0.2:
			slots = []
			data = []
			for i in range(self.size):
				if self.slots[i] != None:
					for _ in range(self.slots[i].size()):
						slots.append(self.slots[i].pop())
						data.append(self.data[i].pop())
			self.size = self.get_nearest_prime(self.size, self.size//2, -1)
			self.slots = [None] * self.size
			self.data = [None] * self.size
			for i in range(len(slots)):
				self.put(slots[i], data[i])

if __name__ == "__main__":			
	H = HashTable()
	H[54] = "cat"
	H[26] = "dog"
	H[93] = "lion"
	H[17] = "tiger"
	H[77] = "bird"
	H[31] = "cow"
	H[44] = "goat"
	H[55] = "pig"
	H[20] = "chicken"
	H[12] = "elephant"
	H[14] = "fish"
	print("После добавления элементов")
	for i in range(H.size):
		print(H.slots[i], end=" ")
		print(H.data[i])
	print(len(H))
	print("cow" in H)
	print(H[20])
	del H[20]
	del H[12]
	del H[14]
	del H[31]
	del H[26]
	del H[93]
	print("После удаления элементов")
	for i in range(H.size):
		print(H.slots[i], end=" ")
		print(H.data[i])
	H["cat"] = "1111111"
	for i in range(H.size):
		print(H.slots[i], end=" ")
		print(H.data[i])

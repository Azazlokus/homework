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
				if i%j == 0:
					break
			else:
				lst.append(i)
		return lst[-1]
		

	def put(self, key, data):
		hashvalue = self.hashfunction(key, len(self.slots))

		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data  # replace
			else:
				i = 1
				nextslot = self.rehash(hashvalue, len(self.slots), i)
				while self.slots[nextslot] != None and \
						self.slots[nextslot] != key:
					i += 1
					nextslot = self.rehash(nextslot, len(self.slots), i)

				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
				else:
					self.data[nextslot] = data  # replace
		if (self.__len__()/self.size > 0.7):
			last_size = self.size
			self.size = self.get_nearest_prime(self.size, 2*self.size)
			self.slots += [None] * (self.size - last_size)
			self.data += [None] * (self.size - last_size)

	def hashfunction(self, key, size):
		return key % size

	def rehash(self, oldhash, size, i):
		return (oldhash + i**2) % size

	def get(self, key):
		startslot = self.hashfunction(key, len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		i = 1
		while self.slots[position] != None and \
				not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position = self.rehash(position, len(self.slots), i)
				i += 1
				if position == startslot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)
	
	def __delitem__(self, key):
		idx = -1
		for i in range(self.size):
			if self.slots[i] == key:
				idx = i
				break
		if idx >= 0:
			self.slots[idx] = None
			self.data[idx] = None

		if self.__len__()/self.size < 0.2:
			slots = []
			data = []
			for i in range(self.size):
				if self.slots[i] != None:
					slots.append(self.slots[i])
					data.append(self.data[i])
			self.size = self.get_nearest_prime(self.size, self.size//2, -1)
			self.slots = [None] * self.size
			self.data = [None] * self.size
			for i in range(len(slots)):
				self.put(slots[i], data[i])


	def __len__(self):
		count = 0
		for i in range(self.size):
			if self.slots[i] != None:
				count += 1
		return count
	
	def __contains__(self, item):
		found = False
		for i in range(self.size):
			if self.data[i] == item:
				found = True
				break
		return found


H = HashTable()
print("До добавления элементов")
print(H.slots)
print(H.data)
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print("После добавления элементов")
print(H.slots)
print(H.data)

print(H[20])
print(H[17])
H[20] = 'duck'
print(H[20])
print(H[99])
print(len(H))
print("cat" in H)

print("До удаления элементов")
print(H.slots)
print(H.data)
del H[20]
del H[54]
del H[26]
del H[93]
del H[55]
del H[44]
print("После удаления элементов")
print(H.slots)
print(H.data)

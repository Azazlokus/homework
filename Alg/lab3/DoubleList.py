class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None
		self.prev = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next
	
	def getPrev(self):
		return self.prev

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext
	
	def setPrev(self, newprev):
		self.prev = newprev


class DoubleList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found
	
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		temp.setPrev(None)
		self.head = temp
	
	def append(self, item):
		current = self.head
		if current == None:
			self.add(item)
			return
		while current.getNext() != None:
			current = current.getNext()
		temp = Node(item)
		temp.setNext(None)
		temp.setPrev(current)
		current.setNext(temp)

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())
		if current.getNext():
			current.getNext().setPrev(previous)
	
	def pop(self, pos=None):
		if self.isEmpty():
			raise ("List is empty")
		current = self.head
		if pos == None:
			while current.getNext() != None:
				current = current.getNext()
		else:
			if self.size() - 1 < pos or pos < 0:
				raise ("Index out of range")
			for _ in range(pos):
				current = current.getNext()
		self.remove(current.getData())
		return current.getData()
	
	def insert_after(self, pos, item):
		if self.size() - 1 < pos or pos < 0:
			raise ("Index out of range")
		current = self.head
		for _ in range(pos):
			current = current.getNext()
		temp = Node(item)
		temp.setNext(current.getNext())
		temp.setPrev(current)
		if current.getNext():
			current.getNext().setPrev(temp)
		current.setNext(temp)
		
	def insert_before(self, pos, item):
		if self.size() - 1 < pos or pos < 0:
			raise ("Index out of range")
		current = self.head
		for _ in range(pos):
			current = current.getNext()
		temp = Node(item)
		temp.setNext(current)
		temp.setPrev(current.getPrev())
		if current.getPrev():
			current.getPrev().setNext(temp)
		current.setPrev(temp)
		if temp.getPrev() == None:
			self.head = temp

	def __str__(self):
		current = self.head
		output = "["
		while current != None:
			output += str(current.getData()) + ", "
			current = current.getNext()
		output = output[:-2] + "]"
		return output

	
if __name__ == "__main__":
	mylist = DoubleList()
	mylist.append(0)
	mylist.append(1)
	mylist.append(2)
	mylist.append(3)
	mylist.append(4)
	print(mylist)
	mylist.insert_before(3, 10)
	mylist.insert_after(0, 10)
	print(mylist)
	

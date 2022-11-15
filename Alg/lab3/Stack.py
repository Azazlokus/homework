from UnordredList import UnorderedList

class Stack:
	def __init__(self):
		self.items = UnorderedList()
	
	def isEmpty(self):
		return self.items.isEmpty()

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[self.items.size()-1:self.items.size()]
		
	def size(self):
		return self.items.size()
	
	def __str__(self):
		current = self.items.head
		output = "["
		while current != None:
			output += str(current.getData()) + ", "
			current = current.getNext()
		output = output[:-2] + "]"
		return output

if __name__ == "__main__":
	stack = Stack()
	print(stack.isEmpty())
	stack.push(4)
	print(stack.size())
	stack.push("dog")
	print(stack.peek())
	stack.pop()
	print(stack.size())
	print(stack.peek())
	print(stack)



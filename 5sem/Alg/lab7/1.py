class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

	def size(self):
		return len(self.items)


class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootVal(self):
		return self.key


def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = Stack()
	eTree = BinaryTree('')
	pStack.push(eTree)
	currentTree = eTree
	for i in fplist:
		if i == '(':
			currentTree.insertLeft('')
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i == ')':
			currentTree = pStack.pop()
		elif i not in ['&', '|', '!']:
			if i == 't':
				i = True
			elif i == 'f':
				i = False
			currentTree.setRootVal(bool(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ['&', '|', '!']:
			currentTree.setRootVal(i)
			currentTree.insertRight('')
			pStack.push(currentTree)
			currentTree = currentTree.getRightChild()
		else:
			raise ValueError
	return eTree


def evaluate(parseTree):
	opers = {'&': lambda x, y: x and y, '!': lambda x: not x,
			 '|': lambda x, y: x or y,}

	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootVal()]
		return fn(evaluate(leftC), evaluate(rightC))
	elif rightC:
		fh = opers[parseTree.getRootVal()]
		return fh(evaluate(rightC))
	else:
		return parseTree.getRootVal()


pt = buildParseTree("( ( t | f ) & f )")


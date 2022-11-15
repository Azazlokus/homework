from UnordredList import UnorderedList

def reverse_list(list: UnorderedList):
	prev = None
	current = list.head
	next = current.getNext()
	while next != None:
		current.setNext(prev) 
		prev = current
		current = next
		next = next.getNext()
	current.setNext(prev)
	list.head = current
	return current
			
			
def reverse_list_r(list: UnorderedList):
	current = list.head
	if current != None:
		pass


myList = UnorderedList()
myList.append(1)
myList.append(2)
myList.append(3)
myList.append(4)
myList.append(5)
print(myList)
reverse_list(myList)
print(myList)
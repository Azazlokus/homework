from UnordredList import UnorderedList


class Deque:
    def __init__(self):
        self.items = UnorderedList()

    def isEmpty(self):
        return self.items.isEmpty()

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

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.add(item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)


if __name__ == "__main__":
    d = Deque()
    d.addRear(4)
    d.addRear("dog")
    d.addFront("cat")
    print(d)
    print(d.removeFront())
    print(d)
    print(d.removeRear())
    print(d)

# Linked List Class


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, next_data):
        self.next = next_data

    def __repr__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            current = current.getNext()
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is not None:
            if current.getData() == item:
                if previous is not None:
                    previous.setNext(current.getNext())
                self.head = current.getNext()
            previous = current
            current = current.getNext()

    def append(self, item):
        temp = Node(item)
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.getNext()
        previous.setNext(temp)

    def insert(self, pos, item):
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        while current is not None:
            if count == pos:
                temp.setNext(current)
                previous.setNext(temp)
                break
            count += 1
            previous = current
            current = current.getNext()

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.getData() == item:
                return count
            count += 1
            current = current.getNext()

    def __repr__(self):
        items = []
        current = self.head
        while current is not None:
            items.append(current.getData())
            current = current.getNext()
        return str(items)

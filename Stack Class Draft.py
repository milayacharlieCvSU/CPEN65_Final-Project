# Stack Class
class Stack:
    def __init__(self):
        self.aList = []

    def push(self, item):
        self.aList.append(item)

    def pop(self):
        return self.aList.pop()

    def peek(self):
        return self.aList[-1]

    def isEmpty(self):
        return self.aList == []

    def size(self):
        return len(self.aList)

    def __repr__(self):
        return str(self.aList)

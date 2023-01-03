# Stack Class
class Stack:
    def __init__(self):
        self.aList = []
       
    # Push the 'item' in the stack.
    def push(self, item):
        if item in self.items:
            return False
        self.aList.append(item)
       
    # Removes the newest item in the stack and return it.
    def pop(self):
        if self.items == []:
            return "The stack is empty."
        return self.aList.pop()
    
    # Peek the newest item in the stack without removing it.
    def peek(self):
        return self.aList[-1]
    
    # Checks whether the stack is empty or not.
    def isEmpty(self):
        return self.aList == []

    # Returns the size of the stack using the len() operator.
    def __len__(self):
        return len(self.aList)

    #returns the stack for printing and debugging purposes.
    def __repr__(self):
        return str(self.aList)

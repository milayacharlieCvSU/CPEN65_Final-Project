# Queue Class
class Queue:
    def __init__(self):
        self.items = []
    
    # Adds 'item' on the queue.
    def enqueue(self, item):
        if item in self.items:
            return False
        return self.items.insert(0, item)
    
    # Removes the first item in the queue. Returns the item if the queue is not empty and a string otherwise.
    def dequeue(self):
        if self.items == []:
            return "The queue is empty."
        return self.items.pop()
    
    # Returns the first item in the queue without removing it.
    def first(self):
        return self.items[-1]
    
    # Check whether the queue is empty or not.
    def isEmpty(self):
        return self.items == []
    
    # Returns the size of the queue using the len() operator.
    def __len__(self):
        return len(self.items)
    
    # Returns the queue for printing and debugging purposes.
    def __repr__(self):
        return str(self.items)

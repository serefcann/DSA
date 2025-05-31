class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.isEmppty():
            return 'list is empty'
        return self.queue.pop(0)
        
    def isEmppty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.isEmppty():
            return 'list is empty'
        return self.queue[0]

MyQueue = Queue()
MyQueue.enqueue(4)
MyQueue.enqueue(5)
MyQueue.enqueue(0)

MyQueue.dequeue()
MyQueue.size()
MyQueue.peek()
MyQueue.isEmppty()
MyQueue.queue # returns the element of the queue (list)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue: # 1 4 5 6
    def __init__(self):
        self.rear = None
        self.front = None
        self.length = 0
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.rear is None:
            self.rear = self.front = newNode
            self.length += 1
            return
        self.rear.next = newNode
        self.rear = newNode
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return 'queue is empty'
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
        
    def isEmpty(self):
        return self.length == 0  
    def peek(self):
        return self.front.data
    def size(self):
        return self.length
    def printQueue(self):
        currentNode = self.front
        while currentNode:
            print(currentNode.data, end= ' -> ')
            currentNode = currentNode.next
        print('None')
        
queue = Queue()
queue.enqueue(4)
queue.enqueue(14)
queue.enqueue(5)
queue.enqueue(3)

queue.dequeue()
queue.isEmpty()
queue.peek()
queue.size()
queue.printQueue()
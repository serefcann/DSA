class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
    def push(self, value):# 1 2 3 4
        newNode = Node(value)
        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1
    def pop(self):
        if self.isEmpty():
            return 'stack is empty'
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.data
    def peek(self):
        if self.isEmpty():
            return 'stack is empty'
        return self.head.data
    def stackSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
        

MyStack = Stack()
MyStack.push(6)
MyStack.push(7)
MyStack.pop()
MyStack.peek()
MyStack.stackSize()
MyStack.isEmpty()

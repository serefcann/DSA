# Stack for arrays
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return print('stack is empty')
        self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return print('stack is empty')
        return self.stack[-1]
        
    def isEmpty(self):
        return len(self.stack) == 0
MyStack = Stack()
MyStack.push(2)
MyStack.push(5)
MyStack.push(9)
MyStack.pop()
MyStack.peek()
MyStack.isEmpty()
MyStack.stack
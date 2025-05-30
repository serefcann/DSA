class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
node1 = Node(3)
node2 = Node(5)
node3 = Node(1)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4


def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end= '-> ')
        currentNode = currentNode.next
    print('none')
traverseAndPrint(node1)

def findLowestValue(head):
    currentNode = head
    min_value = head.data
    while currentNode:
        if currentNode.data < min_value:
            min_value = currentNode.data
        currentNode = currentNode.next
    return min_value
findLowestValue(node1)

def deleteSpesificNode(head, nodeToDelete):
    
    if head == nodeToDelete:
        head = head.next
    
    currentNode = head
    while currentNode and currentNode.next != nodeToDelete:
        currentNode = currentNode.next
    
    if currentNode.next is None:
        return -1    
    
    currentNode.next = currentNode.next.next

deleteSpesificNode(node1,node4)
traverseAndPrint(node1)

def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode
        
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode


newNode = Node(94)
insertNodeAtPosition(node1, newNode=newNode, position=10) 
traverseAndPrint(node1)
        
        
    
    
            
        
        
        
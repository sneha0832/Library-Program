from LinkedList import LinkedList
from Node import Node

class Queue:
    def __init__(self):
        self.list = LinkedList()  
 
    def enqueue(self, data):
        self.list.append(data)
        
    def dequeue(self):
        self.list.goBeginning() 
        x = self.list.getData()
        self.list.remove()
        return x
    
    def peek(self):
        self.list.goBeginning()
        return self.list.getData()
    
    
x = 'data'
newqueue = Queue()
for i in x:
    n = Node(i)
    newqueue.enqueue(n)
print(newqueue)
    
        

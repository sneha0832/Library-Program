# LinkedList class
# I have given you the basic structure of the class.
# TO DO: Complete the methods that have "pass" in their places
# and add comments for each method - 1 or 2 lines saying what it does
# Then test it using the LL_Tester file before doing the assignment
# YOUR NAME: Sneha Patel

from Node import Node

class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = Node()
        self._curr = Node()
    
    #changes or returns where the pointers are pointing
    #we use these instead of normal getters/setters so folks don't mess with our pointers
    # here = a Node object
    def setHead(self, here):
        self._head.link = here
    def getHead(self):
        return self._head.link
    def setTail(self, here):
        self._tail.link = here
    def getTail(self):
        return self._tail.link
    def setCurr(self, here):
        self._curr.link = here
    def getCurr(self):
        return self._curr.link
    
    def isEmpty(self):
        if self.getHead() == None:
            return True
        return False
    
    def isBeginning(self):
        if self.getCurr() == self.getHead():
            return True
        return False
    
    def isEnd(self):
        if self.getCurr() == self.getTail():
            return True
        return False
    
    def goBeginning(self):
        self.setCurr(self._head.link) 
    
    def goEnd(self):
        self.setCurr(self._tail.link)
        
    def getSize(self):
        if self.isEmpty():
            return 0
        else:
            pos = 0
            temp = self.getHead()
            while temp != self.getTail():
                pos += 1
                temp = temp.link
            return pos+1
        
    
    def getPos(self):
        #returns the current position as a number
        if self.isEmpty():
            return -1
        elif self.getHead() == self.getCurr():
            return 0
        temp = self.getHead()
        pos = 0
        while temp != self.getCurr():
            pos += 1
            temp = temp.link
        return pos
    
    def setPos(self, pos):
        self.goBeginning()
        for i in range(0,pos):
            self.goNext()
    
    def goNext(self):
        if self.isEmpty():
            pass
        elif self.isEnd():
            pass
        else:
            self.setCurr(self.getCurr().link)
    
    def goPrev(self):
        if self.isBeginning():
            pass
        elif self.isEmpty():
            pass
        else:
            self.setPos(self.getPos() -1)
    
    def setData(self, d):
        self.getCurr().data = d
        
    def getData(self):
        return self.getCurr().data
    
    def insert(self, n):
        #inserts a new node, n, after the curr.link node
        if self.isEmpty:
            self._head.link = self._curr.link = self._tail.link = n
        else:
            x = self.getCurr()
            self.goNext()
            self.insertBefore(n)
            
    def append(self, n):
        #if the list is empty, set head, curr, and tail to the node
        if self.isEmpty():
            self._head.link = self._curr.link = self._tail.link = n
        #inserts at the end of the list
        else:
            #while self._curr.link != self._tail.link:
            self.goEnd()
            self._curr.link.link = n
            self._tail.link = n              
            
    def insertBefore(self, n): 
        # inserts before curr
        if self.isEmpty():#if  list empty inserts at 1st position
            self._head.link = self._curr.link = self._tail.link = n
        elif self.isBeginning():#if at beginning adds before that node
            n.link = self._head.link
            self._head.link = n
            self._curr.link = n
        else:#if at a position, it goes prev and then adds to
            x = self.getCurr()
            self.goPrev()
            self._curr.link.link = n
            n.link = x
            
    
    def remove(self):
        #removes the node at curr
        if self.isEmpty():
            pass
        elif self.isBeginning():
            self._head.link = self.getCurr().link
        else:
           x = self.getData()
           self.goPrev()
           self._curr.link =  self._curr.link.link
    
    def copy(self):
        #copies the list and returns a new list
        self.setCurr(self._head.link)
        temp = LinkedList()
        while self._curr.link != None:
            n = Node(self._curr.link.data)
            temp.append(n)
            self.setCurr(self._curr.link.link)
        return temp
    
    def Merge(self):
        size = self.getSize()
        if size==1:
            return self
        #iinitialize two ll
        half1 = self.copy()
        half2 = self.copy()
        half1.setPos((size//2) -1)
        half1.getCurr().link = None
        half1.setTail(half1.getCurr())#makes it first half by cutting off the tail and by killing the link
        half2.setPos((size)//2)
        half2.setHead(half2.getCurr())#makes it second half by changing head

        #now we need to merge the halves till the we are left with the base case
        l1 = half1.Merge()
        l2 = half2.Merge()

        return self.Merge2(l1,l2)

    def Merge2(self, l1,l2):
        final = LinkedList()
        while (not l1.isEmpty() and not l2.isEmpty()):
            l1.setPos(0)#first number is always the smallest
            l2.setPos(0)
            x = l1.getData()
            y = l2.getData()
            if x< y :
                final.append(Node(x))
                l1.remove()
            else:
                final.append(Node(y))
                l2.remove()
        while not l1.isEmpty():
            l1.setPos(0)
            item = l1.getData()
            l1.remove()
            final.append(Node(item))
        while not l2.isEmpty():
            l2.setPos(0)
            item = l2.getData()
            l2.remove()
            final.append(Node(item))
        return final

    '''
    def __str__(self):
        self.setCurr(self._head.link)
        s = ""
        while self._curr.link != None:
            s += str(self._curr.link.data)
            s += "  "
            self.setCurr(self._curr.link.link)
        return s
    '''
    def __str__(self):
        current = self.getHead()
        s = ""
        while current is not None:
            s += current.data.s + " | " 
            current = current.link

        return s[:-3] # remove trailing "
                                               
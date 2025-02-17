# LinkedList class
# I have given you the basic structure of the class.
# TO DO: Complete the methods that have "pass" in their places
# and add comments for each method - 1 or 2 lines saying what it does
# Then test it using the LL_Tester file before doing the assignment

#Program 4 - Sorting Algorithms in Linked Lists
#Sneha Patel
# Oct 30, 2023
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
    
    #help from Sara for this sorting algorithm
    def Merge(self):
        size = self.getSize()
        if size==1:
            return self
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


    def QuickSort(self):
        if self.getSize() <= 1:
            return self
        SP = LinkedList()#list for the numbers which are smaller than the pivot value
        GP = LinkedList()#list for the numbers which are larger then the pivot value
        #if self.isEmpty():
        #   return self 
        self.goBeginning()
        piv = self.getData()#taking the first as the pivot value
        #print("sorting.... pivot = {}".format(piv))
        self.goNext()
        #self.goBeginning()
        while (not self.isEnd()):#while the list exists
            if self.getData() <= piv:#if the current number is greater than the pivot value
                SP.append(Node(self.getData()))#append the number(as a new node) to the GP list
            elif self.getData() > piv:#if the current number is smaller than the pivot value
                GP.append(Node(self.getData()))
            self.goNext() 
        # get last node
        if self.getData() <= piv:#if the current number is greater than the pivot value
                SP.append(Node(self.getData()))#append the number(as a new node) to the GP list
        elif self.getData() > piv:#if the current number is smaller than the pivot value
                GP.append(Node(self.getData()))
        
        #self.getTail()
        GP=GP.QuickSort()
        SP=SP.QuickSort()
        #print(SP)
        #print(GP)
        #print(GP)
        if (SP.isEmpty()):
            FL = LinkedList()
        else:
            FL = SP
        FL.append(Node(piv))
        #FL.append(GP.getHead())
        if (not GP.isEmpty()):
            while (not GP.isEmpty()):
                GP.goBeginning()
                FL.append(Node(GP.getData()))
                GP.remove()
        #print(FL)
        return FL
    
    def Insertion_sort(self):
        #while self._curr.link:-1
        self.goBeginning()
        #print(self.getSize())
        for i in range(1,self.getSize()):#for i in range of the list
            while i > 0:
                self.setPos(i-1)
                x = self.getData()
                self.setPos(i)
                y = self.getData()
                if y<x:#if the next number is greater than the number itself then swap
                    self.setData(x)
                    self.goPrev()
                    self.setData(y) 
                i -= 1
        return self
            
                    
    def OBubble_sort(self):
        for i in range(1, self.getSize()):#this loop is for going forwards in the list
            #print(self)
            #self.goBeginning()#go to the beginning
            for j in range(1, self.getSize()):#this loop is for looking at two numbers
                self.setPos(j-1)
                x = self.getData()
                self.setPos(j)
                y = self.getData()
                if x > y:#if the next number is greater than the number itself then swap
                    self.setData(x)
                    self.goPrev()
                    self.setData(y)
        return self

    def __str__(self):
        self.setCurr(self._head.link)
        s = ""
        while self._curr.link != None:
            s += str(self._curr.link.data)
            s += "  "
            self.setCurr(self._curr.link.link)
        return s
                                               
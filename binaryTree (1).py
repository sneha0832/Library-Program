# binary tree code
# TO DO:
#      1. Add a method for deleting (removing) a node no matter where it's located
#      2. Add the traversal methods (inorder, postorder, and preorder) using recursion
#      3. Print the tree level by level so it kind of looks like a tree as the __str__ method
#         (feel free to get online/AI help for this one)
#      4. In a separate file, create your own testing program. That program should
#         try every method in this class in multiple scenarios (like the LLTester does).

from binNode import binNode

class binaryTree:
    def __init__(self, r = None, c = None):
        self._root = r
        self._curr = c
    
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, n):
        self._root = n
    @property
    def curr(self):
        return self._curr
    @curr.setter
    def curr(self, n):
        self._curr = n
    
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def isLeaf(self):
        if self.curr.left == None and self.curr.right == None:
            return True
        else:
            return False
    
    def getData(self):
        if self.curr == None:
            return None
        else:
            return self.curr.data
        
    def goRoot(self):
        self.curr = self.root
    
    def goLeft(self):
        self.curr = self.curr.left
    
    def goRight(self):
        self.curr = self.curr.right
        
    def getMin(self):
        self.goRoot()
        while self.curr.left != None:
            self.goLeft()
        return self.getData()

    def getMax(self):
        self.goRoot()
        while self.curr.right != None:
            self.goRight()
        return self.getData()

    # recursive function to insert
    # only used inside binaryTree class!!!
    def insertNode(self, here, n):
        if here == None:
            here = n
        else:
            if n.data < here.data:
                 here.left = self.insertNode(here.left, n)
            else:
                here.right = self.insertNode(here.right, n)
        return here
    
    # inserts a node (n)
    # This is the method you'll call outside of this class
    def insert(self, n):
        if self.isEmpty() == True:
            self.root = n
            self.curr = n
        else:
            self.goRoot()
            self.curr = self.insertNode(self.curr, n)
            
    # does the actual counting
    # again, used only in-class
    def count(self, n):
         if n == None:
             return 0
         else:
             l = 1
             l += self.count(n.left)
             l += self.count(n.right)
             return l
            
    # use this outside of the class
    def getSize(self):
        return self.count(self.root)
    
    # next 2 methods find a node in the tree or returns None if not there
    def findIt(self, n, what):
        if n == None:
            return None # not found
        if n.data.name == what:
            return n
        elif what < n.data.name:
            return self.findIt(n.left, what)
        elif what > n.data.name:
            return self.findIt(n.right, what)
    
    def search(self, what):
        self.curr = self.findIt(self.root, what)
        return self.curr
   
    # remove a node from the tree
    # "what" is the data - use it to find the node to kill
    def remove(self, what):
        
        pass

    
    ### traversal methods ###
    def inOrder(self, n):
        if n.root == None:
            return
        self.inOrder(n.left)
        print(n.data)
        self.inOrder(n.right)     
    
    def traverseInOrder(self):
        self.goRoot()
        self.inOrder(self.curr)
    
    def PreOrder(self, n):
        if n.root == None:
            return
        print(n.data)
        if n.left:
            self.PreOrder(n.left)
        elif n.right:
            self.PreOrder(n.right)
        else:
            return 

               
    def traversePreOrder(self):
        self.goRoot()
        self.PreOrder(self.curr)
        
    def PostOrder(self, n):
        pass
        
    def traversePostOrder(self):
        self.goRoot()
        self.PostOrder(self.curr)
        
    # returns a string that when printed
    # shows the tree in tree form
    # for example:
    #         M
    #      F      T
    #    B   H  R   W
    def __str__(self):
        pass
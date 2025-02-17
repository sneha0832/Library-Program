# binary tree code
# TO DO:
#      1. Add a method for deleting (removing) a node no matter where it's located
#      2. Add the traversal methods (inorder, postorder, and preorder) using recursion
#      3. Print the tree level by level so it kind of looks like a tree as the __str__ method
#         (feel free to get online/AI help for this one)
#      4. In a separate file, create your own testing program. That program should
#         try every method in this class in multiple scenarios (like the LLTester does).

#Final Program
#Binary Tree
#Sneha Patel
#Dec 11, 2023

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
    '''
    def findIt(self, n, what, attribute):
        #print(attribute)
        if n is None:
            return None  # not found
        if getattr(n.data, attribute) == what:
            return n
        elif what < getattr(n.data, attribute):
            #print(n.data)
            return self.findIt(n.left, what, attribute)
        elif what > getattr(n.data, attribute):
            #(n.data)
            return self.findIt(n.right, what, attribute)

    def search(self, n, what, attribute):
        self.curr = self.findIt(n, what, attribute)
        return self.curr
    #above I updated my search and findit method
    '''
    # next 2 methods find a node in the tree or returns None if not there
    def findIt(self, n, what):
        if n == None:
            return None # not found
        if n.data == what:
            return n
        elif what < n.data:
            return self.findIt(n.left, what)
        elif what > n.data:
            return self.findIt(n.right, what)
    
    def search(self,what):
        n = self.findIt(self.root, what)
        return n
    
    #helper method to remove node
    def helper_remove(self, node,node_to_remove):
        if node is None:
            return None
        if node_to_remove < node.data:
            node.left = self.helper_remove(node.left, node_to_remove)
        elif node_to_remove > node.data:
            node.right = self.helper_remove(node.right, node_to_remove)
        else:  # Node to be removed is found
            if node.left is None:  # Case 1: Node has one or no child
                return node.right
            elif node.right is None:  # Case 2: Node has one child
                return node.left
            else:  # Case 3: Node has two children
                swap = self.getMin()
                node.data = swap #replaces the data of the current node
                node.right = self.helper_remove(node.right, swap)
        return node

    # remove a node from the tree
    # "what" is the data - use it to find the node to kill
    def remove(self, what):
        value = what
        node_to_remove = value
        #node_to_remove = self.search(what)
        self.root = self.helper_remove(self.root, node_to_remove)
    
    ### traversal methods ###
    #Inorder = "LNR"
    def inOrder(self, n):
        if n is not None:
            self.inOrder(n.left)
            print(n.data)
            self.inOrder(n.right)     
    
    def traverseInOrder(self):
        self.goRoot()
        self.inOrder(self.curr)
    #Preorder = "NLR"
    def PreOrder(self, n):
        if n is not None:
            print(n.data)
            if n.left:
                self.PreOrder(n.left)
            if n.right:
                self.PreOrder(n.right)

    def traversePreOrder(self):
        self.goRoot()
        self.PreOrder(self.curr)
    #PostOrder = "LRN"   
    def PostOrder(self, n):
        if n is not None:
            if n.left:
                self.PostOrder(n.left)
            if n.right:
                self.PostOrder(n.right)
            print(n.data)
    
    def traversePostOrder(self):
        self.goRoot()
        self.PostOrder(self.curr)
        
    # returns a string that when printed
    # shows the tree in tree form
    # for example:
    #         M
    #      F      T
    #    B   H  R   W
    #took help from stockexchange site
    #helper method for str
    def str(self,node,level=0):
        result = ""
        if node is not None:
            result += self.str(node.left, level + 1)
            result += ' ' * 4 * level + '-> ' + str(node.data) + "\n"
            result += self.str(node.right, level + 1)
        return result

    def __str__(self):
        if self.root is None:
            return "Empty tree"
        return self.str(self.root)

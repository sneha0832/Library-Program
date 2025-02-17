#Final Program
#binaryNode class
#Sneha Patel
#Dec 11, 2023

# Node class for a binary tree
class binNode:
    def __init__(self, d=None, l=None, r=None):
        self._data = d
        self._left = l
        self._right = r
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, d):
        self._data = d
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, l):
        self._left = l
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, r):
        self._right = r
    
    def __str__(self):
        return str(self.data)
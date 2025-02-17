# This is the Node class that your linked list will use
# You may not change anything in this file
#Program 4 - Sorting Algorithms in Linked Lists
#Sneha Patel
# Oct 30, 2023

class Node:
    def __init__(self, d=None, l=None):
        self._data = d
        self._link = l
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, d):
        self._data = d
    @property
    def link(self):
        return self._link
    @link.setter
    def link(self, l):
        self._link = l

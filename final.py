from Node import Node
from LinkedList import LinkedList

class Library:
    def __init__(self,title,author,status,Priority):
        self._title = title
        self._author = author
        self._status= bool(1)
        self._priority = int(Priority)

    @property
    def title(self):  
        return self._title 
    @title.setter
    def title(self,title):
        self._title = title

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        self._author = author

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,status):
        self._status= bool(1)
    
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self,Priority):
        self._priority = int(Priority)
    
    def __lt__(self,other):
        return self.author < other.author

    def __str__(self):
        return f"{self._author}, {self._status}, {self.title}, {self.priority}"


file = open("SciFiLiBooks.txt")
books_list = []
for line in file:
    line = line.rstrip("\n")
    x =line.split(', ')
    p = Library(x[0], x[1], x[2], x[3])
    books_list.append(p)

books_linked_list = LinkedList()
for i in books_list:
    books_linked_list.append(Node(i))

books_linked_list.setCurr(books_linked_list.getHead())
while books_linked_list.getCurr() is not None:
    book = books_linked_list.getData()
    print(book.author)
    books_linked_list.goNext()

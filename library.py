#Final Program
#Library class and queu
#Sneha Patel
#Dec 11, 2023

class Library:
    def __init__(self,title,author,status,Priority):
        self._title = title
        self._author = author
        self._status= int(status)
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
        self._status= status
    
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self,Priority):
        self._priority = int(Priority)

    def __str__(self):
        return f"{self.author} : {self.title}, {self.status} "
        #return f"{self._title}, {self._author}, {self.priority}, {self.status}"

    def __lt__(self, other, criterion='author'):
        if criterion == 'author':
            return self._author < other._author
        elif criterion == 'title':
            return self._title < other._title
        else:
            # Default to author if an invalid criterion is provided
            return self._title < other._title
        
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, book):
        self.queue.append(book)
        #print(f"Book '{book.title}' has been returned and added to the queue.")

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty.")
    
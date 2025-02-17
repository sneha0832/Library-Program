class ReturnQueue:
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

#Final Program
#main program - Kind of like building a library software
#Sneha Patel
#Dec 11, 2023
from BT import binaryTree
from binNode import binNode
from library import Library
from library import Queue


file = open("SciFiLiBooks.txt")
books_list = []
for line in file:
    line = line.rstrip("\n")
    x =line.split(', ')
    p = Library(x[0], x[1], x[2], x[3])
    books_list.append(p)

tree = binaryTree()
for book in books_list:
    node = binNode(book)
    tree.insert(node)
while(True):
    print("1. List of all the books\n2. search book by author\n3. search book by title\n4. return book\n5. Take book\n6. fire emergency\n7. quit")
    Que = input('What do you want to do? ')
    if Que == '1':
        tree.traverseInOrder()
    elif Que == '2':
        Que3 = input('\nEnter author name: \n')
        #print('HI')
        result = tree.search(tree.root,Que3,'author')
        #print("Hi")
        if result:
            print(f"\nBooks by {Que3}:\n")
            while result:
                print(f"Title: {result.data.title}, Author: {result.data.author},  Status: {result.data.status}")
                result = tree.search(result.right,Que3,'author')
        else:
            print(f"\nNo books found by {Que3}.")

    elif Que == '3':
        Que4 = input('Enter book title: ')
        result = tree.search(tree.root,Que4,'title')
        if result:
            print(f"\nBooks by {Que4}:\n")
            while result:
                #print('1')
                print(f"Title: {result.data.title}, Author: {result.data.author},  Status: {result.data.status}")
                #print("3")
                result = tree.search(result.right, Que4,'title')
                #print("4")
        else:
            print(f"\nNo books found by {Que4}.")


    elif Que == '4':
        return_queue = Queue()
        while True:
            return_input = input("Enter the title of the book to return (or 'done'): ")
            if return_input.lower() == 'done':
                break
            return_queue.enqueue(return_input)

        while return_queue.queue:
            returned_book_title = return_queue.dequeue()
            book_found = False  # Flag to check if the book was found in the list

            for book in books_list:
                if book.title == returned_book_title:
                    book.status = 1
                    print(f"Checking in: {returned_book_title}, {book.status}")
                    print()
                    book_found = True
                    break  # Exit the loop once the book is found and updated

            if not book_found:
                print(f"Book '{returned_book_title}' not found in the library.")
        #for book in books_list:
           # print(f"{book.title} - Status: {book.status}")

    elif Que == "5":
        take_queue =  Queue()
        while True:
            take_input = input("Enter the name of the book (or 'done'): ")
            if take_input.lower() == 'done':
                break
            take_queue.enqueue(take_input)
        
        while take_queue.queue:
            take_book_title = take_queue.dequeue()
            book_found1 = False
        for book in books_list:
            if book.title == take_book_title:
                book.status = 0
                print(f"Checking out: {take_book_title}, {book.status}")
                print()
            book_found1 = True

        if not book_found1:
                print(f"Book '{take_book_title}' not found in the library.")
        
        
    elif Que == '6':
        print("\nFIRE EMERGENCY!")

        checked_in = []
        for book in books_list:
            #print(f"Book: {book.title}, Status: {book.status} , Priority: {book.priority}")
            if book.status == 1: 
                checked_in.append(book)

        checked_in.sort(key=lambda x: int(x.priority))

        print("Books to rescue:")
        number = 2
        for book in checked_in[:15]:
            print(f"Title: {book.title}, Priority: {book.priority}")
    


    elif Que == '7':
        books_list.sort(key=lambda x: str(x.title))
        for book in books_list:
            print(f"Book: {book.title}, Status: {book.status}")

#1. I used list beause I think it's easy to iterate and also to store data beacuse then I used it to make tree       
#2. For the tsak of sorting the reading file I have used a Binary tree. 
#   I think binary tree is best for searching and sorting data quickly. So, used it to for sorting and searching the file of books.
#3. I used a queue for book returns because it ensures a first-in, first-out order, providing a systematic and efficient way to process multiple return requests in the order they are initiated.
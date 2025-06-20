# SciFiLi - Science Fiction Library Management System

## Overview
SciFiLi is a library management program designed to efficiently store, search, check in/out, and sort books using appropriate data structures. This project demonstrates the application of various data structures and algorithms to manage a science fiction library effectively.

## Features
1. **Load Books from File:** Reads book data from a file and stores it in an internal data structure.
2. **Search Books:** Allows searching by title or author, displaying all books by a particular author and their check-in status.
3. **Check In/Out Books:** Enables librarians to check books in and out.
4. **Process Book Returns:** Simulates book returns where returned books are placed in a queue.
5. **Sort and Save Data:** At the end of the session, all books are sorted alphabetically by title and saved back to a file with their status.
6. **User Interface:** A simple text-based or GUI menu allows the user to interact with the system.

## Data Structures Used
1. **List:** Used for initial storage of book data because it is easy to iterate over and manipulate before structuring into a tree.
2. **Binary Search Tree (BST):** Chosen for sorting and searching books efficiently.
   - **Justification:** BST allows for quick insertions, deletions, and lookups, making it ideal for organizing book data.
3. **Queue:** Used to handle book returns in a first-in, first-out (FIFO) manner.
   - **Justification:** This ensures books are returned in the order they were placed, mimicking real-world return processes.

## Input File Format
Each line in the input file contains book details in the following format:
```
Title, Author, CheckInStatus, Priority
```
Example:
```
Watership Down, AdamsR, 0, 7
```
- **Title**: Name of the book
- **Author**: Name of the author
- **CheckInStatus**: Boolean (1 = checked in, 0 = checked out)
- **Priority**: Integer representing book importance (1 is the highest priority)

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SciFiLi.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SciFiLi
   ```
3. Run the program:
   ```bash
   python scifili.py
   ```




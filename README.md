Book Collection Manager

A simple command-line application for managing a collection of books using SQLite in Python. This tool allows users to add, view, update, and delete books from a database.

Features

Create and manage a database of books.
Perform CRUD (Create, Read, Update, Delete) operations on book records.
Interactive command-line menu for easy navigation.
Requirements

Python 3.x
SQLite (comes pre-installed with Python)
Installation

Clone the repository (if applicable) or download the book_collection_manager.py file.
Ensure Python is installed on your system. You can download it from python.org.
Usage

Open a terminal (or command prompt).
Navigate to the directory where you saved the book_collection_manager.py file.
Run the script using the following command:
bash
Copy code
python book_collection_manager.py
Follow the prompts in the interactive menu:
Add Book: Enter book details to add a new book.
View Books: Display all books in the collection.
Update Book: Modify the details of an existing book by its ID.
Delete Book: Remove a book from the collection by its ID.
Exit: Close the application.
Example

When running the application, you will see a menu like this:

markdown
Copy code
Menu:
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Exit
You can then select an option and follow the prompts to manage your book collection.

Notes

The application creates a SQLite database file named books.db in the same directory as the script.
Ensure you have the necessary permissions to read and write in the directory where the script is run.
License

This project is open-source and available for personal and educational use.

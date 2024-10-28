import sqlite3

def connect_db():
    """Connect to the SQLite database (or create it if it doesn't exist)."""
    conn = sqlite3.connect('books.db')
    return conn

def create_table(conn):
    """Create a table for storing book information."""
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                genre TEXT
            )
        ''')
    print("Table created successfully.")

def add_book(conn, title, author, year, genre):
    """Add a new book to the collection."""
    with conn:
        conn.execute('''
            INSERT INTO books (title, author, year, genre)
            VALUES (?, ?, ?, ?)
        ''', (title, author, year, genre))
    print(f"Added book: {title}")

def view_books(conn):
    """View all books in the collection."""
    cursor = conn.execute('SELECT * FROM books')
    books = cursor.fetchall()
    
    print("\nBooks in Collection:")
    for book in books:
        print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}, Genre: {book[4]}")

def update_book(conn, book_id, title, author, year, genre):
    """Update an existing book's information."""
    with conn:
        conn.execute('''
            UPDATE books
            SET title = ?, author = ?, year = ?, genre = ?
            WHERE id = ?
        ''', (title, author, year, genre, book_id))
    print(f"Updated book ID {book_id}.")

def delete_book(conn, book_id):
    """Delete a book from the collection."""
    with conn:
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    print(f"Deleted book ID {book_id}.")

def main():
    conn = connect_db()
    create_table(conn)

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            genre = input("Enter genre: ")
            add_book(conn, title, author, year, genre)

        elif choice == '2':
            view_books(conn)

        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year = input("Enter new year: ")
            genre = input("Enter new genre: ")
            update_book(conn, book_id, title, author, year, genre)

        elif choice == '4':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(conn, book_id)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()

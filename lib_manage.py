import pandas as pd                 
class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
class LibraryManager:
    def __init__(self):
        self.books = pd.DataFrame(columns=['Title', 'Author', 'Year', 'ISBN'])
        self.menu()
    def menu(self):
        while True:
            print('''
            1. View Books
            2. Add Book
            3. Remove Book
            4. Exit
            ''')
            choice = input("Enter your choice: ")
            if choice == '1':
                self.ViewBooks()
            elif choice == '2':
                self.AddBook()
            elif choice == '3':
                self.RemoveBook()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    def ViewBooks(self):
        if self.books.empty:
            print("No books available.")
        else:
            print(self.books)
    def AddBook(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = input("Enter publication year: ")
        isbn = input("Enter ISBN number: ")
        if isbn in self.books['ISBN'].values:
            print("A book with this ISBN already exists.")
            return
        else:
            new_book = Book(title, author, year, isbn)
            self.books.loc[len(self.books)] = [
                new_book.title,
                new_book.author,
                new_book.year,
                new_book.isbn
            ]
        print("Book added successfully.")  
    def RemoveBook(self):
        isbn = input("Enter ISBN number of the book to remove: ")
        if isbn in self.books['ISBN'].values:
            self.books = self.books[self.books['ISBN'] != isbn]
            print("Book removed successfully.")
        else:
            print("Book not found.")     
library = LibraryManager()

# library_management.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

    def is_available(self) -> bool:
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  
    def add_book(self, book: Book):
        self._books.append(book)

    def check_out_book(self, title: str):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title: str):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return
                else:
                    print(f"'{title}' is already available.")
                    return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)
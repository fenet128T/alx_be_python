class Book:
    """Base class for all books"""
    
    def __init__(self, title: str, author: str) -> None:
        """Initialize a book with title and author"""
        self.title = title
        self.author = author


class EBook(Book):
    """Derived class for electronic books"""
    
    def __init__(self, title: str, author: str, file_size: int) -> None:
        """Initialize an ebook with title, author, and file size"""
        super().__init__(title, author)  # Call parent class constructor
        self.file_size = file_size


class PrintBook(Book):
    """Derived class for printed books"""
    
    def __init__(self, title: str, author: str, page_count: int) -> None:
        """Initialize a print book with title, author, and page count"""
        super().__init__(title, author)  # Call parent class constructor
        self.page_count = page_count


class Library:
    """Library class that uses composition to manage books"""
    
    def __init__(self) -> None:
        """Initialize an empty library"""
        self.books = []
    
    def add_book(self, book) -> None:
        """Add a book to the library"""
        self.books.append(book)
    
    def list_books(self) -> None:
        """Print details of all books in the library"""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
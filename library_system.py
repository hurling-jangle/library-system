# library_system.py

from book import Book
from patron import Patron
from transaction import Transaction

# Create books
book1 = Book(101, "Introduction to Python", "John Doe")
book2 = Book(102, "Data Structures in Python", "Jane Smith")

# Create patrons
patron1 = Patron(201, "Alice")
patron2 = Patron(202, "Bob")

# Create transactions
transaction1 = Transaction(1001, book1, patron1)
transaction2 = Transaction(1002, book2, patron2)

# Display information
print("Transaction Information:")
transaction1.display_info()
print()
transaction2.display_info()

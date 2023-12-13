# transaction.py

from book import Book
from patron import Patron

class Transaction:
    def __init__(self, transaction_id, book, patron):
        self.transaction_id = transaction_id
        self.book = book
        self.patron = patron

    def display_info(self):
        print(f"Transaction ID: {self.transaction_id}")
        self.book.display_info()
        self.patron.display_info()

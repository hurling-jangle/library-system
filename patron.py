# patron.py

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name

    def display_info(self):
        print(f"Patron ID: {self.patron_id}")
        print(f"Name: {self.name}")

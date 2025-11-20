#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count  # internal storage

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")        


book = Book("And Then There Were None", 272)
print(book.title)        # Output: And Then There Were None
print(book.page_count)   # Output: 272

print(turn_page())  # Output: Flipping the page...wow, you read fast!
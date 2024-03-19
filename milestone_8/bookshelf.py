import random
from faker import Faker

class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

class Shelf:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

class Room:
    def __init__(self):
        self.shelves = {}
    def add_shelf(self, shelf):
        self.shelves.append(shelf)
        
    def by_cat(self, books):
        
        for book in books:
            if book.category in self.shelves.keys():
                self.shelves[book.category].add_book(book)
            else:
                self.shelves[book.category] = Shelf(book.category)                
                self.shelves[book.category].add_book(book)
                

    def sort_books_by_cat_and_title(self):
        self.shelves = dict(sorted(self.shelves.items()))
        for item in self.shelves.values():
            item.books.sort(key=lambda book: book.title)
            


fake = Faker()
books = set()
for _ in range(10):
  title = fake.catch_phrase()
  author = fake.name()
  category = random.choice(["Fiction", "Adventures", "Children"])
  books.add(Book(title, author, category))




room = Room()
room.by_cat(books)


room.sort_books_by_cat_and_title()


print("Books after sorting by title:")
for shelf in room.shelves.values():
  print(f"\nShelf: {shelf.name}")
  for book in shelf.books:
    print(f"- {book.title} by {book.author} ({book.category})")
import json
from catalog import Book

def load_books():
    with open("books.json", encoding="utf-8") as file:
        books = json.load(file)
        book_objects = []
        
        for book in books:
            book_object = Book(
                book['title'],
                book['author'],
                book['checked_out']
                )
            book_objects.append(book_object)
            
    return book_objects

def save_books(books):
    book_dicts = []
    for book in books:
        book_dict = {
            "title": book.title,
            "author": book.author,
            "checked_out": book.checked_out
        }
        book_dicts.append(book_dict)
        
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(book_dicts, file, indent=4)
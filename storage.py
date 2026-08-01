import json

def load_books():
    with open("books.json", encoding="utf-8") as file:
        books = json.load(file)
        
    return books

def save_books(book_list):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(book_list, file, indent=4)
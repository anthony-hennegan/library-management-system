def is_available(book):
    return not book["checked_out"]
    
def display_available_books(book_list):
    print("Available for Checkout")
    print("----------------------")
    for book in book_list:
        available = is_available(book)
        if available:
            print(f"{book['title']} by {book['author']}")
            
def display_checked_out_books(book_list):
    print("Currently Checked Out")
    print("----------------------")
    for book in book_list:
        available = is_available(book)
        if not available:
            print(f"{book['title']} by {book['author']}")
            
def count_available_books(book_list):
    available_book_count = 0
    for book in book_list:
        if is_available(book):
            available_book_count += 1
    return available_book_count

def search_book_by_title(title, book_list):
    title = title.strip().lower()
    found_book = False
    
    for book in book_list:
        if title == book['title'].lower():
            found_book = True
            
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            
            if not book['checked_out']:
                print("Available: Yes")
            else:
                print("Available: No")
                
            break
        
    if not found_book:
        print("Book not found.")
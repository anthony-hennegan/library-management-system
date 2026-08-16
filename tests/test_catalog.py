from catalog import Library, Book, update_book_title


def test_update_book_title():
    book1 = Book('book1', 'author1')
    book2 = Book('book2', 'author2')
    book3 = Book('book3', 'author3')
    
    book_list = [book1, book2, book3]
    
    library = Library('Test Library', book_list)
    new_title = 'Book One'
    
    result = update_book_title(library, book1.title, new_title)
    assert result is True
    
def test_update_book_title_failed_to_find():
    book1 = Book('book1', 'author1')
    book2 = Book('book2', 'author2')
    book3 = Book('book3', 'author3')
    
    book_list = [book1, book2, book3]
    library = Library('Test Library', book_list)
    new_title = 'Book One'
    
    result = update_book_title(library, 'wrong title', new_title)
    assert result is None
    
def test_update_book_title_falsy_title():
    book1 = Book('book1', 'author1')
    book2 = Book('book2', 'author2')
    book3 = Book('book3', 'author3')
    
    book_list = [book1, book2, book3]
    library = Library('Test Library', book_list)
    new_title = 'Book One'
    
    result = update_book_title(library, '', new_title)
    assert not result
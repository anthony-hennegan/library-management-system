from catalog import Library, Book



def test_find_book_in_library():
    book1 = Book('book1', 'author1')

    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.find_book(book1.title)

    assert result is book1
    
def test_find_book_not_in_library():
    book1 = Book('book1', 'author1')
    book_list = [book1]

    library = Library('Test Library', book_list)
    
    result = library.find_book('book3')
    
    assert result is None
    
def test_add_book_to_library():
    book1 = Book('book1', 'author1')
    book_list = [book1]

    library = Library('Test Library', book_list)
    
    book2 = Book('book2', 'author2')
    result = library.add_book(book2)
    
    assert result is book2
    assert book2 in library.books
    
def test_remove_book_in_library():
    book1 = Book('book1', 'author1')
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.remove_book(book1)
    
    assert result is book1
    assert book1 not in library.books

def test_remove_book_not_in_library():
    book1 = Book('book1', 'author1')
    book2 = Book('book2', 'author2')
    book_list = [book1, book2]
    
    library = Library('Test Library', book_list)
    book = library.find_book('book3')
    result = library.remove_book(book)
    
    assert result is None
    
def test_checkout_book_in_library():
    book1 = Book('book1', 'author1')
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.checkout_book(book1.title)
    
    assert result is book1
    assert book1.checked_out is True
    
def test_checkout_book_not_in_library():
    book1 = Book('book1', 'author1')
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.checkout_book('book3')
    
    assert result is None
    
def test_checkout_book_already_checked_out():
    book1 = Book('book1', 'author1', True)
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.checkout_book(book1.title)
    
    assert result is False
    assert book1.checked_out is True
    
def test_return_book_in_library():
    book1 = Book('book1', 'author1', True)
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.return_book(book1.title)
    
    assert result is book1
    assert book1.checked_out is False
    
def test_return_book_not_in_library():
    book1 = Book('book1', 'author1', True)
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.return_book('book3')
    
    assert result is None

def test_return_book_already_returned():
    book1 = Book('book1', 'author1')
    book_list = [book1]

    library = Library('Test Library', book_list)
    result = library.return_book(book1.title)
    
    assert result is False
    assert book1.checked_out is False
    
def test_find_books_by_author():
    author = 'author1'
    book1 = Book('book1', author)
    book2 = Book('book2', author)
    book3 = Book('book3', 'author2')
    
    book_list = [book1, book2, book3]

    library = Library('Test Library', book_list)
    result = library.find_books_by_author(author)
    
    assert result == [book1, book2]

def test_find_books_by_author_with_no_books():
    author = 'author1'
    book1 = Book('book1', author)
    book2 = Book('book2', author)
    book3 = Book('book3', author)
    
    book_list = [book1, book2, book3]

    library = Library('Test Library', book_list)
    result = library.find_books_by_author('author2')
    
    assert result == []
    

    
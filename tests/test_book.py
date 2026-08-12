from catalog import Book


def test_available_book_can_be_checked_out():
    book = Book("book1", "author1")

    result = book.checkout()

    assert result is True
    assert book.checked_out is True
    
def test_unavailable_book_cannot_be_checked_out():
    book = Book("book1", "author1", True)

    result = book.checkout()

    assert result is False
    assert book.checked_out is True
    
    
def test_checked_out_book_can_be_returned():
    book = Book("book1", "author1", True)
    
    result = book.return_book()
    
    assert result is True
    assert book.checked_out is False
    
def test_unchecked_out_book_cannot_be_returned():
    book = Book("book1", "author1")
    
    result = book.return_book()
    
    assert result is False
    assert book.checked_out is False
    
    
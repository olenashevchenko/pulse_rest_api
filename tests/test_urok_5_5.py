import pytest
from pulse_rest_api.pulse_rest_api.models.books import Book

test_data = {
    Book(title = 'koala', author = 'Koala'),
    Book(title = 'title', author = 'author')
}

@pytest.mark.parametrize("book", test_data, ids = [repr(b) for b in test_data])
def test_book_creation(app, book):
    book = Book (title = 'koala', author = 'Koala')
    response = app.create_object(book)
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()

#def test_book_creation_no_author(app):
    #book = Book(title='koala')
    #response = app.create_object(book)
    # Verification
    #assert response.status_code == 201
    #assert response.json() == book.get_dict_with_id()

if __name__ == "__main__":
    pytest.main()


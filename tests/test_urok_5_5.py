
from pulse_rest_api.pulse_rest_api.models.books import Book

def test_book_creation(app):
    book = Book (title = 'koala', author = 'Koala')
    response = app.create_object(book)
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()

def test_book_creation_no_author(app):
    book = Book(title='koala')
    response = app.create_object(book)
    assert response.status_code == 201
    assert response.json() == book.get_dict_with_id()
    #Verification
    #app.assertEqual (response.status_code, 201)
    #self.client.get_book (book)
    #app.assertEqual (response.json(), book.get_dict_with_id())

if __name__ == "__main__":
    pytest.main()

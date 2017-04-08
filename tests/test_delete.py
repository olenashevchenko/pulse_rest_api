import pytest
from models.books import Book

@pytest.fixture
def book(app):
    b = Book(title="For del", author="For del")
    r = app.create_object(b)
    return(b)

def test_delete(app, book):
    response = app.delete_object(book)
    assert response.status_code == 204


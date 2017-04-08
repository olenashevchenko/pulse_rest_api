import unittest
from urok_5.pulse_api_client import BookPulseRestAPI

from urok_5.models import Book

class BookRestAPITests(unittest.TestCase):
    def setUp(self):
        self.client = BookPulseRestAPI("books")

    def test_book_creation(self):
        book = Book (title = 'koala', author = 'Koala')
        response = self.client.create_book(book)

        #Verification
        self.assertEqual (response.status_code, 201)
        #self.client.get_book (book)
        self.assertEqual (response.json(), book.get_dict_with_id())

if __name__ == "__main__":
    unittest.main()


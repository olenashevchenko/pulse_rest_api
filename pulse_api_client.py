import requests
class BookPulseRestAPI:
    def __init__ (self, resourse):
        self.host = "pulse-rest-testing.herokuapp.com"
        self.base_url = "http://{}/".format(self.host)
        self.url = self.base_url + resourse + "/"

    def create_book(self, book):
        book_data = book.get_dict()
        book_data = {'title': book.title, 'author': book.author}
        url = self.base_url + "books/"
        response = requests.post(url, data=book_data)
        book.set_id(response.json()["id"])
        return response

    def get_books(self):
        pass


    def get_book(self, book):
        pass

    def modify_book(self, book):
        pass
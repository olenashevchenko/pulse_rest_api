import requests

class PulseRestAPI():
    def __init__(self, resourse):
        self.host = "pulse-rest-testing.herokuapp.com"
        self.base_url = "http://{}/".format(self.host)
        self.url = self.base_url + resourse + "/"

    def create_object(self, obj):
        obj_data = obj.get_dict_without_id()
        response = requests.post(self.url, data=obj_data)
        if response.status_code == 201:
            obj.set_id(response.json()["id"])
        return response


    def get_objects(self):
        pass

    def modify_object(self):
        pass

    def delete_object(self, obj):
        obj_id = obj.id
        response = requests.delete(self.url + str(obj_id) + "/")
        return response
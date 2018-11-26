import requests

from base import Base

class List(Base):
    def __init__(self, list_id, name):
        self.list_id = list_id
        self.name = name
        print('List with {} id and name {} is created'.format(list_id, name))

    def create_card(self, name):
        url = "https://api.trello.com/1/cards"

        querystring = {
            'idList': self.list_id
        }
        querystring.update({'name': name})
        response = requests.request("POST", url, params={**querystring, **self.get_token()})
        return response

    def get_all_cards(self):
        url = 'https://api.trello.com/1/lists/{}/cards'.format(self.list_id)
        response = requests.get(url, params=self.get_token()).json()
        return_dict = dict()
        for object in response:
            return_dict[object['name']] = object['id']
        return return_dict
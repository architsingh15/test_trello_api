import requests
from base import Base

class Board(Base):
    def __init__(self, board_id, name):
        self.board_id = board_id
        self.name = name
        print('Board with {} id created and name {}'.format(board_id, name))

    def get_all_cards(self):
        payload = {
            'fields': 'name'
        }
        r = requests.get('https://api.trello.com/1/boards/{}/cards'.format(self.board_id), params={**payload, **self.get_token()})
        cards_content = r.json()
        content_cards = dict()
        for content in cards_content:
            content_cards[content['name']] = content['id']
        return content_cards

    def get_all_list(self):
        r = requests.get('https://api.trello.com/1/boards/ZR96NzME/lists', params=self.get_token())
        list_data = r.json()
        list_ids = dict()
        for list in list_data:
            list_ids[list['name']] = list['id']
        return list_ids
import pprint

import requests

from base import Base
from board import Board
from list import List

pp = pprint.PrettyPrinter(indent=4)

class CreateObjectFactory(Base):

    def create_board(self, name):
        url = "https://api.trello.com/1/boards/"
        querystring = {
            "name": name
        }
        response = requests.request("POST", url, params={**querystring, **self.get_token()})
        board_id = response.json()['id']
        return Board(board_id, name)

    def create_list(self, board_id, list_name):
        url = "https://api.trello.com/1/lists"
        querystring = {
            "idBoard": board_id
        }
        querystring.update({"name": list_name})
        response = requests.request("POST", url, params={**querystring, **self.get_token()})
        return List(board_id, list_name)
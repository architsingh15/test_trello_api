import requests

from base import Base

class Card(Base):
    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name
        print('Card created with id {} and name {}'.format(card_id, name))

    def move_to_list(self, list_id):
        url = 'https://api.trello.com/1/cards/{}'.format(self.card_id)
        payload = self.get_token()
        payload.update({'idList': list_id})
        r = requests.put(url, data=payload)
        return r

    def add_comment(self, comment):
        comment_url = "https://api.trello.com/1/cards/{}/actions/comments".format(self.card_id)
        querystring = self.get_token()
        querystring.update({
            "text": comment
        })
        response = requests.request("POST", comment_url, params=querystring)

    def list_details(self):
        payload = self.get_token()
        url = "https://api.trello.com/1/cards/{}/list".format(self.card_id)
        r = requests.get(url, params=payload)
        content = r.json()
        return {
            content['id']: content['name']
        }
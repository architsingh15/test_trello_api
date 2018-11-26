import datetime
import unittest

from board import Board
from card import Card
from factory import CreateObjectFactory


class TestTrelloAPIMethods(unittest.TestCase):

    def test_assignment_1(self):
        now = datetime.datetime.now().time()
        date = datetime.datetime.now().date()
        aruba_board = Board('ZR96NzME', 'Aruba Python')

        card_details = aruba_board.get_all_cards()
        list_details = aruba_board.get_all_list()

        archit_card_id = card_details['Archit']
        archit_card = Card(archit_card_id, 'Archit')
        archit_card.move_to_list(list_details['1st Round'])
        archit_card.add_comment('Moved to 1st round by Archit {} - {}'.format(date, now))
        archit_card.move_to_list(list_details['2nd Round'])
        archit_card.add_comment('Moved to 2nd round by Archit {} - {}'.format(date, now))
        archit_card.move_to_list(list_details['Shortlisted'])
        archit_card.add_comment('Moved to Shortlisted round by Archit {} - {}'.format(date, now))

        sampath_card_id = card_details['Sampath']
        sampath_card = Card(sampath_card_id, 'Sampath')

        sampath_list = sampath_card.list_details()
        for id, name in sampath_list.items():
            sampath_list_name = name

        sampath_card_id = card_details['Sampath']
        sampath_card = Card(sampath_card_id, 'Sampath')

        if sampath_list_name == "Rejected":
            sampath_card.add_comment('Card in rejected list. Ignored by Archit {} - {}'.format(date, now))
        else:
            sampath_card.move_to_list(list_details['Rejected'])
            sampath_card.add_comment('Moved to Rejected by Archit {} - {}'.format(date, now))

    def test_assignment_2(self):
        create_object = CreateObjectFactory()
        test_board = create_object.create_board('Test Board')
        list_list = ['Scheduled', '1st Round', '2nd Round', 'Shortlisted', 'Rejected']

        list_objects_list = []

        for list in list_list:
            list_objects_list.append(create_object.create_list(test_board.board_id, list))

        for obj in list_objects_list:
            obj.create_card('Archit')

        card_details = list_objects_list[0].get_all_cards()

        for name, id in card_details.items():
            card_object = Card(id, name)
            card_object.move_to_list(list_objects_list[1].list_id)

if __name__ == '__main__':
    unittest.main()
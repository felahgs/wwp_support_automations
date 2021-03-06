import sys, os, re

from trello import TrelloClient


class TrelloApi():
    def __init__(self):
        # https://trello.com/app-key
        client = TrelloClient(
            api_key='ebb32a0fd1772ad3a9a99815f8a39b02',
            api_secret='353b7821984734f5a6d97f268790a53271eb45dd15c049ebe54b539fc11710a4',
        )

        self.all_boards = client.list_boards()
        self.wls_board = self.all_boards[1]
        self.my_lists = self.wls_board.list_lists()

    def get_done_cards(self, days):
        """Return all cards marked as done from a given list of dates"""
        done_sources = []
        print('Searching Trello cards..\n')
        for list in self.my_lists:
            for card in list.list_cards(card_filter='all'):
                if "Done" in card.name: 
                    name = card.name.split()[0]
                    date = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{2,4}')
                    date = date.findall(card.name)[0]
                    # print(name, date)
                    if date in days:
                        # done_sources.append(name + ' ' + date)
                        done_sources.append(name)
                    # exit(0)
                    # print(card.name)
        return done_sources

    def get_done_cards_obj(self, days, filter):
        """Return all cards marked as done from a given list of dates"""
        done_sources = []
        print('Searching Trello cards..\n')
        for list in self.my_lists:
            for card in list.list_cards(card_filter=filter):
                if (("Done" in card.name) or ("Moved" in card.name)): 
                    name = card.name.split()[0]
                    date = re.compile('[0-9]{2}/[0-9]{2}/[0-9]{2,4}')
                    date = date.findall(card.name)
                    if len(date) > 0:
                        date = date[0]
                    else:
                        continue
                    # print(name, date)
                    if date in days:
                        # done_sources.append(name + ' ' + date)
                        done_sources.append(card)
                    # exit(0)
                    # print(card.name)
        return done_sources

    def get_list(self, name):
        for list in self.my_lists:
            if name in list.name:
                return list

    def get_all_cards(self, filter='open'):
        """Return all cards from the board"""
        print('Searching Trello cards..\n')
        done_sources = []
        for list in self.my_lists:
            for card in list.list_cards(card_filter=filter):
                name = card.name.split()[0]
                done_sources.append(card)
        return done_sources

    def get_all_open_cards(self):
        """Return all cards from the board"""
        print('Searching Trello cards..\n')
        done_sources = []
        for list in self.my_lists:
            for card in list.list_cards(card_filter='open'):
                name = card.name.split()[0]
                done_sources.append(card)
        return done_sources
    
    def get_card(self, name):
        """Return the first card that matches the card name with the selected string"""
        for list in self.my_lists:
            for card in list.list_cards(card_filter='all'):
                if name in card.name:
                    return card
        return 'None'

    def get_member(self, name):
        """Return the first member that matches the chosen name string"""
        members = self.wls_board.get_members()
        for member in members:
            if name in member.full_name:
                return member
        return 'None'

    def get_all_members(self):
        """Return a list with all the members from the board"""
        members = self.wls_board.get_members()
        return members

    def get_label(self, name):
        """Return the first label that matches the chosen name string"""
        label_list = self.wls_board.get_labels()
        for label in label_list:
            if name in label.name: 
                return label
    
    def get_all_labels(self):
        """Return all labels from the board"""
        labels = self.wls_board.get_labels
        return labels
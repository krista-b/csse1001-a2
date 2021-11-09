#!/usr/bin/env python3
"""
Assignment 2 - Sleeping Coders
CSSE1001/7030
Semester 2, 2019
"""

import random

__author__ = "Krista Bradshaw: 45285143"


class Card:
    '''DS'''
        
    def play(self, player, game):
        '''player: Player, game: a2_support.CodersGame'''
        #get the players deck
        players_deck = player.get_hand()
        #find where the card (self) occurs in the deck, see .index()
        card_slot = players_deck.get_cards().index(self)
        #remove the card at the above index from the deck using remove_card
        players_deck.remove_card(card_slot)
        #get a new card from game.pick_card()
        new_card = game.pick_card()
        #add to players deck
        players_deck.add_card(new_card)
        #set action to no action, game.set_action('')
        game.set_action('NO_ACTION')
        

    def action(self, player, game, slot):
        '''player: Player, game: a2_support.CodersGame, slot:int'''
        pass

    def __str__(self):
        '''DS'''
        return 'Card()'

    def __repr__(self):
        '''DS'''
        return str(self)
    
class NumberCard(Card):
    '''DS'''

    def __init__(self, number):
        '''DS'''
        self._number = number

    def play(self, player, game):
        '''DS'''
        super().play()
        game.set_action('NO_ACTION')
        
    def get_number(self):
        '''DS'''
        return self._number

    def __str__(self):
        return 'NumberCard({})'.format(self._number)
    
    def __repr__(self):
        return str(self)

class CoderCard(Card):
    '''DS'''

    def __init__(self, name):
        '''DS'''
        self._name = name
        
    def get_name(self):
        '''DS'''
        return self._name

    def __str__(self):
        return 'CoderCard({})'.format(self._name)
    
    def __repr__(self):
        return str(self)

class TutorCard(Card):
    '''DS'''

    def __init__(self, name):
        '''DS'''
        self._name = name
        
    def get_name(self):
        '''DS'''
        return self._name

    def play(self, player, game):
        '''DS'''
        super().play()
        #override with specific tutor action
    
    def __str__(self):
        return 'TutorCard({})'.format(self._name)
    
    def __repr__(self):
        return str(self)
    
class KeyboardKidnapperCard(Card):
    '''DS'''

    def play(self, player, game):
        '''DS'''
        super().play()
        #override with specific kidnapper action
        
    def __str__(self):
        return 'KeyboardKidnapperCard()'

    def __repr__(self):
        return str(self)

class AllNighterCard(Card):
    '''DS'''

    def play(self, player, game):
        '''DS'''
        super().play()
        #override with specific allnighter action
        
    def __str__(self):
        return 'AllNighterCard()'

    def __repr__(self):
        return str(self)

class Deck:
    '''DS'''
    
    def __init__(self, starting_cards=None): 
        '''DS'''
        if starting_cards == None:
            self._cards = []
        if starting_cards != None:
            self._cards = starting_cards
            
    def get_cards(self):
        '''DS'''
        return self._cards

    def get_card(self, slot):
        '''DS'''
        return self._cards[slot]

    def top(self):
        '''DS'''
        return self._cards[-1]

    def remove_card(self, slot):
        '''DS'''
        self._cards.pop(slot)
        
    def get_amount(self):
        '''DS'''
        return len(self._cards)

    def shuffle(self):
        '''DS'''
        return random.shuffle(self._cards)

    def pick(self, amount: int=1):
        '''DS'''
        cards_picked = []
        count = 0
        while count < amount:
            if self._cards != []:
                add = self._cards.pop()
                cards_picked.append(add)
                count += 1
        return cards_picked

    def add_card(self, card):
        '''DS'''
        return self._cards.append(card)

    def add_cards(self, cards):
        '''DS'''
        return self._cards.extend(cards)

    def copy(self, other_deck):
        '''DS'''
        otherdeck = Deck.get_cards(other_deck)
        return self._cards.extend(otherdeck)
                                 
    def __str__(self):
        '''DS'''
        return 'Deck({})'.format(str(self._cards)[1:-1])

    def __repr__(self):
        '''DS'''
        return str(self)

class Player:
    '''DS'''
    def __init__(self, name):
        '''DS'''
        self._name = name
        super().__init__()
        self._hand = Deck() 
        self._coders = Deck() 
        
    def get_name(self):
        '''DS'''
        return self._name
    
    def get_hand(self):
        '''DS'''
        return self._hand 
    
    def get_coders(self):
        '''DS'''
        return self._coders 
    
    def has_won(self):
        '''DS'''
        coder_cards = self._coders.get_cards()
        if len(coder_cards) >= 4:
            return True
        return False
    
    def __str__(self):
        '''DS'''
        return 'Player({}, {}, {})'.format(self._name, self._hand, self._coders)

    def __repr__(self):
        '''DS'''
        return str(self)
    
def main():
    '''DS'''
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

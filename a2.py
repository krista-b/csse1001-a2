#!/usr/bin/env python3
"""
Assignment 2 - Sleeping Coders
CSSE1001/7030
Semester 2, 2019
"""

import random 

__author__ = "Krista Bradshaw: 45285143"


class Card:
    """
    Card(): A class to represent the types of cards in the game.
    """
    def play(self, player, game):
        """Called when the player plays a Card; removes the card
            from the player's hand and replaces it with a new card
            from the pickup pile.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
        """
        card_slot = player.get_hand().get_cards().index(self)
        player.get_hand().remove_card(card_slot)
        new_card = game.pick_card()[0]
        player.get_hand().add_card(new_card)
        game.set_action('NO_ACTION')
        
    def action(self, player, game, slot):
        """Called when an action of a special card is performed. 

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
            slot(int): Index position of card within deck.
        """
        pass

    def __str__(self):
        """Returns the string respresentation of the Card.

        Return:
            Card(str): The string representation of the Card.
        """
        return 'Card()'

    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)
    
class NumberCard(Card):
    """
    NumberCard(): A class to represent the Number Card type.
    """
    def __init__(self, number):
        """Construct a NumberCard Card based on an integer.

        Parameters:
            number(int): number associated with the NumberCard.
        """
        self._number = number

    def play(self, player, game):
        """Called when the player plays a NumberCard.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
        """
        super().play(player, game)
        game.next_player()
        
    def get_number(self):
        """Return the number associated with the NumberCard.

        Return:
            number(int): The number associated with the NumberCard. 
        """
        return self._number
    
    def __str__(self):
        """Returns the string respresentation of the NumberCard.
            NumberCard(number)

        Return:
            NumberCard(str): The string representation of the NumberCard.
        """
        return 'NumberCard({})'.format(self._number)
    
    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)

class CoderCard(Card):
    """
    CoderCard(): A class to represent the Coder Card type.
    """
    def __init__(self, name):
        """Construct a CoderCard Card based on a name.

        Parameters:
            name(str): name associated with the CoderCard.
        """
        self._name = name

    def play(self, player, game):
        """Called when the player plays a CoderCard and sets action accordingly.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
        """
        game.set_action('NO_ACTION')
        
    def get_name(self):
        """Return the name associated with the CoderCard.

        Return:
            name(str): The name associated with the CoderCard. 
        """
        return self._name

    def __str__(self):
        """Returns the string respresentation of the CoderCard.
            CoderCard(name)

        Return:
            CoderCard(str): The string representation of the CoderCard.
        """
        return 'CoderCard({})'.format(self._name)
    
    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)

class TutorCard(Card):
    """
    TutorCard(): A class to represent the Tutor Card type.
    """
    def __init__(self, name):
        """Construct a TutorCard Card based on an name.

        Parameters:
            name(str): name associated with the TutorCard.
        """
        self._name = name
        
    def play(self, player, game):
        """Called when the player plays a TutorCard and sets action accordingly.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
        """
        super().play(player, game)
        game.set_action('PICKUP_CODER')

    def action(self, player, game, slot):
        """Called when a TutorCard is played; select a coder from the pile.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
            slot(int): Index position of card within deck.
        """
        player.get_coders().add_card(game.get_sleeping_coder(slot))
        game.set_sleeping_coder(slot, None)
        game.set_action('NO_ACTION')
        game.next_player()
        
    def get_name(self):
        """Return the name associated with the TutorCard.

        Return:
            name(str): The name associated with the TutorCard. 
        """
        return self._name
    
    def __str__(self):
        """Returns the string respresentation of the TutorCard.
            TutorCard(name)

        Return:
            TutorCard(str): The string representation of the TutorCard.
        """
        return 'TutorCard({})'.format(self._name)
    
    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)
    
class KeyboardKidnapperCard(Card):
    """
    KeyboardKidnapperCard(): A class to represent the Keyboard Kidnapper Card type.
    """
    def play(self, player, game):
        """Called when the player plays a KeyboardKidnapperCard
            and sets action accordingly.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
        """
        super().play(player, game)
        game.set_action('STEAL_CODER')

    def action(self, player, game, slot):
        """Called when a KeyboardKidnapperCard is played;
            select a coder from another player's hand.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
            slot(int): Index position of card within deck.
        """
        #get selected card and add to current players deck
        game.current_player().get_coders().add_card(player.get_coders().get_card(slot))
        player.get_coders().remove_card(slot)
        game.set_action('NO_ACTION')
        game.next_player()
        
    def __str__(self):
        """Returns the string respresentation of the KeyboardKidnapperCard.

        Return:
            KeyboardKidnapper(str): The string representation of
                the KeyboardKidnapperCard.
        """
        return 'KeyboardKidnapperCard()'

    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)

class AllNighterCard(Card):
    """
    AllNighterCard(): A class to represent the All Nighter Card type.
    """
    def play(self, player, game):
        """Called when the player plays a AllNighterCard
            and sets action accordingly.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
        """
        super().play(player, game)
        game.set_action('SLEEP_CODER')

    def action(self, player, game, slot):
        """Called when a AllNighterCard is played;
            select a coder from another player's hand.

        Parameters:
            player(Player): The player associated with the card.
            game(a2_support.CodersGame): The game being played.
            slot(int): Index position of card within deck.
        """
        selected_coder = player.get_coders().get_card(slot)

        for empty_slot,coder in enumerate(game.get_sleeping_coders()):
            #index each sleeping coder in the coders deck
            if game.get_sleeping_coder(empty_slot) is None:
                #find first empty slot in sleeping coders deck
                #add sleeping coder to it
                game.set_sleeping_coder(empty_slot, selected_coder)
            
        player.get_coders().remove_card(slot)
        game.set_action('NO_ACTION')
        game.next_player()
        
    def __str__(self):
        """Returns the string respresentation of the AllNighterCard.

        Return:
            AllNighterCard(str): The string representation of the AllNighterCard.
        """
        return 'AllNighterCard()'

    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)

class Deck:
    """
    Deck(): A class to represent the deck; a collection of order cards.
    """
    def __init__(self, starting_cards=None): 
        """Construct a deck based on a list of starting cards.

        Parameters:
            starting_cards(List[Card]): list of Cards within the deck.
        """
        if starting_cards == None:
            self._cards = []
        else:
            self._cards = starting_cards
            
    def get_cards(self):
        """Return the list of cards within the deck.
      
        Return:
            cards(List[Card]): The list of cards within the deck. 
        """
        return self._cards

    def get_card(self, slot):
        """Return the card at a particular slot within the deck.

        Parameters:
            slot(int): Index position of card within deck.
            
        Return:
            card(Card): The card at a particular slot within the deck. 
        """
        return self._cards[slot]

    def top(self):
        """Return the card on the top of the deck (end of the list).

        Return:
            card(Card): The card on the top of the deck. 
        """
        return self._cards[-1]

    def remove_card(self, slot):
        """Remove the card at a particular slot from the deck.

        Parameters:
            slot(int): Original index position of card within deck.
        """
        self._cards.pop(slot)
        
    def get_amount(self):
        """Return the amount of cards within the deck (length of the list of cards).

        Return:
            amount(int): The amount of cards within the deck. 
        """
        return len(self._cards)

    def shuffle(self):
        """Shuffles the order of the cards within the deck."""
        random.shuffle(self._cards)

    def pick(self, amount: int=1):
        """Return the list of cards of a particular amount
            picked from the top of the deck.

        Return:
            cards(List[Card]): The list of cards picked from the deck.
        """
        cards_picked = []
        count = 0
        while count < amount:
            if self._cards != []:
                #loop over the list, adding each card until amount of cards is reached.
                cards_picked.append(self._cards.pop())
                count += 1
        return cards_picked

    def add_card(self, card):
        """Add a particular card to the original deck.

        Parameters:
            card(Card): The card to be added to the deck.
        """
        self._cards.append(card)

    def add_cards(self, cards):
        """Add a particular list of cards to the original deck.

        Parameters:
            cards(List[Card]): The list of cards to be added to the deck.
        """
        self._cards.extend(cards)

    def copy(self, other_deck):
        """Add a particular deck to the original deck.

        Parameters:
            other_deck(Deck): The deck whose cards are to be added
                to the original deck.
        """
        self._cards.extend(Deck.get_cards(other_deck))
                                 
    def __str__(self):
        """Returns the string respresentation of the deck.
            Deck(List[Card])

        Return:
            Deck(str): The string representation of the deck.
        """
        return 'Deck({})'.format(str(self._cards)[1:-1])

    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)

class Player:
    """
    Player(): A class to represent the a player in the game.
    """
    def __init__(self, name):
        """Construct a player based on a name.

        Parameters:
            name(str): name belonging to the player. 
        """
        self._name = name
        super().__init__()
        self._hand = Deck() 
        self._coders = Deck() 
        
    def get_name(self):
        """Return the name associated with the player.

        Return:
            name(str): The name associated with player. 
        """
        return self._name
    
    def get_hand(self):
        """Return the deck of cards held by the player.
            
        Return:
            hand(Deck): The deck of cards held by the player.
        """
        return self._hand 
    
    def get_coders(self):
        """Return the deck of CoderCards held by the player.
            
        Return:
            coders(Deck): The deck of CoderCards held by the player.
        """
        return self._coders 
    
    def has_won(self):
        """Called when the player has won the game.
                Player has won when their deck contains 4 CoderCards.

        Return:
            (bool): True when player has won, False when player has not won.
        """
        return self._coders.get_amount() >= 4
    
    def __str__(self):
        """Returns the string respresentation of the player.
            Player(name, hand, coders)

        Return:
            player(str): The string representation of the player.
        """
        return 'Player({}, {}, {})'.format(self._name, self._hand, self._coders)

    def __repr__(self):
        """Returns the same as the corresponding str method."""
        return str(self)
    
def main():
    """Instructs the user to run the associated GUI file instead
        in order to lay the 'Sleeping Coders' game."""
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

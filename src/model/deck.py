from src.model.card import Card
from random import shuffle


class Deck(object):
    cards = []

    def __init__(self, num_deck: int):
        """
        Represents the deck(s) used for the blackjack game. Games typically utilize 6-8 decks.
        :param num_deck: the number of decks used in the game
        :rtype: object
        """
        self.build_deck(num_deck)

    def build_deck(self, num_deck):
        """
        Initializes the cards in the deck based on the number of decks you want to play with.
        :param num_deck: the number of decks used for the game
        :return: n/a
        """
        self.cards = []
        i = 0
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
        suits = ["spades", "clubs", "diamonds", "hearts"]
        while i < num_deck:
            for rank in ranks:
                for suit in suits:
                    card = Card(rank, suit)
                    self.cards.append(card)
            i += 1
        self.shuffle()

    def shuffle(self):
        """
        Shuffles the cards in the deck.
        :return: n/a
        """
        shuffle(self.cards)

    def draw(self):
        """
        Pops the card at the end of the list of cards.
        :return: a Card object
        """
        return self.cards.pop()

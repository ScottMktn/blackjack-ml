from src.model.card import Card


class Dealer(object):
    def __init__(self):
        """
        Represents the dealer at a blackjack table.
        """
        self.hand = []

    def add_card(self, card: Card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand.clear()



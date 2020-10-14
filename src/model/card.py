class Card(object):
    def __init__(self, rank: type, suit: str) -> object:
        """
        Represents a single card in a standard 52 card deck.
        :rtype: object
        """
        self.rank = rank
        self.suit = suit

    def describe(self):
        return f"The {self.rank} of {self.suit}."


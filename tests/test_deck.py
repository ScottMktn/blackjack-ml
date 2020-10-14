from unittest import TestCase
from src.model.deck import Deck
from src.model.card import Card


class TestDeck(TestCase):
    def setUp(self):
        self.test_deck_one = Deck(1)
        self.test_deck_two = Deck(6)

    def test_init_deck(self):
        self.assertEqual(len(self.test_deck_one.cards), 52)
        self.assertEqual(len(self.test_deck_two.cards), 312)

    def test_all_cards_in_deck(self):
        # Get the card descriptions
        deck_one_described = []
        for card in self.test_deck_one.cards:
            deck_one_described.append(card.describe())

        # Build a test deck
        test_cards = []
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
        suits = ["spades", "clubs", "diamonds", "hearts"]
        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                test_cards.append(card)

        # Check if all of the cards in the test desk are in test_deck_one
        for card in test_cards:
            self.assertIn(card.describe(), deck_one_described)

    def test_build_deck(self):
        self.assertEqual(len(self.test_deck_one.cards), 52)
        self.test_deck_one.build_deck(3)
        self.assertEqual(len(self.test_deck_one.cards), 156)



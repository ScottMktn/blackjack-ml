from unittest import TestCase
from src.model.dealer import Dealer
from src.model.card import Card


class TestDealer(TestCase):
    def setUp(self):
        self.test_dealer = Dealer()
        self.test_card_one = Card(3, "spades")
        self.test_card_two = Card("ace", "diamonds")
        self.test_card_three = Card(4, "hearts")

    def test_add_card(self):
        self.assertEqual(len(self.test_dealer.hand), 0)
        self.test_dealer.add_card(self.test_card_one)
        self.assertEqual(len(self.test_dealer.hand), 1)
        self.assertEqual(self.test_dealer.hand[0].describe(), "The 3 of spades.")

    def test_clear_hand(self):
        self.test_add_card()
        self.assertEqual(len(self.test_dealer.hand), 1)
        self.test_dealer.clear_hand()
        self.assertEqual(len(self.test_dealer.hand), 0)
from unittest import TestCase
from src.model.card import Card


class TestCard(TestCase):
    def setUp(self):
        self.test_card_one = Card(3, "spades")
        self.test_card_two = Card("ace", "diamonds")

    def test_card_init(self):
        self.assertEqual(self.test_card_one.rank, 3)
        self.assertEqual(self.test_card_one.suit, "spades")
        self.assertEqual(self.test_card_two.rank, "ace")
        self.assertEqual(self.test_card_two.suit, "diamonds")

    def test_describe(self):
        self.assertEqual(self.test_card_one.describe(), "The 3 of spades.")
        self.assertEqual(self.test_card_two.describe(), "The ace of diamonds.")

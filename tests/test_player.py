from unittest import TestCase
from src.model.player import Player
from src.model.card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.test_player_one = Player(1000)
        self.test_player_two = Player(0)
        self.test_card_one = Card(3, "spades")
        self.test_card_two = Card("ace", "diamonds")
        self.test_card_three = Card(4, "hearts")

    def test_invalid_player(self):
        with self.assertRaises(ValueError):
            Player(-1)

    def test_make_bet(self):
        self.assertEqual(self.test_player_one.bet, 0)
        self.test_player_one.make_bet(200)
        self.assertEqual(self.test_player_one.bet, 200)
        self.assertEqual(self.test_player_one.balance, 800)

    def test_make_bet_error(self):
        with self.assertRaises(ValueError):
            self.test_player_one.make_bet(2000)
        with self.assertRaises(ValueError):
            self.test_player_two.make_bet(1)

    def test_add_card_basic(self):
        self.assertEqual(len(self.test_player_one.hand), 0)
        self.test_player_one.add_card(self.test_card_one)
        self.assertEqual(len(self.test_player_one.hand), 1)
        self.assertEqual(self.test_player_one.hand[0].describe(), "The 3 of spades.")

    def test_add_card_complex(self):
        self.assertEqual(len(self.test_player_one.hand), 0)
        self.test_player_one.add_card(self.test_card_one)
        self.test_player_one.add_card(self.test_card_two)
        self.assertEqual(self.test_player_one.hand[0].describe(), "The 3 of spades.")
        self.assertEqual(self.test_player_one.hand[1].describe(), "The ace of diamonds.")
        self.test_player_one.add_card(self.test_card_three)
        self.assertEqual(self.test_player_one.hand[2].describe(), "The 4 of hearts.")

    def test_clear_hand(self):
        self.test_add_card_complex()
        self.assertEqual(len(self.test_player_one.hand), 3)
        self.test_player_one.clear_hand()
        self.assertEqual(len(self.test_player_one.hand), 0)



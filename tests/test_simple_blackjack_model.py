from unittest import TestCase
from src.model.simple_blackjack_model import SimpleBlackjackModel
from src.model.card import Card


class TestSimpleBlackjackModel(TestCase):
    def setUp(self):
        num_deck = 6;
        player_starting_amt = 1000;
        self.SimpleBlackjackModel = SimpleBlackjackModel(num_deck, player_starting_amt)

    def test_invalid_deck(self):
        with self.assertRaises(ValueError):
            SimpleBlackjackModel(-1, 1000)

    def test_invalid_player_starting_amt(self):
        with self.assertRaises(ValueError):
            SimpleBlackjackModel(6, -20)

    def test_deal(self):
        self.assertEqual(len(self.SimpleBlackjackModel.player.hand), 0)
        self.assertEqual(len(self.SimpleBlackjackModel.dealer.hand), 0)
        self.SimpleBlackjackModel.deal()
        self.assertEqual(len(self.SimpleBlackjackModel.player.hand), 2)
        self.assertEqual(len(self.SimpleBlackjackModel.dealer.hand), 2)

    def test_card_value(self):
        self.test_card_one = Card(7, "spades")
        self.test_card_two = Card("king", "hearts")
        self.test_card_three = Card("ace", "diamonds")
        self.assertEqual(self.SimpleBlackjackModel.card_value(self.test_card_one), 7)
        self.assertEqual(self.SimpleBlackjackModel.card_value(self.test_card_two), 10)
        self.assertEqual(self.SimpleBlackjackModel.card_value(self.test_card_three), [1, 11])

    def test_hand_value(self):
        self.test_card_value()
        self.test_hand_one = []
        self.test_hand_two = [self.test_card_two, self.test_card_three]
        self.test_hand_three = [self.test_card_one, self.test_card_two, self.test_card_three]
        self.assertEqual(self.SimpleBlackjackModel.hand_value(self.test_hand_one), 0)
        self.assertEqual(self.SimpleBlackjackModel.hand_value(self.test_hand_two), 21)
        self.assertEqual(self.SimpleBlackjackModel.hand_value(self.test_hand_three), 18)

    def test_hit(self):
        self.assertEqual(len(self.SimpleBlackjackModel.player.hand), 0)
        self.SimpleBlackjackModel.hit()
        self.assertEqual(len(self.SimpleBlackjackModel.player.hand), 1)
        self.SimpleBlackjackModel.stay()
        self.SimpleBlackjackModel.hit()
        self.assertEqual(len(self.SimpleBlackjackModel.dealer.hand), 1)

    def test_stay(self):
        self.assertEqual(self.SimpleBlackjackModel.is_player_turn, True)
        self.SimpleBlackjackModel.stay()
        self.assertEqual(self.SimpleBlackjackModel.is_player_turn, False)

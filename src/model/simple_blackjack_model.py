from src.model.dealer import Dealer
from src.model.player import Player
from src.model.deck import Deck
from src.utils.utils import Utils
from src.model.card import Card


class SimpleBlackjackModel(object):

    def __init__(self, num_deck):
        """
        Represents a simple model for a blackjack game between a single player and a dealer.
        :param num_deck: the number of decks used for the game
        """
        player_starting_amt = int(input("How much do you want to start with:\n"))
        Utils.require_non_negative(num_deck)
        Utils.require_non_negative(player_starting_amt)
        self.dealer = Dealer()
        self.player = Player(player_starting_amt)
        self.deck = Deck(num_deck)
        self.is_player_turn = True  # True if the players turn. False if the dealers turn

    def play(self):
        """
        Plays a simple blackjack game.
        :return: void method
        """
        # Pregame
        print(f"The player has ${self.player.balance} available")
        player_bet = int(input("Please make a bet:\n"))
        print("----------------------------------")

        # Bet made -> deal cards
        self.player.make_bet(player_bet)
        self.deal()
        print(self.get_game_state())

        # Gameplay
        while not self.is_hand_over():
            action = input(f"Do you want to 'HIT' or 'STAY'\n")
            print("----------------------------------")
            if action == "HIT":
                self.hit()
                print(self.get_game_state())
            elif action == "STAY":
                self.stay()
                print(self.get_game_state())
            else:
                print("Please enter either 'HIT' or 'STAY'\n")

        # Do you want to play again? If not, return the result of the blackjack session
        play_again = input("Do you want to play again? (YES / NO):\n")
        print("----------------------------------")
        if play_again == "YES":
            self.clear()
            self.play()
        else:
            print(f"The player currently has: ${self.player.balance}\n")
            print(f"Thank you for playing!")
            print(f"The number of cards left in the deck: {len(self.deck.cards)}")

    # ----------------SET UP METHODS-------------------
    def deal(self):
        """
        Deals out two cards to all players and the dealer at a table. Starts with the player to the left of the dealer.
        :return: None
        """
        deal_player = True
        i = 0
        while i < 4:
            if deal_player:
                self.player.add_card(self.deck.draw())
                deal_player = False
            else:
                self.dealer.add_card(self.deck.draw())
                deal_player = True
            i += 1

    def is_hand_over(self):
        """
        When playing, a hand is over when:
        - it is the players turn and they have busted (hand value > 21)
        - it is the players turn and they have blackjack (hand value = 21)
            -> if the dealer has 21, PUSH, otherwise, the player gets 1.5X their betting amount
        - it is the dealers turn and they have busted
        - it is the dealers turn and they have > 16, but < 21
        :return: boolean. True if hand is over, False if not.
        """
        player_hand_val = self.hand_value(self.player.hand)
        dealer_hand_val = self.hand_value(self.dealer.hand)

        # It is the players turn, so the dealer has <= 21
        if self.is_player_turn:
            if player_hand_val > 21:
                print("LOSE")
                return True
            elif player_hand_val == 21: # blackjack case
                if dealer_hand_val == 21:
                    print("PUSH")
                    self.player.balance += self.player.bet
                else:
                    print("WIN")
                    self.player.balance += 2.5 * self.player.bet
                return True
        # It is the dealers turn, so the player has <= 21
        else:
            if dealer_hand_val > 21:
                print("WIN")
                self.player.balance += 2 * self.player.bet
                return True
            elif dealer_hand_val > player_hand_val:
                print("LOSE")
                return True
            elif player_hand_val == dealer_hand_val:
                print("PUSH")
                self.player.balance += self.player.bet
                return True
            elif dealer_hand_val >= 17:
                if player_hand_val > dealer_hand_val:
                    print("WIN")
                    self.player.balance += 2 * self.player.bet
                    return True
        return False

    def get_game_state(self) -> str:
        """
        Represents the true current state of the blackjack game as a string.
        :return: a string representing the true current state
        """
        result = ""
        turn = "PLAYER" if self.is_player_turn else "DEALER"
        dealer_hand = [self.card_value(card) for card in self.dealer.hand]
        player_hand = [self.card_value(card) for card in self.player.hand]
        if self.is_player_turn:
            turn = "PLAYER" if self.is_player_turn else "DEALER"
            dealer_hand_hidden = ["?", dealer_hand[1]]
            result += f"Dealer's Hand: {dealer_hand_hidden} -> ?\n\n"
        else:
            result += f"Dealer's Hand: {dealer_hand} -> {self.hand_value(self.dealer.hand)}\n\n"
        result += f"Player's Balance: {self.player.balance}\n"
        result += f"Player's Bet: {self.player.bet}\n"
        result += f"Player's Hand: {player_hand} -> {self.hand_value(self.player.hand)}\n\n"
        result += f"It is the {turn}'s turn"
        return result

    @staticmethod
    def card_value(card: Card) -> int:
        """
        Returns the value of a card in a blackjack game. Aces are either 1 or 11.
        :return: an integer representing the value of a card
        """
        if isinstance(card.rank, int):
            return card.rank
        elif card.rank == "ace":
            return 11
        else:
            return 10

    def hand_value(self, hand: list) -> int:
        """
        Converts a list representing a hand into its game value.
        :param hand: the player or dealer hand
        :return: int
        """
        val = 0
        num_aces = 0
        for card in hand:
            if card.rank == 'ace':
                num_aces += 1
                val += self.card_value(card)
            else:
                val += self.card_value(card)
        while num_aces > 0:
            if val > 21:
                val -= 10
            num_aces -= 1
        return val

    # ----------------GAME PLAY METHODS-------------------
     def hit(self) -> str:
        """
        Deals a card to the current player or dealer depending on whose turn it is.
        :return: n/a. void method
        """
        if self.is_player_turn:
            self.player.add_card(self.deck.draw())
        else:
            self.dealer.add_card(self.deck.draw())

    def stay(self):
        """
        A stay action from the player or the dealer. If the player stays, it is then
        the dealers turn. If the dealer stays, evaluate the hand to see who wins
        :return: n/a. void method
        """
        if self.is_player_turn:
            self.is_player_turn = False
        else:
            self.is_hand_over()

    def clear(self):
        """
        Clears the hands of the player(s) and dealer.
        :return: None
        """
        self.is_player_turn = True
        self.player.clear_hand()
        self.dealer.clear_hand()


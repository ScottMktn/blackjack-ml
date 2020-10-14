from src.utils.error_messages import ErrorMessages
from src.utils.utils import Utils
from src.model.dealer import Dealer


class Player(Dealer):
    def __init__(self, balance):
        """
        Represents a single player at a blackjack table.
        :param balance:
        """
        super().__init__()
        Utils.require_non_negative(balance)
        self.balance = balance
        self.bet = 0

    def make_bet(self, bet_amount):
        if bet_amount <= self.balance:
            self.balance -= bet_amount
            self.bet = bet_amount
        else:
            raise ValueError(ErrorMessages.InsufficientFundsError.error_message())



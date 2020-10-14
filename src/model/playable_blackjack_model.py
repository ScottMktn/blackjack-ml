from src.model.simple_blackjack_model import SimpleBlackjackModel
from src.utils.utils import Utils


class PlayableBlackjackModel(SimpleBlackjackModel):
    def __init__(self):
        player_starting_amount = int(input("How much do you want to start with:\n"))
        Utils.require_non_negative(player_starting_amount)
        super().__init__(6, player_starting_amount)

    def is_hand_over(self):
        """
        @OVERRIDES is_hand_over() method in SimpleBlackjackModel

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
        return True
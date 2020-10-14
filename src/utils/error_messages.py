from enum import Enum


class ErrorMessages(Enum):
    InsufficientFundsError = "You do not have enough funds."
    RequireNonZero = "Value/Param can not be less than zero"

    def error_message(self):
        return self.value

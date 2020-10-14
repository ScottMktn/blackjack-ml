from src.utils.error_messages import ErrorMessages


class Utils(object):
    @staticmethod
    def require_non_negative(elements):
        if elements < 0:
            raise ValueError(ErrorMessages.RequireNonZero.error_message())



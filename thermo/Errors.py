class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InvalidInputError(Error):
    """Exception raised for invalid input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message

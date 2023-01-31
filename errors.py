class Error:
    """Helper class for error types and codes."""
    wrong_filename = 101
    empty_data = 102

class LetterboxdException(Exception):
    """Exception class to throw custom exceptions."""
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code

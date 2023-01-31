class Error:
    wrong_filename = 101
    empty_data = 102

class LetterboxdException(Exception):
    def __init__(self, msg, code):
        super().__init__(msg)
        self.code = code
class ApplicationError(Exception):
    pass


class ParsingError(ApplicationError):
    def __init__(self, message):
        self.message = message
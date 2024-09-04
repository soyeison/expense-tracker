class WriteCsvFileException(Exception):
    def __init__(self, message = "Error while write csv file"):
        self.message = message
        super().__init__(self.message)
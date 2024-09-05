class DontExistExpense(Exception):
    def __init__(self, message = "Don't exist id ingressed"):
        self.message = message
        super().__init__(message)
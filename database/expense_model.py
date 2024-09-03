from datetime import datetime

class ExpenseModel:
    listExpense = []

    def __init__(self, id, description, amount, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.amount = amount
        self.createdAt = createdAt
        self.updatedAt = updatedAt

    def add(self):
        # Convertir de ExpenseModel a dict y guardarlo en listExpense
        dictToSave = {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "createdAt": self.createdAt,
            "updatedAt": self.createdAt,
        }
        ExpenseModel.listExpense.append(dictToSave)
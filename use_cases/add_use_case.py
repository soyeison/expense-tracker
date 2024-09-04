from domain.expense import Expense
from adapters.csv_expense_repository import CsvExpenseRepository

class AddUseCase:
    def __init__(self, expense_repository: CsvExpenseRepository) -> None:
        self.expenses = expense_repository

    def execute(self, expense: Expense):
        try:
            if expense.id is not None:
                self.expenses.add(expense)
                self.expenses.save()
            else:
                raise ValueError("Expense id cannot be None")

            return expense
        except Exception as e:
            raise e

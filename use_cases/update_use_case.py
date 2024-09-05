from datetime import datetime
from adapters.csv_expense_repository import CsvExpenseRepository

class UpdateUseCase:
    def __init__(self, expense_repository: CsvExpenseRepository) -> None:
        self.expenses = expense_repository

    def execute(self, id, element_type, element_value):
        try:
            self.expenses.update(id, "updatedAt", datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            return self.expenses.update(id, element_type, element_value)
        except Exception as e:
            raise e
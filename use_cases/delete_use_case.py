from adapters.csv_expense_repository import CsvExpenseRepository

class DeleteUseCase:
    def __init__(self, expense_repository: CsvExpenseRepository) -> None:
        self.expenses = expense_repository

    def execute(self, id):
        try:
            return self.expenses.delete(id)
        except Exception as e:
            raise e

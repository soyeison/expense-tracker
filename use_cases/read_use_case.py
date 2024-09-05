from domain.expense import Expense
from utils.format_list_response import formatListResponse
from adapters.csv_expense_repository import CsvExpenseRepository

class ReadUseCase:
    def __init__(self, expense_repository: CsvExpenseRepository) -> None:
        self.expenses = expense_repository

    def execute(self):
        try:
            expenses = self.expenses.read_expenses()
            return formatListResponse(expenses)

        except Exception as e:
            raise e

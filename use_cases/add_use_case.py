from utils.conver_to_database import convertToDatabaseExpenseModel
from domain.expense import Expense
from database.expense_model import ExpenseModel

class AddUseCase:
    @staticmethod
    def execute(expense: Expense):
        try:
            expenseSaved = ExpenseModel.add(expense.id, expense.description, expense.amount, expense.createdAt, expense.createdAt)
            return expenseSaved
        except Exception as e:
            raise e

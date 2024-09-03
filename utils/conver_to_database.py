from domain.expense import Expense
from database.expense_model import ExpenseModel

def convertToDatabaseExpenseModel(expense: Expense):
    expenseModel = ExpenseModel(
        expense.id,
        expense.description, 
        expense.amount, 
        expense.createdAt,
        expense.createdAt # Revisar esto cuando se implemente update
    )
    return expenseModel
from datetime import datetime
from adapters.csv_expense_repository import CsvExpenseRepository

class SummaryUseCase:
    def __init__(self, expense_repository: CsvExpenseRepository) -> None:
        self.expenses = expense_repository

    def execute(self, month = None):
        try:
            expenses = self.expenses.read_expenses()

            summary = self.get_total(month, expenses)

            month_name = self.get_month_name(month)
            
            return (summary, month_name)
        except Exception as e:
            raise e
        
    def get_month_name(self, month):
        if month is None:
            return None
        
        date_of_month = datetime(2024, month, 1)

        month_name = date_of_month.strftime("%B")

        return month_name
        
    def get_total(self, month, expenses):
        summary = 0
        if month is None:
            for expense in expenses:
                summary = summary + float(expenses[expense].amount)
        else:
            for expense in expenses:
                if datetime.strptime(expenses[expense].createdAt, '%d-%m-%Y %H:%M:%S').month == month:
                    summary = summary + float(expenses[expense].amount)
        
        return summary

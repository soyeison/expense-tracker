import csv
import config
from domain.expense import Expense
from errors.write_csv_file_exception import WriteCsvFileException

class CsvExpenseRepository:
    def __init__(self):
        self.expenses = {}

    def add(self, expense: Expense):
        self.expenses[expense.id] = expense
        return self.expenses
    
    def save(self):
        try:
            with open(config.DATABASE_FILE_PATH, 'a', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for expense_id in self.expenses:
                    actual_expense = self.expenses[expense_id]
                    writer.writerow([
                        actual_expense.id, 
                        actual_expense.description, 
                        actual_expense.amount, 
                        actual_expense.createdAt, 
                        actual_expense.updatedAt
                    ])
        except IOError as e:
            raise WriteCsvFileException(f"Error writting in CSV: {e}")
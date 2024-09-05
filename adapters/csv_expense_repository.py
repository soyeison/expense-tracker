import csv
import config
from domain.expense import Expense
from errors.write_csv_file_exception import WriteCsvFileException

class CsvExpenseRepository:
    def __init__(self):
        self.expenses = {}
        self.readCsv()

    def add(self, expense: Expense):
        self.expenses[expense.id] = expense
        return self.expenses
    
    def read_expenses(self):
        return self.expenses
    
    def readCsv(self):
        try:
            with open(config.DATABASE_FILE_PATH, 'r', newline='\n') as file:
                reader = csv.reader(file, delimiter=';')
                listReader = list(reader)
                for expense in listReader:
                    self.expenses[expense[0]] = Expense(
                        id=expense[0],
                        description=expense[1],
                        amount=expense[2],
                        createdAt=expense[3],
                        updatedAt=expense[4]
                    )
        except Exception as e:
            raise e
    
    def saveCsv(self):
        try:
            with open(config.DATABASE_FILE_PATH, 'a', newline='\n') as file:
                writer = csv.writer(file, delimiter=';')
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
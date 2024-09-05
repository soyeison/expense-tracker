import csv
import config
from domain.expense import Expense
from errors.write_csv_file_exception import WriteCsvFileException
from errors.dont_exist_expense import DontExistExpense

class CsvExpenseRepository:
    def __init__(self):
        self.expenses = {}
        self.readCsv()

    def add(self, expense: Expense):
        self.expenses[expense.id] = expense
        return self.expenses
    
    def read_expenses(self):
        return self.expenses
    
    def update(self, id, element_key, element_value):
        try:
            element_to_update = self.expenses[id]
            setattr(element_to_update, element_key, element_value)
            self.saveCsv()

            return element_to_update
        
        except KeyError as e:
            raise DontExistExpense(f"Don't exist task with id: {id}")
        except Exception as e:
            raise e
    
    def delete(self, id):
        try:
            expenseDeleted = self.expenses.pop(id)
            self.saveCsv()
            
            return expenseDeleted
        except KeyError as e:
            raise DontExistExpense(f"Don't exist task with id: {id}")
    
    def readCsv(self):
        try:
            with open(config.DATABASE_FILE_PATH, 'r', newline='\n') as file:
                reader = csv.reader(file, delimiter=';')
                listReader = list(reader)
                if len(listReader[0]) == 0:
                    self.expenses = {}
                else:
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
            with open(config.DATABASE_FILE_PATH, 'w', newline='\n') as file:
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
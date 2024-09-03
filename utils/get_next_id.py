import config
import csv
from database.expense_model import ExpenseModel

def getNextId():
    try:
        with open(config.DATABASE_FILE_PATH, 'r', newline='\n') as file:
            reader = csv.reader(file, delimiter=';')
            listReader = list(reader)
            if len(listReader) == 0:
                return "1"
            lastItemOfList = listReader[len(listReader) - 1]
            nextId = int(lastItemOfList[0]) + 1
            return str(nextId)
    except Exception as e:
        print(f"Something happend handling next id: {e}")
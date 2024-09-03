import config
import csv
from error.write_csv_file_exception import WriteCsvFileException

class ExpenseModel:
    listExpense = []

    try:
        with open(config.DATABASE_FILE_PATH, 'r', newline='\n') as fichero:
                reader = csv.reader(fichero, delimiter=';')
                for id, description, amount, createdAt, updatedAt in reader:
                    listExpense.append({
                        "id": id,
                        "description": description,
                        "amount": amount,
                        "createdAt": createdAt,
                        "updatedAt": updatedAt,
                    })
    except ValueError as e:
        print(f"Problems trying read elements from database: {e}")

    @staticmethod
    def add(id, description, amount, createdAt, updatedAt):
        dictToSave = {
            "id": id,
            "description": description,
            "amount": amount,
            "createdAt": createdAt,
            "updatedAt": updatedAt,
        }
        ExpenseModel.listExpense.append(dictToSave)

        # Guardar esto en un archivo JSON
        try:
            ExpenseModel.saveCsv()
            return dictToSave
        
        except Exception as e:
            print("Something wrong trying save")
            raise e
    
    @staticmethod
    def saveCsv():
        try:
            with open(config.DATABASE_FILE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for expense in ExpenseModel.listExpense:
                    writer.writerow([expense["id"], expense["description"], expense["amount"], expense["createdAt"], expense["updatedAt"]])
        except IOError as e:
            raise WriteCsvFileException(f"Error writting in CSV: {e}")

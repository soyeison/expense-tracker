import argparse
from datetime import datetime
from domain.expense import Expense
from use_cases.add_use_case import AddUseCase
from use_cases.read_use_case import ReadUseCase
from use_cases.delete_use_case import DeleteUseCase
from utils.get_next_id import getNextId

from adapters.csv_expense_repository import CsvExpenseRepository

def command_add(description, amount):
    try:
        expense_repository = CsvExpenseRepository()
        add_use_case = AddUseCase(expense_repository)

        new_expense = Expense(
            id=getNextId(), 
            description=description, 
            amount=amount, 
            createdAt=datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            updatedAt=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        )

        expense = add_use_case.execute(new_expense)
        return f"Expense added successfully (ID: {expense.id})"
    except Exception as e:
        raise e
        
def command_list():
    try:
        expense_repository = CsvExpenseRepository()
        read_use_case = ReadUseCase(expense_repository)
        return read_use_case.execute()
    except Exception as e:
        raise e
    
def command_summary():
    try:
        print("Summary")
    except Exception as e:
        raise e
    
def command_delete(id: str):
    try:
        expense_repository = CsvExpenseRepository()
        delete_use_case = DeleteUseCase(expense_repository)
        delete_use_case.execute(id)
        return "Expense deleted successfully"
    except Exception as e:
        raise e

def main():
    parser = argparse.ArgumentParser(description="Manage your finances CLI")
    subparse = parser.add_subparsers(dest="command", help="Sub-commands")

    # Agregar los argumentos de add
    parser_add = subparse.add_parser('add', help="Add expense")
    parser_add.add_argument("--description", type=str, required=True, help="Description of expense")
    parser_add.add_argument("--amount", type=float, required=True, help="Amount of that expense")

    # Agregar los argumentos de list
    parser_list = subparse.add_parser('list', help="List all expenses")

    # Agregar los argumentos de summary
    parser_summary = subparse.add_parser("summary", help="Summary all expenses")
    parser_summary.add_argument("--month", type=int, required=False, help="Filter summary by months")

    # Agregar los argumentos de update
    parser_update = subparse.add_parser("update", help="Update a row")
    parser_update.add_argument("--id", type=int, required=True, help="Id of finance")
    parser_update.add_argument("--description", type=str, required=True, help="Description of expense to update")

    # Agregar los argumentos de delete
    parser_delete = subparse.add_parser('delete', help="Delete expense")
    parser_delete.add_argument("--id", type=str, required=True, help="Id of finance")

    args = parser.parse_args()

    try:
        if args.command == "add":
            print(command_add(args.description, args.amount))

        elif args.command == "list":
            print(command_list())

        elif args.command == "summary":
            print(command_summary())

        elif args.command == "update":
            print("Se ejecuto update")

        elif args.command == "delete":
            print(command_delete(args.id))
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
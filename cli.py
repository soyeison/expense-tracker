import argparse
from datetime import datetime
from domain.expense import Expense
from use_cases.add_use_case import AddUseCase
from utils.get_next_id import getNextId

def command_add(description, amount):
        try:
            idToSave = getNextId()
            descriptionToSave = description
            amountToSave = amount
            createdAtToSave = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

            newExpense = Expense(idToSave, descriptionToSave, amountToSave, createdAtToSave)
            rowSaved = AddUseCase.execute(newExpense)

            return rowSaved
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
    parser_delete.add_argument("--id", type=int, required=True, help="Id of finance")

    args = parser.parse_args()

    try:
        if args.command == "add":
            print(command_add(args.description, args.amount))

        elif args.command == "list":
            print("Se ejecuto list")

        elif args.command == "summary":
            print("Se ejecuto summary")

        elif args.command == "update":
            print("Se ejecuto update")

        elif args.command == "delete":
            print("Se ejecuto delete")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
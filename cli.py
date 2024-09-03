import argparse
from datetime import datetime
from domain.expense import Expense

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

    print("Args:",args)

    try:
        if args.command == "add":
            id = '1'
            description = "Hola mundo"
            amount = 53
            createdAt = datetime.now()
            newExpense = Expense(id, description, amount, createdAt)
            # Caso de uso de agregar
            # Dentro del caso de uso convertir al formato que necesita la DB
            # Guardar

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
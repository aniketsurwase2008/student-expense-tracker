from .analytics import total
from .service import ExpenseService
from .storage import ExpenseStorage
from .validators import CATEGORIES

def print_expenses(expenses):
    if not expenses:
        print("\nNo expenses recorded.")
        return
    print("\nID  DATE        CATEGORY     AMOUNT      NOTE")
    print("-" * 58)
    for e in expenses:
        print(f"{e.expense_id:<3} {e.date:<11} {e.category:<12} ₹{e.amount:>8.2f}  {e.note}")

def add_expense(service):
    print("\nAdd Expense")
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input(f"Category {CATEGORIES}: ").strip()
    amount = input("Amount (₹): ").strip()
    note = input("Note (optional): ").strip()
    try:
        e = service.add(date, category, amount, note)
        print(f"Added expense #{e.expense_id}.")
    except ValueError as exc:
        print(f"Input error: {exc}")

def delete_expense(service):
    try:
        expense_id = int(input("Expense ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return
    print("Deleted." if service.delete(expense_id) else "Expense ID not found.")

def show_summary(service):
    data = service.summary()
    print(f"\nTotal spending: ₹{data['total']:.2f}")
    print("\nBy category:")
    for category, amount in data["by_category"].items():
        print(f"  {category:<12} ₹{amount:.2f}")
    print("\nMonthly:")
    for month, amount in data["monthly"].items():
        print(f"  {month}: ₹{amount:.2f}")
    if data["top_categories"]:
        print("\nTop categories:")
        for category, amount in data["top_categories"]:
            print(f"  {category:<12} ₹{amount:.2f}")

def run():
    service = ExpenseService(ExpenseStorage())
    while True:
        print("\n=== Student Expense Tracker ===")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Delete expense")
        print("4. View analytics")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(service)
        elif choice == "2":
            print_expenses(service.list_all())
        elif choice == "3":
            delete_expense(service)
        elif choice == "4":
            show_summary(service)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.")

if __name__ == "__main__":
    run()

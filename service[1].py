from typing import List, Optional
from .analytics import by_category, monthly_totals, top_categories, total
from .models import Expense
from .storage import ExpenseStorage
from .validators import validate_amount, validate_category, validate_date

class ExpenseService:
    def __init__(self, storage: ExpenseStorage):
        self.storage = storage
        self.expenses = storage.load()

    def _next_id(self) -> int:
        return max((e.expense_id for e in self.expenses), default=0) + 1

    def add(self, date: str, category: str, amount: str, note: str = "") -> Expense:
        expense = Expense(
            self._next_id(),
            validate_date(date),
            validate_category(category),
            validate_amount(amount),
            note.strip(),
        )
        self.expenses.append(expense)
        self.storage.save(self.expenses)
        return expense

    def list_all(self) -> List[Expense]:
        return sorted(self.expenses, key=lambda e: (e.date, e.expense_id), reverse=True)

    def get(self, expense_id: int) -> Optional[Expense]:
        return next((e for e in self.expenses if e.expense_id == expense_id), None)

    def delete(self, expense_id: int) -> bool:
        expense = self.get(expense_id)
        if expense is None:
            return False
        self.expenses.remove(expense)
        self.storage.save(self.expenses)
        return True

    def summary(self):
        return {
            "total": total(self.expenses),
            "by_category": by_category(self.expenses),
            "monthly": monthly_totals(self.expenses),
            "top_categories": top_categories(self.expenses),
        }

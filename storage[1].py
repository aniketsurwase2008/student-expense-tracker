import json
from pathlib import Path
from typing import List
from .models import Expense

class ExpenseStorage:
    def __init__(self, path: str = "data/expenses.json"):
        self.path = Path(path)

    def load(self) -> List[Expense]:
        if not self.path.exists():
            return []
        try:
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            return [Expense.from_dict(item) for item in raw]
        except (json.JSONDecodeError, OSError, KeyError, TypeError, ValueError) as exc:
            raise RuntimeError(f"Could not read expense data: {exc}") from exc

    def save(self, expenses: List[Expense]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [expense.to_dict() for expense in expenses]
        temp = self.path.with_suffix(".tmp")
        temp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        temp.replace(self.path)

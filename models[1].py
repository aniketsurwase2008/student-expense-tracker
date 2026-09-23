from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class Expense:
    expense_id: int
    date: str
    category: str
    amount: float
    note: str = ""

    def to_dict(self) -> Dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> "Expense":
        return cls(
            expense_id=int(data["expense_id"]),
            date=str(data["date"]),
            category=str(data["category"]),
            amount=float(data["amount"]),
            note=str(data.get("note", "")),
        )

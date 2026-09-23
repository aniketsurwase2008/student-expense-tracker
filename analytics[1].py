from collections import defaultdict
from typing import Dict, List, Tuple
from .models import Expense

def total(expenses: List[Expense]) -> float:
    return round(sum(e.amount for e in expenses), 2)

def by_category(expenses: List[Expense]) -> Dict[str, float]:
    result = defaultdict(float)
    for expense in expenses:
        result[expense.category] += expense.amount
    return {k: round(v, 2) for k, v in sorted(result.items())}

def monthly_totals(expenses: List[Expense]) -> Dict[str, float]:
    result = defaultdict(float)
    for expense in expenses:
        result[expense.date[:7]] += expense.amount
    return {k: round(v, 2) for k, v in sorted(result.items())}

def top_categories(expenses: List[Expense], limit: int = 3) -> List[Tuple[str, float]]:
    return sorted(by_category(expenses).items(), key=lambda item: item[1], reverse=True)[:limit]

from datetime import datetime

CATEGORIES = ("Food", "Travel", "Education", "Shopping", "Bills", "Health", "Other")

def validate_date(value: str) -> str:
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError as exc:
        raise ValueError("Date must use YYYY-MM-DD format.") from exc
    return value

def validate_category(value: str) -> str:
    normalized = value.strip().title()
    if normalized not in CATEGORIES:
        raise ValueError("Category must be one of: " + ", ".join(CATEGORIES))
    return normalized

def validate_amount(value: str) -> float:
    try:
        amount = float(value)
    except ValueError as exc:
        raise ValueError("Amount must be a number.") from exc
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")
    return round(amount, 2)

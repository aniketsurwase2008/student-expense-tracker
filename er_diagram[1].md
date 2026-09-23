# Storage / ER Diagram

```text
+-----------------------------+
|          EXPENSE            |
+-----------------------------+
| PK expense_id : INTEGER     |
| date        : TEXT          |
| category    : TEXT          |
| amount      : REAL          |
| note        : TEXT          |
+-----------------------------+

Storage format: JSON array of Expense records.

Example:
[
  {
    "expense_id": 1,
    "date": "2026-09-18",
    "category": "Food",
    "amount": 150.0,
    "note": "Lunch"
  }
]
```

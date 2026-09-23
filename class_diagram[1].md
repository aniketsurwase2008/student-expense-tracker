# Class / Component Diagram

```text
+-------------------+
|      Expense      |
+-------------------+
| expense_id        |
| date              |
| category          |
| amount            |
| note              |
+-------------------+
| to_dict()         |
| from_dict()       |
+---------^---------+
          |
          | used by
          |
+---------+---------+       +--------------------+
|   ExpenseService  |------>|  ExpenseStorage    |
+-------------------+       +--------------------+
| expenses          |       | path               |
| add()             |       | load()             |
| list_all()        |       | save()             |
| get()             |       +--------------------+
| delete()          |
| summary()         |
+---------+---------+
          |
          v
+-------------------+
|      cli.py       |
+-------------------+
| run()             |
| add_expense()     |
| delete_expense()  |
| show_summary()    |
+-------------------+

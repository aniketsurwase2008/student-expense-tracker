# System Architecture

```text
+------------------+
|   User / CLI      |
+---------+--------+
          |
          v
+------------------+
|     cli.py       |
| Input / Output   |
+---------+--------+
          |
          v
+------------------+
|   service.py     |
| Business Logic   |
+----+--------+----+
     |        |
     v        v
+---------+ +-------------+
|models.py| | validators.py|
+---------+ +-------------+
     |
     v
+------------------+
|   storage.py     |
| JSON Persistence |
+---------+--------+
          |
          v
+------------------+
| expenses.json    |
+------------------+

Analytics module reads validated Expense objects through the service layer.
```

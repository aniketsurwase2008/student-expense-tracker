# Student Expense Tracker — Python Essentials

A modular command-line application for recording student expenses, storing them locally in JSON, and generating useful spending summaries.

## Why this project?
The project applies Python Essentials concepts in a practical problem: data structures, functions, classes, modules, file handling, JSON, exception handling, validation, sorting, aggregation, and testing.

## Features
- Add an expense
- List saved expenses
- Delete an expense
- Validate date/category/amount
- Persist data in `data/expenses.json`
- Calculate total spending
- Calculate category-wise spending
- Calculate month-wise spending
- Show top spending categories
- Run automated unit tests

## Project Structure
```text
student-expense-tracker/
├── expense_tracker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── analytics.py
│   ├── cli.py
│   ├── models.py
│   ├── service.py
│   ├── storage.py
│   └── validators.py
├── tests/
│   └── test_expense_tracker.py
├── data/
│   └── expenses.json
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── use_case.md
│   ├── class_diagram.md
│   ├── sequence.md
│   └── er_diagram.md
├── statement.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements
- Python 3.9 or newer
- No external Python packages are required.

## Setup
### Windows
```powershell
git clone <YOUR_PUBLIC_REPOSITORY_URL>
cd student-expense-tracker
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux
```bash
git clone <YOUR_PUBLIC_REPOSITORY_URL>
cd student-expense-tracker
python3 -m venv .venv
source .venv/bin/activate
```

## Dependency Installation
This project uses only the Python standard library, so there are no third-party dependencies. You can still run:
```bash
pip install -r requirements.txt
```

## Run
From the repository root:
```bash
python -m expense_tracker
```

## Example Input
```text
Choose an option: 1
Date (YYYY-MM-DD): 2026-09-18
Category ('Food', 'Travel', 'Education', 'Shopping', 'Bills', 'Health', 'Other'): Food
Amount (₹): 150
Note (optional): Lunch
```

## Test
Run:
```bash
python -m unittest discover -s tests -v
```

## Data Storage
Expenses are stored in `data/expenses.json`. The file is created/updated automatically. The application uses a temporary file before replacing the main JSON file to reduce the chance of a partially written data file.

## Design Documentation
See the `docs/` directory for architecture, workflow, use-case, class, sequence, and ER/storage diagrams.

## GitHub Submission Checklist
1. Create a public GitHub repository.
2. Keep `README.md` and `statement.md` at the repository root.
3. Push the complete project.
4. Verify the repository opens without login.
5. Submit only the repository root URL, for example:
   `https://github.com/YOUR_USERNAME/student-expense-tracker`
6. Do not submit `/tree/main/` or `/blob/main/` URLs.

## Academic Note
This is a reference implementation created for the Python Essentials project requirements. Before submission, review, test, and personalize the project so that the final repository reflects your own understanding and work.

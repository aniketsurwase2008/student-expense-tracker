import tempfile
import unittest
from pathlib import Path
from expense_tracker.analytics import by_category, monthly_totals, total
from expense_tracker.service import ExpenseService
from expense_tracker.storage import ExpenseStorage

class ExpenseTrackerTests(unittest.TestCase):
    def make_service(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        self.tmp.close()
        Path(self.tmp.name).write_text("[]", encoding="utf-8")
        return ExpenseService(ExpenseStorage(self.tmp.name))

    def test_add_and_total(self):
        service = self.make_service()
        service.add("2026-09-01", "Food", "120.50", "Lunch")
        service.add("2026-09-02", "Travel", "80", "Bus")
        self.assertEqual(total(service.list_all()), 200.50)

    def test_category_and_monthly_summary(self):
        service = self.make_service()
        service.add("2026-09-01", "Food", "100", "")
        service.add("2026-09-12", "Food", "50", "")
        service.add("2026-10-01", "Education", "200", "")
        self.assertEqual(by_category(service.list_all())["Food"], 150.0)
        self.assertEqual(monthly_totals(service.list_all())["2026-10"], 200.0)

    def test_invalid_amount(self):
        service = self.make_service()
        with self.assertRaises(ValueError):
            service.add("2026-09-01", "Food", "-5", "")

    def test_delete(self):
        service = self.make_service()
        item = service.add("2026-09-01", "Bills", "300", "")
        self.assertTrue(service.delete(item.expense_id))
        self.assertFalse(service.delete(item.expense_id))

if __name__ == "__main__":
    unittest.main()

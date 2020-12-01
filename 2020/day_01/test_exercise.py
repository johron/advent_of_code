import unittest
import exercise

class TestExpenseReport(unittest.TestCase):
    def test_exercise_01_1(self):
        number = exercise.get_expense_report_nr([1721,979,366,299,675,1456], 2, 2020)
        self.assertEqual(number, 514579)

    def test_exercise_01_2(self):
        number = exercise.get_expense_report_nr([1721,979,366,299,675,1456], 3, 2020)
        self.assertEqual(number, 241861950)

if __name__ == '__main__':
    unittest.main()
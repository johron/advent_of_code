import unittest
import exercise

class TestExpenseReport(unittest.TestCase):
    def test_exercise_01(self):
        number = exercise.get_expense_report_number_2([1721,979,366,299,675,1456], 2020)
        self.assertEqual(number, 514579)

    def test_exercise_02(self):
        number = exercise.get_expense_report_number_3([1721,979,366,299,675,1456], 2020)
        self.assertEqual(number, 241861950)

    def test_recursive_2(self):
        number = exercise.recursive_solve([1721,979,366,299,675,1456], 2, 0, 2020)
        self.assertEqual(number, 514579)

    def test_recursive_3(self):
        number = exercise.recursive_solve([1721,979,366,299,675,1456], 3, 0, 2020)
        self.assertEqual(number, 241861950)

    def test_fib_05(self):
        self.assertEqual(exercise.fibbonacci(5), 5)
        self.assertEqual(exercise.fibbonacci(7), 13)

if __name__ == '__main__':
    unittest.main()
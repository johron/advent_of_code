import unittest
import exercise

class TestExercise01(unittest.TestCase):
    def test_original_fuel(self):
        self.assertEqual(exercise.fuel_equation(12), 2)
        self.assertEqual(exercise.fuel_equation(14), 2)
        self.assertEqual(exercise.fuel_equation(1969), 654)
        self.assertEqual(exercise.fuel_equation(100756), 33583)

    def test_compound_fuel(self):
        self.assertEqual(exercise.compound_fuel_equation(14), 2)
        self.assertEqual(exercise.compound_fuel_equation(1969), 966)
        self.assertEqual(exercise.compound_fuel_equation(100756), 50346)
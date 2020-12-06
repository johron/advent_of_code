import unittest
import exercise

def get_input():
    return 'FBFBBFFRLR'


class TestPassportValidator(unittest.TestCase):
    def test_exercise_05a(self):
        self.assertEqual(exercise.get_seat('FBFBBFFRLR'), 357)
    def test_exercise_05b(self):
        self.assertEqual(exercise.get_seat('BFFFBBFRRR'), 567)
    def test_exercise_05c(self):
        self.assertEqual(exercise.get_seat('FFFBBBFRRR'), 119)
    def test_exercise_05d(self):
        self.assertEqual(exercise.get_seat('BBFFBBFRLL'), 820)        


    

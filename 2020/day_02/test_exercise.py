import unittest
import exercise

class TestPasswordValidator(unittest.TestCase):
    def test_exercise_02_1(self):
        self.assertTrue(exercise.normal_password(1, 3, 'a', 'abcde'))
        self.assertFalse(exercise.normal_password(1, 3, 'b', 'cdefg'))
        self.assertTrue(exercise.normal_password(2, 9, 'c', 'ccccccccc'))
    
    def test_exercise_02_2(self):
        self.assertTrue(exercise.validate_from_string('1-3 a: abcde', exercise.normal_password))
        self.assertFalse(exercise.validate_from_string('1-3 b: cdefg', exercise.normal_password))
        self.assertTrue(exercise.validate_from_string('2-9 c: ccccccccc', exercise.normal_password))

    def test_exercise_02_3(self):
        self.assertTrue(exercise.validate_from_string('1-3 a: abcde', exercise.toboggan_password))
        self.assertFalse(exercise.validate_from_string('1-3 b: cdefg', exercise.toboggan_password))
        self.assertFalse(exercise.validate_from_string('2-9 c: ccccccccc', exercise.toboggan_password))
    
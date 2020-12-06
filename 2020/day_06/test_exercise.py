import unittest
import exercise

def get_input():
    return """abc

a
b
c

ab
ac

a
a
a
a

b"""


class TestCustomsDeclaration(unittest.TestCase):
    def test_exercise_06a(self):
        self.assertEqual(exercise.get_sum_of_answers(get_input().split('\n\n')), 11)
    def test_exercise_06b(self):
        self.assertEqual(exercise.get_sum_of_consensus(get_input().split('\n\n')), 6)


    

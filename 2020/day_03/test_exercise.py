import unittest
import exercise

def get_input():
    return "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"

class TestPasswordValidator(unittest.TestCase):
    def test_exercise_03_1(self):
        self.assertEqual(exercise.get_tree_collisions(get_input().splitlines(), 0, 0, 3, 1), 7)
    def test_exercise_03_2(self):
        slopes = [[1,1], [3,1], [5,1], [7, 1], [1, 2]]
        collisions = exercise.get_tree_collision_product(get_input().splitlines(), 0, 0, slopes)
        self.assertEqual(collisions, 336)



    
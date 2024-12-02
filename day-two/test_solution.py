import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution([], 0, 0)
        self.solution.get_levels("test_input.txt")
        self.solution_two = solution([], 0, 0)
        self.solution_two.get_levels("test_input_2.txt")

    def test_safe_levels(self):
        # Arrange
        expected_safe = 2

        # Act
        actual_safe = self.solution.get_safe_levels()

        # Assert
        self.assertEqual(expected_safe, actual_safe)

    def test_safe_levels_two(self):
        # Arrange
        expected_safe = 5

        # Act
        actual_safe = self.solution_two.get_safe_levels()

        # Assert
        self.assertEqual(expected_safe, actual_safe)


if __name__ == "__main__":
    unittest.main()

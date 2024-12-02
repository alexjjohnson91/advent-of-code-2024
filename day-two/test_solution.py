import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution([])
        self.solution.get_levels("test_input.txt")

    def test_safe_levels(self):
        # Arrange
        expected = 2

        # Act
        actual = self.solution.get_safe_levels()

        # Assert
        self.assertEqual(expected, actual)

    def test_unsafe_levels(self):
        # Arrange
        expected = 4

        # Act
        actual = self.solution.get_unsafe_levels()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

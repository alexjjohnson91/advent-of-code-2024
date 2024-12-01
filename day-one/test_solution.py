import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution([], [])
        self.solution.get_arrays("test_input.txt")

    def test_distance(self):
        # Arrange
        expected = 11

        # Act
        actual = self.solution.get_distance()

        # Assert
        self.assertEqual(expected, actual)

    def test_similarity(self):
        # Arrange
        expected = 31

        # Act
        actual = self.solution.get_similarity()

        # Assert
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

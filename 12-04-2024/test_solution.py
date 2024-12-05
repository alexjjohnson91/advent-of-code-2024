import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution("test_input.txt")

    def test_word_search(self):
        # Arrange
        expected_words = 18

        # Act
        actual_words = self.solution.find_words()

        # Assert
        self.assertEqual(expected_words, actual_words)

    def test_part_two(self):
        # Arrange
        expected_words = 9

        # Act
        actual_words = self.solution.count_xmas()

        # Assert
        self.assertEqual(expected_words, actual_words)


if __name__ == "__main__":
    unittest.main()

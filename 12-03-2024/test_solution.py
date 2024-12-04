import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution("test_input.txt")

    def setup_method(self, method):
        print("starting new test" + method)
        self.matches = []

    def test_result(self):
        # Arrange
        expected_result = 161
        self.solution.get_matches()

        # Act
        actual_result = self.solution.get_result()

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_result_recursive(self):
        # Arrange
        expected_result = 48
        self.solution.get_matches_recursive(self.solution.text, True)

        # Act
        actual_result = self.solution.get_result()

        # Assert
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()

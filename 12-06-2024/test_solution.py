import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution("test_input.txt")

    def test_distinct_positions(self):
        expected = 41
        actual = self.solution.get_distinct_positions()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

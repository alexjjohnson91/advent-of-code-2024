import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution("test_input.txt")

    def test_solution(self):
        expected = 143
        actual = self.solution.count_middle_pages()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

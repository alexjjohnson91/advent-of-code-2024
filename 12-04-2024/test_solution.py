import unittest
from solution import solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = solution("test_input.txt")


if __name__ == "__main__":
    unittest.main()

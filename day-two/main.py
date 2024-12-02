from solution import solution

if __name__ == "__main__":
    day_two_solution = solution([], 0, 0)
    day_two_solution.get_levels("input.txt")
    print("safe levels", str(day_two_solution.get_safe_levels()))

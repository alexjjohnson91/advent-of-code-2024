from solution import solution

if __name__ == "__main__":
    day_three_solution = solution("input.txt")
    day_three_solution.get_matches_recursive(day_three_solution.text, True)

    print(day_three_solution.get_result())

from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    solution = solution([], [])
    solution.get_arrays("input.txt")
    print(solution.get_distance())
    print(solution.get_similarity())

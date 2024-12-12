from solution import solution


def log(msg):
    print(msg)


if __name__ == "__main__":
    sln = solution([], [])
    sln.get_arrays("input.txt")
    print(sln.get_distance())
    print(sln.get_similarity())

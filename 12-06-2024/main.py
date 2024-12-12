from solution import solution

if __name__ == "__main__":
    sln = solution("input.txt")

    print(sln.current_x, sln.current_y)
    print(sln.border_x, sln.border_y)

    print(sln.get_distinct_positions())





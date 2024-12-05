class solution:
    def __init__(self, file_name):
        with open(file_name, "r") as file:
            self.grid = [list(line.strip()) for line in file]
        self.row, self.col = len(self.grid), len(self.grid[0])

    def find_words(self):
        words = 0
        xmas = "XMAS"
        samx = "SAMX"

        for row in self.grid:
            row_string = "".join(row)
            words += row_string.count(xmas)
            words += row_string.count(samx)

        for col_idx in range(len(self.grid[0])):
            col_string = "".join(row[col_idx] for row in self.grid)
            words += col_string.count(xmas)
            words += col_string.count(samx)

        n, m = len(self.grid), len(self.grid[0])
        for start in range(-(n - 1), m):
            diagonal = "".join(
                self.grid[r][c] for r in range(n) for c in range(m) if c - r == start
            )
            words += diagonal.count(xmas)
            words += diagonal.count(samx)

        for start in range(m + n - 1):
            diagonal = "".join(
                self.grid[r][c] for r in range(n) for c in range(m) if r + c == start
            )
            words += diagonal.count(xmas)
            words += diagonal.count(samx)
        return words

    def count_xmas(self):
        n, m = len(self.grid), len(self.grid[0])
        xmas_count = 0

        for r in range(n - 2):
            for c in range(m - 2):
                diagonal1 = (
                    self.grid[r][c] + self.grid[r + 1][c + 1] + self.grid[r + 2][c + 2]
                )
                diagonal2 = (
                    self.grid[r][c + 2] + self.grid[r + 1][c + 1] + self.grid[r + 2][c]
                )
                if (diagonal1 in {"MAS", "SAM"}) and (diagonal2 in {"MAS", "SAM"}):
                    xmas_count += 1

        return xmas_count

    def print_grid(self):
        for row in self.grid:
            print(row)

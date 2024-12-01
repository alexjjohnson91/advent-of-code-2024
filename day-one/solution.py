class solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def solve(self):
        return self.a[0] + self.b[0]

    def get_arrays(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                x, y = map(int, line.split())

                self.a.append(x)
                self.b.append(y)

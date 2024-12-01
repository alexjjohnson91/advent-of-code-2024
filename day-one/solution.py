class solution:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_distance(self):
        self.a.sort()
        self.b.sort()
        distance = 0
        for i in range(len(self.a)):
            distance += abs(self.a[i] - self.b[i])

        return distance

    def get_similarity(self):
        similarity = 0

        for i in range(len(self.a)):
            similarity += self.a[i] * self.b.count(self.a[i])

        return similarity

    def get_arrays(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                x, y = map(int, line.split())
                self.a.append(x)
                self.b.append(y)

class solution:
    def __init__(self, a):
        self.a = a

    def get_safe_levels(self):
        return 0

    def get_unsafe_levels(self):
        return 0

    def get_safe_level(self, level):
        for i in range(len(level)):
            print(i)

    def get_levels(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                level = [int(x) for x in line.split()]
                self.a.append(level)

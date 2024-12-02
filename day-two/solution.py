class solution:
    def __init__(self, a, safe_levels):
        self.a = a
        self.safe_levels = safe_levels

    def get_safe_levels(self):
        for i in range(len(self.a)):
            if self.get_safe_level(self.a[i]) == True:
                self.safe_levels += 1
        return self.safe_levels

    def get_safe_level(self, level):
        for i in range(1, len(level)):
            prev = level[i - 1]
            curr = level[i]
            if prev > curr:
                print("current array is descending")
                return self.get_safe_level_desc(level)
            else:
                print("current array is ascending")
                return self.get_safe_level_asc(level)
        return False

    def get_safe_level_asc(self, level):
        i = 1
        while i < len(level):
            prev = level[i - 1]
            curr = level[i]
            print("prev: " + str(prev) + "\tcurr: " + str(curr))
            if curr < prev:
                print("broken direction")
                return False
            elif curr == prev:
                print("levels are equal")
                return False
            elif abs(prev - curr) > 3:
                print("range is broken")
                return False
            else:
                i += 1
        return True

        
    def get_safe_level_desc(self, level):
        i = 1
        while i < len(level):
            prev = level[i - 1]
            curr = level[i]
            print("prev: " + str(prev) + "\tcurr: " + str(curr))
            if curr > prev:
                print("broken direction")
                return False
            elif curr == prev:
                print("levels are equal")
                return False
            elif abs(prev - curr) > 3:
                print("range is broken")
                return False
            else: 
                i += 1 
        return True

    def get_levels(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                level = [int(x) for x in line.split()]
                self.a.append(level)

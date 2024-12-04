import re


class solution:
    def __init__(self, file_name):
        with open(file_name, "r") as file:
            self.text = file.read().replace("\n", "")
        self.matches = []
        self.mul_pattern = r"mul\([0-9]+,[0-9]+\)"
        self.do_pattern = r"do\(\)"
        self.dont_pattern = r"don't\(\)"

    def get_matches(self):
        self.matches = re.findall(self.mul_pattern, self.text)

    def get_matches_recursive(self, text_string, enabled_flag):
        print("searching: " + text_string)

        if enabled_flag == True:
            # first look for disable pattern
            dont_match = re.search(self.dont_pattern, text_string)
            mul_match = re.search(self.mul_pattern, text_string)

            if (dont_match and mul_match) and dont_match.start() < mul_match.start():
                print("found " + dont_match.group() + " disabling")
                self.get_matches_recursive(text_string[dont_match.end() :], False)
            elif mul_match:
                print("found " + mul_match.group() + " appending to list")
                self.matches.append(mul_match.group())
                print(mul_match.group())
                self.get_matches_recursive(text_string[mul_match.end() :], enabled_flag)
            else:
                return
        else:  # if disabled, look for an enable pattern
            match = re.search(self.do_pattern, text_string)
            if match:
                print("found " + match.group() + " enabling")
                self.get_matches_recursive(text_string[match.end() :], True)
        return

    def get_result(self):
        result = 0

        for match in self.matches:
            x, y = re.findall(r"[0-9]+", match)
            result += int(x) * int(y)
            print(match)

        return result

    def get_text(self, file_name):
        with open(file_name, "r") as file:
            self.text = file.read().replace("\n", "")

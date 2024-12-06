class solution:
    def __init__(self, file_name):
        with open(file_name, "r") as file:
            self.rules = self.get_rules(file)
            self.updates = self.get_updates(file)
        self.valid_updates = self.get_valid_updates()

    def count_middle_pages(self):
        sum = 0
        for update in self.valid_updates:
            sum += update[int(len(update) / 2)]

        return sum

    def get_valid_updates(self):
        valid_updates = []
        for update in self.updates:
            print("checking: ", str(update))
            if self.check_update(update):
                valid_updates.append(update)
        return valid_updates

    def check_update(self, update):
        for page_number in update:
            print("checking page: ", str(page_number))
            if self.check_rules_for_page_number(update, page_number):
                continue
            else:
                return False
        return True

    def check_rules_for_page_number(self, update, page_number):
        for rule in self.get_rules_for_page(page_number):
            if page_number in rule:
                cri = rule.index(page_number)
                cui = update.index(page_number)
                if rule[1 - cri] not in update:
                    continue
                tui = update.index(rule[1 - cri])
                if cri == 0:
                    if tui > cui:
                        continue
                    else:
                        return False
                else:
                    if tui < cui:
                        continue
                    else:
                        return False
        return True

    def get_rules_for_page(self, page_number):
        rules = []
        for rule in self.rules:
            if page_number in rule:
                rules.append(rule)

        return rules

    def get_updates(self, file):
        updates = []
        for line in file:
            numbers = [int(num) for num in line.strip().split(",")]
            updates.append(numbers)
        return updates

    def get_rules(self, file):
        rules = []
        for line in file:
            if line.strip():
                numbers = [int(num) for num in line.strip().split("|")]
                rules.append(numbers)
            else:
                break

        return rules

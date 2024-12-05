class solution:
    def __init__(self, file_name):
        with open(file_name, "r") as file:
            self.rules = self.get_rules(file)
            self.updates = self.get_updates(file)

    def get_pages(self):
        return 0
        
    def print_rules(self):
        for update in self.updates:
            print("Current Update: ", update)
            for page_number in update:
                print("Rules for: " + str(page_number))
                print(self.get_rules_for_page(page_number))

        return 0

    def get_rules(self, file):
        rules = []
        for line in file: 
            if line.strip():
                numbers = [int(num) for num in line.strip().split('|')]
                rules.append(numbers)
            else:
                break

        return rules

    def get_rules_for_page(self, page_number):
        rules_for_page = []
        for rule in self.rules:
            if page_number in rule:
                rules_for_page.append(rule)

        return rules_for_page
                

    def get_updates(self, file):
        updates = []
        for line in file: 
            numbers = [int(num) for num in line.strip().split(',')]
            updates.append(numbers)
        return updates

    def print_updates(self):
        for update in self.updates:
            for number in update:
                print(number)


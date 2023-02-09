
class Maks:
    def __init__(self):
        self.name_m = str("Maks")
        self.age = int(32)
        self.hug = "//input[@class='gLFyf']"

    def print_data(self, new_name=None, new_age=None):
        if not new_name:
            new_name = self.name_m
        if not new_age:
            new_age = self.age
        print(f"My name is {new_name}. My age {new_age}")

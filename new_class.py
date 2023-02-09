from main import Maks


class Liza(Maks):
    def __init__(self):
        super().__init__()
        self.name = "Liza"
        self.age = 32

    def print_(self):
        print(self.print_data())


Liza().print_()
import unittest
from main import Maks
from new_class import Liza


class Tests():
    def __init__(self):
        super().__init__()
        self.maks = Maks()
        self.liza = Liza()

    def test_names(self):
        self.maks.print_data(self.liza.name, self.liza.age)
# Maks().print_data(new_age=Liza().age, new_name=Liza().name)

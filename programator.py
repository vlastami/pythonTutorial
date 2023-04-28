
from clovek import Clovek

class Programator(Clovek):

    def __init__(self, jmeno, vek, jazyk):
        super().__init__(jmeno, vek)
        self.__jazyk = jazyk

    def get_jazyk(self):
        return self.__jazyk
    def pozdrav(self, pozdrav = None):
        if (pozdrav == None):
            print("Hello World")
        else: super(Programator, self).pozdrav()
    def vypis_povolani(self):
        print("Programátor")
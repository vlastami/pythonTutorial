from abc import ABC, abstractmethod
import copy

class Clovek(ABC):
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek
        Clovek.pridej_cloveka()
    def get_age(self):
        return self._vek
    def set_age(self, x):
        self._vek = x

    _pocetLidi = 0

    PLNOLETOST = 18

    @staticmethod
    def pridej_cloveka():
        Clovek._pocetLidi += 1

    @staticmethod
    def get_pocet_lidi():
        return Clovek._pocetLidi

    @abstractmethod
    def vypis_povolani(self):
        return "Nemám povolání."

    def __str__(self):
        return f"{self._jmeno}, {self._vek}"


    def pozdrav(self,pozdrav):
        print(f"{pozdrav} {self._jmeno}, {self._vek}")
    def pozdrav(self, pozdrav = "Ahoj"):
        print(f"{pozdrav} {self._jmeno}")


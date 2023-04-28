from abc import ABC, abstractmethod
from enum import Enum
class Zvire():
    def __init__(self, vaha):
        self.__vaha = vaha

    class Zbarveni(Enum):
        zbarveni_bile = 1
        zbarveni_modre = 2
        zbarveni_zelene = 3

    def get_leta(self):
        return self.__vaha < 9

    def get_vaha(self):
        return self.__vaha

    def nakrm(self, hmotnost):
        self.__vaha += hmotnost

    @abstractmethod
    def vydej_zvuk(self):
        return f""

    def __str__(self):
        if self.get_leta():
            return f"Létavé zvíře, {self.__vaha} Kg se zvukem {self.vydej_zvuk()}"
        else:
            return f"Nelétavé zvíře, {self.__vaha} Kg se zvukem {self.vydej_zvuk()}"


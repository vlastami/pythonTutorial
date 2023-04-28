from zvire import Zvire

class Kachna(Zvire):
    def __init__(self, vaha, barva):
        super().__init__(vaha)
        self.barva = barva

    def vydej_zvuk(self):
        return "Kač kač"
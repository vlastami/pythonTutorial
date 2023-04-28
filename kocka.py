from zvire import Zvire

class Kocka(Zvire):
    def __init__(self, vaha, vek):
        super().__init__(vaha)
        self.vek = vek

    def vydej_zvuk(self):
        return f"Mňau"
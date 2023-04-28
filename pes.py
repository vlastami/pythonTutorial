from zvire import Zvire

class Pes(Zvire):
    def __init__(self, vaha, obojek):
        super().__init__(vaha)
        self.obojek = obojek
    def vydej_zvuk(self):
        return "Haf"

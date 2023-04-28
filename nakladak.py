class Nakladak:
   __naklad = 0
   def Naloz(self, hmotnost):
       self.__naklad += hmotnost
   def Vyloz(self, hmotnost):
       if hmotnost > self.__naklad:
           raise Exception("Nelze vyložit více než je náklad")
       self.__naklad -= hmotnost
   def Vypis(self):
       print(f"Mám naloženo {self.__naklad} Kg.")
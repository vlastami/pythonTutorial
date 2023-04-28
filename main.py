from clovek import Clovek
from programator import Programator
from kachna import Kachna
from pes import Pes
from kocka import Kocka

from enum import Enum

class jazyk(Enum):
    CSharp = "CSharp"
    Java = "Java"
    PHP = "Php"
    Python = "Python"

jazyk = jazyk.CSharp
print(jazyk)
josef = Programator("Josef", 39, "C#")
karel = Programator("Karel", 42, "PHP")
josef.pozdrav("Zdar")
josef.pozdrav()
print(josef.get_jazyk())
print(f"{Clovek.get_pocet_lidi()}")

zvirata = []
zvirata.append(Pes(3, True))
zvirata.append(Kachna(1, "zelená"))
zvirata.append(Kocka(5, 3))

for zvire in zvirata:
    print(zvire.vydej_zvuk())

from nakladak import Nakladak

tatra = Nakladak()
tatra.Naloz(2000)
try:
    tatra.Vyloz(3000)
except Exception as e:
    print(e)
tatra.Vypis()



a = 20
b = 30
u = Programator("Karel", 20, "php")
v = Programator("Pepa", 23, "java")

a = b
print(a)

u=v
print(u)

print(Clovek.PLNOLETOST)
print(karel.PLNOLETOST)
Clovek.PLNOLETOST = 21
print(Clovek.PLNOLETOST)
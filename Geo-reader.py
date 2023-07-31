import math
class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x={self.x}, y={self.y}"

nume_fisier = "D:/Practica/dategeo.txt"
ListaPuncte = []
skip_line = False
perimetru = 0
angleDegrees =0

# Cautam prin fisier liniile cu criteriul corect si cream obiecte carora le atribuim valorile.
with open(nume_fisier, "r") as fisier:
    for linie in fisier:
        if linie.startswith("P"):
            skip_line = True
        elif skip_line and not linie.startswith("P"):
            coordonate_punct = linie.split()
            if len(coordonate_punct) >= 2:
                try:
                    x = float(coordonate_punct[0])
                    y = float(coordonate_punct[1])
                    punct = Punct(x, y)
                    ListaPuncte.append(punct)
                except ValueError:
                    pass
            skip_line = False

for i in range(len(ListaPuncte) - 1):
    punct1 = ListaPuncte[i]
    punct2 = ListaPuncte[i + 1]
    distanta = math.sqrt((punct2.x - punct1.x) ** 2 + (punct2.y - punct1.y) ** 2)
    perimetru += distanta


with open(nume_fisier, "r") as fisier:
    linii = fisier.readlines()
    i = 0
    while i < len(linii):
        linie = linii[i]
        if linie.startswith("ARC"):
            i += 2  # Skip two lines below the current line
            if i < len(linii):
                valorii_arc = linii[i].split()
                print(valorii_arc)
                if len(valorii_arc) >= 3:
                        j=0
                        j in range(len(ListaPuncte))
                        punct1 = ListaPuncte[j + int(valorii_arc[0])]
                        punct2 = ListaPuncte[j + int(valorii_arc[1])]
                        punct3 = ListaPuncte[j + int(valorii_arc[2])]

                        angle2 = math.atan2(punct2.y - punct3.y, punct2.x - punct3.x)
                        angle1 = math.atan2(punct1.y - punct2.y, punct1.x - punct2.x)
                        angleDegrees = (angle1 - angle2) * 360 / (2 * math.pi)
                break
        i += 1
lungime_arc =0 
r=5
lungime_arc = angleDegrees * r
# Afisam puncteled
for index, punct in enumerate(ListaPuncte, start=1):
    print(f"Punct {index}: {punct}")
print("Perimetrul este:", perimetru)
print ("Unghi este de :",angleDegrees,"grade")
print(lungime_arc)
print("Perimeturl final este",perimetru+lungime_arc)


import os
from random import randint
from sty import bg, rs
from math import log

os.system("cls")

# initialisations
nbColonnes: int = 10
nbLignes: int = 10
Tab: list[int] = [[0] * nbLignes for _ in range(nbColonnes)]

# valeurs aléatoires
for x in range(0, nbColonnes):
    for y in range(0, nbLignes):
        Tab[x][y] = randint(0, 255)

# calcul de la luminosité
lum: int = 0
for x in range(0, nbColonnes):
    for y in range(0, nbLignes):
        lum += Tab[x][y]
lum = int(lum / (nbColonnes * nbLignes))

# affichages de la matrice originelle
L = 6 # Largeur d'une case
H = 2 # Hauteur d'une case
for x in range(0, nbColonnes):
    for y in range(0, nbLignes):
        print(f"\033[{y*H+1};{x*L+1}H{Tab[x][y]}")
        qui = bg(Tab[x][y], Tab[x][y], Tab[x][y]) + '  ' + bg.rs
        print(f"\033[{nbLignes * H + y + 1};{x * 2 + 1}H{qui}")

# nouvelle image plus contrastée
TabCon: list[int] = [[lum] * nbLignes for _ in range(nbColonnes)]
taux: int = 10
for x in range(0, nbColonnes):
    for y in range(0, nbLignes):
        if Tab[x][y] > lum:
            TabCon[x][y] = int(Tab[x][y] + log(Tab[x][y] - lum) * taux)
            TabCon[x][y] = min(TabCon[x][y], 255)
        elif Tab[x][y] < lum:
            TabCon[x][y] = int(Tab[x][y] - log(lum - Tab[x][y]) * taux)
            TabCon[x][y] = max(TabCon[x][y], 0)

# affichages matrice contrastée
for x in range(0, nbColonnes):
    for y in range(0, nbLignes):
        print(f"\033[{y*H+1};{(x + nbColonnes + 1) * L + 1}H{TabCon[x][y]}")
        qui = bg(TabCon[x][y], TabCon[x][y], TabCon[x][y]) + '   ' + bg.rs
        print(f"\033[{nbLignes * H + y + 1};{(nbColonnes + 1)*L + x * 2 + 1}H{qui}")

print("luminosité = " + str(lum))
"""
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását 
(fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
"""

import random
valasztott_szam = input("Fej, vagy írás? ")
sorsolt_szam = random.randint(1, 2)
fej = 1
iras = 2

if valasztott_szam == sorsolt_szam:
    print("Eltaláltad!")
else:
    print("Nem lesz jó, majd legközelebb!")


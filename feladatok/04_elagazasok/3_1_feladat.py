"""
3. feladat
A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! 
Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb. 
"""

import random

gondolt_szam = random.randint(1,5)
# print(f"a random szám: {gondolt_szam}")

szam = int(input("Kérek egy számot! "))

if szam == gondolt_szam:
    print("Eltaláltad! ;)")
elif szam > gondolt_szam:
    print("Majdnem! Kicsit kevesebbet!")
else:
    print("Az úgy karcsú lesz! Kicsit több!")
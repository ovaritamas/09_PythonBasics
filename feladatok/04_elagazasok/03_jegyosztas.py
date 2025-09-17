"""Kérj be egy pontszámot 0–100 között, és írd ki az érdemjegyet:
    0-49: Elégtelen
    50-64: Elégséges
    65-79: Közepes
    80-89: Jó
    90-100: Jeles
"""

pontszam = int(input("Add meg a pontszámodtat [0-100]"))

if 0 < pontszam <= 49:
    print("Elégtelen")
elif 50 <= pontszam <= 64:
    print("Elégséges") 
elif 65 <= pontszam <= 79:
    print("Közepes")
elif 80 <= pontszam <= 89:
    print("Jó") 
elif 90 <= pontszam <= 100:
    print("Jeles") 
else:
    print("Ismeretlen számformátum! Próbáld újra! [0-100]")  
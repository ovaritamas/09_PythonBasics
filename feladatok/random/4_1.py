"""
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, 
majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal!
Az összehasonlítás eredményéről tájékoztassa a felhasználót! 
"""

import random

veletlen_szam = random.randint(1, 3)

megadott_szam = int(input("Gondolj egy számra (1-3): "))

if veletlen_szam == megadott_szam:
    print("Eltaláltad, gratulálok!:D ")
elif veletlen_szam > megadott_szam:
    print("Az úgy karcsú lesz!")
else:
    print("Sok lesz, kicsit kevesebbet")


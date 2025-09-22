"""
1.2 feladat
Fejleszd tovább az első feladat programját úgy, hogy amennyiben a felhasználó nem a két lehetséges válasz (igen/nem) 
közül ad meg egyet, a gép kiírja: "Sajnos nem értem a válaszodat!" 
"""

valasz = input("Jó napod van? (igen/nem)")

if valasz == "igen":
    print("Szükséged van egy teára, hogy még jobb legyen!")
elif valasz == "nem":
    print("🍔 - Itt egy hamburger, ettől jobb lesz.")
else:
    print("Sajnos nem értem a válaszodat!")
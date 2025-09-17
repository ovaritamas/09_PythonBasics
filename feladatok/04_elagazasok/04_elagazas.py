szam = float(input("Adj meg egy számot: "))

#Pozitív, negatív, nulla

if szam < 0:
    print("A szám negatív")
elif szam == 0:
    print("A szám nulla")
else:
    print("A szám pozitív")

#Paritás

if szam % 2 == 0 and szam != 0:
    print("A szám páros")
elif szam == 0:
    print("A szám páros")
else:
    print("A szám páratlan")


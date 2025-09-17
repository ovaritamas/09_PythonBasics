"""
Kérj be három egész számot, és írd ki, melyik a legnagyobb.
"""

first_num = int(input("Add meg az első számot: "))
second_num = int(input("Add meg az második számot: "))
third_num = int(input("Add meg az harmadik számot: "))

if first_num > second_num and third_num:
    print("Az első szám a legnagyobb")
elif second_num > first_num and third_num:
    print("A második szám a legnagyobb")
else:
    print("A harmadik szám a legnagyobb")
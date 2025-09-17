# Triangle area and circumfence calculation

a = float(input("Give the a side of the triangle: "))
b = float(input("Give the b side of the triangle: "))
c = float(input("Give the c side of the triangle: "))
ma = float(input("Give the ma of the triangle: ")) #height from a side

area = a + b + c
circumfence = a * ma / 2 

print(f"The area of the triangle: {area}")
print(f"The circumfence of the triangle: {circumfence}")
"""
Kérj be egy hőmérsékletet Celsiusban, és adj tanácsot:
- 0 alatt: „Nagyon hideg, öltözz melegen!”
- 0-20: „Hűvös, kabát ajánlott.”
- 21-30: „Kellemes idő.”
- 30 felett: „Forróság, igyál sok vizet!”

"""

temperature = float(input("Adj meg egy hőmérsékletet: "))
if temperature < 0:
    print("Nagyon hideg, öltözz melegen!")

elif temperature <= 20:
    print("Hűvös, kabát ajánlott.")

elif 21 <= temperature <= 30:
    print("Kellemes idő") 

elif temperature > 30:
    print("Forróság, igyál sok vizet!") 

else:
    print("Melyik bolygón élsz?")

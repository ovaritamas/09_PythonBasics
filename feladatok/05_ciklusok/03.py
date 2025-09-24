
folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False
    elif valasz == 'igen' or 'nem':
        print("Rossz formátum! (Csak i/n)")
print('>> Végre már <<')      
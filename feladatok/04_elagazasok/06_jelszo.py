"""
Kérj be egy jelszót, és ha megegyezik a „titok” szóval, írd ki: „Belépés engedélyezve!”, különben „Helytelen jelszó!”.
"""

password = input("Add meg a jelszavat: ")

if password == "titok":
    print("A jelszó helyes")
else:
    print("A jelszó helytelen! Próbáld újra később!")
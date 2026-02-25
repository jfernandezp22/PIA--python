password = "contraseña"
password_user = str(input("Introduzca la contraseña: "))

if password.lower() == password_user.lower():
    print("Todo OK")
else:
    print("Error")
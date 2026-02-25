edad = int(input("Introduzca su edad: "))
ingresos = int(input("Introduzca sus ingresos: "))

if edad >= 18 & ingresos >= 1000:
    print("Debes tributar")
else:
    print("No debes tributar")
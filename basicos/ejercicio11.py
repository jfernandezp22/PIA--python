interes = 0.04
cantidad = int(input("Introduzca la cantidad que va a depositar: "))

for i in range(1, 4, 1):
    interes_generado = cantidad * interes
    cantidad += interes_generado * 12
    print("Al finalizar el año", i, "habrá en la cuenta", round(cantidad, 2))
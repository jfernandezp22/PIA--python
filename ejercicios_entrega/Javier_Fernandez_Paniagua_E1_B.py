# PARTE B
numeros_dividir = []
bandera = True

for i in range(3):
    n = int(input("Escriba un número: "))
    numeros_dividir.append(n)

for n in numeros_dividir:
    for n2 in numeros_dividir:
        if n2 < n:
            continue
        elif n2 % n != 0:
            bandera = False
if bandera:
    print("Todos los números son divisibles entre sí")
else:
    print("Todos los números no son divisibles entre sí")
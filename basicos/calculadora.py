print("Bienvenido a la calculadora")

numero_1 = int(input("Primer número: "))
numero_2 = int(input("Segundo número: "))
operacion = input("Indica la operación a realizar (+, -, *, /): ")

if operacion == "+":
    print(numero_1 + numero_2)
elif operacion == "-":
    print(numero_1 - numero_2)
elif operacion == "*":
    print(numero_1 * numero_2)
elif operacion == "/":
    print(numero_1 / numero_2)
else:
    print("Operación no válida")
print("Bienvenido a la calculadora")

numero_1 = int(input("Primer número: "))
numero_2 = int(input("Segundo número: "))
operacion = input("Indica la operación a realizar (+, -, *, /): ")

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

match operacion:
    case "+":
        print(suma(numero_1, numero_2))
    case "-":
        print(resta(numero_1, numero_2))
    case "*":
        print(multiplicacion(numero_1, numero_2))
    case "/":
        print(division(numero_1, numero_2))
    case _:
        print("Operación no válida")
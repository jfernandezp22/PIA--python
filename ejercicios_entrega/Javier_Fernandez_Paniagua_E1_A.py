# PARTE A
n1 = int(input("Escriba un primer número: "))
n2 = int(input("Escriba un segundo número: "))
n3 = int(input("Escriba un tercer número: "))


if n3 > n2 and n2 > n1:
    print("El orden de los números es:", n1, n2, n3)
elif n1 < n2 and n1 < n3 and n3 < n2:
    print("El orden de los números es:", n1, n3, n2)
elif n3 > n2 and n2 < n1 and n3 > n1:
    print("El orden de los números es:", n2, n1, n3)
elif n1 > n2 and n2 < n3 and n1 > n3:
    print("El orden de los números es:", n2, n3, n1)
elif n1 > n2 and n2 > n3:
    print("El orden de los números es:", n3, n2, n1)
elif n3 < n1 and n3 < n2 and n1 < n2:
    print("El orden de los números es:", n3, n1, n2)
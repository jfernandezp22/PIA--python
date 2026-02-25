estatura = float(input("Introduce tu estatura en metros: "))
peso = float(input("Introduces tu peso en kilos: "))

print("Tu índice de masa corporal (IMC) es de ", round(peso / pow(estatura, 2), 2))
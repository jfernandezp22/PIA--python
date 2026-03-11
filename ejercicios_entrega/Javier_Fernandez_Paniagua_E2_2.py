anno = int(input("Escriba un año: "))

if anno % 400 == 0 or anno % 4 == 0:
    if anno % 100 == 0:
        print("El año", anno, "no es bisiesto")
    else:
        print("El año", anno, "es bisiesto")
else:
    print("El año", anno, "no es bisiesto")
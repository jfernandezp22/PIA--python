precio = 3.49
descuento = 0.6
n_barras_mal = int(input("Introduce el número de barras de pan vendidas que no eran del día: "))
print("Su precio habitual de venta hubiese sido:", n_barras_mal * precio)
print("Pero su precio de venta total ha sido:", (n_barras_mal * precio) * descuento)
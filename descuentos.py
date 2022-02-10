
# Precios
huevos_precio=float(input("Ingresar el precio del Maple de Huevos: ")) 
paleta_precio=float(input("Ingresar el precio del Kilo de Paleta: "))

# Cantidades
huevos_cant_maples=float(input("Ingresar cantidad de Maples de Huevos: "))
paleta_cant_kilo=float(input("Ingresar peso de Paleta: "))

# calculo de subtotales
huevos_subtotal=huevos_precio * huevos_cant_maples
paleta_subtotal=paleta_precio * paleta_cant_kilo 

# calculo del total
total=paleta_subtotal+huevos_subtotal 

# Calculo reintegro del 30%
reintegro_30=total*0.3

# Calculo descuento del 20%
descuento_20=paleta_subtotal*0.2

total_con_descuento=total-descuento_20

print("Subtotal Huevos: "+str(huevos_subtotal)+"$")
print("Subtotal Paleta: "+str(paleta_subtotal)+"$")
print("Total sin descuento: "+str(total)+"$")
print("Reintegro del 30%: "+str(reintegro_30)+"$")
print("Descuento del 20%: "+str(descuento_20)+"$")

print("Total con descuento: "+str(total_con_descuento)+"$")

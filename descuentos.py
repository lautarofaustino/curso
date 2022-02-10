
# Precios
coca_precio=float(input("Ingresar el precio de botellas de coca: ")) 
ricota_precio=float(input("Ingresar el precio del Kilo de ricota: "))

# Cantidades
coca_cant_botellas=float(input("Ingresar cantidad de botellas de coca: "))
ricota_cant_kilo=float(input("Ingresar peso de ricota: "))

#calculo de 2 x 1 
beneficios =int(coca_cant_botellas/2)
sobra=coca_cant_botellas-(beneficios*2)
coca_subtotal=coca_precio*(beneficios+sobra)

# calculo de subtotales
ricota_subtotal=ricota_precio * ricota_cant_kilo 

# calculo del total
total=ricota_subtotal+coca_subtotal 

# Calculo reintegro del 30%
reintegro_30=total*0.3

# Calculo descuento del 20%
descuento_35=ricota_subtotal*0.2

total_con_descuento=total-descuento_35


print("Subtotal cocas: "+str(coca_subtotal)+"$")
print("Subtotal ricota: "+str(ricota_subtotal)+"$")
print("Total sin descuento: "+str(total)+"$")
print("Reintegro del 30%: "+str(reintegro_30)+"$")
print("Descuento del 20%: "+str(descuento_35)+"$")

print("Total con descuento: "+str(total_con_descuento)+"$")

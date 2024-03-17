# Función que calcula el descuento en compras
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (porcentaje_descuento/100) * monto_total
    return descuento
# Primera llamada a la función calcular_descuento (proporcionando el monto total de la compra)
monto_total_compra1 = 8000
descuento1 = calcular_descuento(monto_total_compra1)
monto_final1 = monto_total_compra1 - descuento1
print("10% de descuento")
print("Primera Compra:")
print(f"Monto de la compra: ${monto_total_compra1}")
print(f"Monto del descuento: ${descuento1}")
print(f"Monto final a pagar después del descuento: ${monto_final1}")
# Segunda llamada a la función calcular_descuento (proporcionando el monto total de la compra como el porcentaje de descuento)
monto_total_compra2 = 500
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_total_compra2, porcentaje_descuento2)
monto_final2 = monto_total_compra2 - descuento2
print("20% de descuento")
print("Segunda Compra:")
print(f"Monto de la compra: ${monto_total_compra2}")
print(f"Monto del descuento: ${descuento2}")
print(f"Monto final a pagar después del descuento: ${monto_final2}")

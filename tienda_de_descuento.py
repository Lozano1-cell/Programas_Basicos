total = float(input("Ingresa el total de tu compra: "))

if total > 500:
    descuento = total * 0.20
elif total >= 200:
    descuento = total * 0.15
elif total >= 100:
    descuento = total * 0.10
else:
    descuento = 0.0

total_final = total - descuento
print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {total_final}")

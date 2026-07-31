#  Media de números positivos
suma = 0
cantidad = 0

print("Ingresa números positivos (ingresa un número negativo para terminar):")
while True:
    num = float(input("Número: "))
    if num < 0:
        break
    suma += num
    cantidad += 1

if cantidad > 0:
    media = suma / cantidad
    print(f"La media de los números positivos es: {media}")
else:
    print("No se ingresaron números positivos.")

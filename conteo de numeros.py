#  Conteo de números
mayores = 0
menores = 0
iguales = 0

n = int(input("¿Cuántos números deseas evaluar?: "))
for _ in range(n):
    num = float(input("Ingresa un número: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1

print(f"Mayores a cero: {mayores}")
print(f"Menores a cero: {menores}")
print(f"Iguales a cero: {iguales}")

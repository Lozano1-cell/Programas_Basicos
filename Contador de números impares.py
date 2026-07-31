#  Contador de números impares
contador_impares = 0
print("Ingresa números (el programa cuenta cuántos impares ingresas, escribe 0 para salir):")
while True:
    num = int(input("Número: "))
    if num == 0:
        break
    if num % 2 != 0:
        contador_impares += 1

print(f"Total de números impares ingresados: {contador_impares}")

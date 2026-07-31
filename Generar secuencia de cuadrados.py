#  Generar secuencia de cuadrados
print("Generador de cuadrados. Ingresa un límite (ingresa 0 o negativo para salir):")
while True:
    n = int(input("Ingresa hasta qué número generar cuadrados: "))
    if n <= 0:
        print("Saliendo...")
        break
    
    i = 1
    while i <= n:
        print(f"El cuadrado de {i} es {i**2}")
        i += 1

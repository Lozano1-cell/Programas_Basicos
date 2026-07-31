#  Generar secuencia aritmética
print("Generador de progresión aritmética (ej. inicio, incremento y límite):")
while True:
    inicio = int(input("Ingresa el número inicial: "))
    incremento = int(input("Ingresa el valor del incremento: "))
    limite = int(input("Ingresa el valor límite: "))
    
    actual = inicio
    while actual <= limite:
        print(actual, end=" ")
        actual += incremento
    print()
    
    repetir = input("¿Deseas hacer otra secuencia? (s/n): ").lower()
    if repetir != 's':
        print("Finalizando programa.")
        break

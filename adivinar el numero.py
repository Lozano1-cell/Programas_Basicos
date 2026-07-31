# Adivinar el número
import random

secreto = random.randint(1, 100)
intento = 0

print("¡Adivina el número secreto entre 1 y 100!")
while intento != secreto:
    intento = int(input("Ingresa tu suposición: "))
    if intento < secreto:
        print("Demasiado bajo.")
    elif intento > secreto:
        print("Demasiado alto.")
    else:
        print("¡Felicidades, adivinaste el número!")

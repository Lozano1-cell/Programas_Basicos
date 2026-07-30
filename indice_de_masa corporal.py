# Programa 3: Cálculo del Índice de Masa Corporal (IMC)
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros (ej. 1.75): "))

imc = peso / (estatura ** 2)
print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

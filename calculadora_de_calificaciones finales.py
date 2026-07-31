# 1. Calculadora de calificaciones finales
parciales = float(input("Ingresa la calificación de parciales (0-100): "))
proyecto = float(input("Ingresa la calificación del proyecto (0-100): "))
examen = float(input("Ingresa la calificación del examen (0-100): "))

final = (parciales * 0.40) + (proyecto * 0.30) + (examen * 0.30)
print(f"La calificación final es: {final}")

celsius = float(input("Ingresa la temperatura en grados Celsius: "))
opcion = input("¿A qué deseas convertir? (Fahrenheit / Kelvin): ").strip().lower()

match opcion:
    case "fahrenheit" | "f":
        resultado = (celsius * 9/5) + 32
        print(f"Equivale a {resultado} °F")
    case "kelvin" | "k":
        resultado = celsius + 273.15
        print(f"Equivale a {resultado} K")
    case _:
        print("Opción de conversión no válida.")

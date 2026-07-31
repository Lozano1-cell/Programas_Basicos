mes = input("Ingresa el mes del año: ").strip().lower()

match mes:
    case "diciembre" | "enero" | "febrero":
        print("La estación es Invierno.")
    case "marzo" | "abril" | "mayo":
        print("La estación es Primavera.")
    case "junio" | "julio" | "agosto":
        print("La estación es Verano.")
    case "septiembre" | "octubre" | "noviembre":
        print("La estación es Otoño.")
    case _:
        print("Mes no válido.")

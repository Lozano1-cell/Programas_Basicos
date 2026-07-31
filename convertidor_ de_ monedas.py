pesos = float(input("Ingresa la cantidad en pesos mexicanos (MXN): "))
moneda = input("Ingresa la moneda destino (USD, EUR, THB, JPY, KRW, AUD, PEN, CAD, VES, ARS): ").strip().upper()

match moneda:
    case "USD":
        print(f"Equivale a: {pesos * 0.058} USD")
    case "EUR":
        print(f"Equivale a: {pesos * 0.053} EUR")
    case "THB":
        print(f"Equivale a: {pesos * 2.10} THB")
    case "JPY":
        print(f"Equivale a: {pesos * 9.10} JPY")
    case "KRW":
        print(f"Equivale a: {pesos * 80.50} KRW")
    case "AUD":
        print(f"Equivale a: {pesos * 0.088} AUD")
    case "PEN":
        print(f"Equivale a: {pesos * 0.22} PEN")
    case "CAD":
        print(f"Equivale a: {pesos * 0.080} CAD")
    case "VES":
        print(f"Equivale a: {pesos * 2.10} VES")
    case "ARS":
        print(f"Equivale a: {pesos * 50.20} ARS")
    case _:
        print("Moneda no reconocida.")

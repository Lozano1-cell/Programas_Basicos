#  Contador de dígitos
numero = int(input("Ingresa un número entero: "))
aux = abs(numero)
digitos = 0

if aux == 0:
    digitos = 1
else:
    while aux > 0:
        aux //= 10
        digitos += 1

print(f"El número {numero} tiene {digitos} dígitos.")

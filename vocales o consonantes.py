# Vocales o consonantes (ingresa letra por letra, presiona espacio para terminar)
print("Ingresa letras una por una (escribe un espacio o presiona Enter con espacio para salir):")
while True:
    caracter = input("Ingresa una letra: ")
    if caracter == " " or caracter == "":
        print("Fin del programa.")
        break
    
    letra = caracter.lower()
    if letra in "aeiouáéíóú":
        print(f"'{caracter}' es una vocal.")
    elif letra.isalpha():
        print(f"'{caracter}' es una consonante.")
    else:
        print("No es una letra válida.")

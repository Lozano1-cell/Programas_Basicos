#  Números divisibles por 3 y 5 del 1 al 100
print("Números divisibles por 3 y 5 entre 1 y 100:")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

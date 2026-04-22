n = int(input("¿Cuántos números deseas ingresar? "))
pares = 0
impares = 0
for i in range(1, n + 1):
    numero = int(input(f"Ingresa el número {i}: "))
    if numero % 2 == 0:
        print(f"{numero} es PAR")
        pares += 1
    else:
        print(f"{numero} es IMPAR")
        impares += 1
print("\n--- Resumen ---")
print(f"Cantidad de números pares:   {pares}")
print(f"Cantidad de números impares: {impares}")
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
if b == 0:
    print("El segundo número no puede ser 0 (división por cero).")
elif a % b == 0:
    print(f"{a} ES múltiplo de {b}.")
else:
    print(f"{a} NO es múltiplo de {b}.")
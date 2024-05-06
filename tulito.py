def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total 

numero = int(input("Ingrese un número: ")) 
if numero <= 0:
    print("Número no válido.")
else: 
    print("El factorial es: " + str(factorial(numero)))

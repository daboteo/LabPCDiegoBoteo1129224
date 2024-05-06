import math

print("Menu", "1. Sumar", 
"2. Restar",
"3. Multiplicar", 
"4. División",
"5. Raíz cuadrada",
"6. Potencia",
"7. Factorial",
sep= "\n")

opcion = input("Ingrese su opción: ")

if opcion == "1":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"La suma es: {num1 + num2}") 

elif opcion == "2":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"La resta es: {num1 - num2}")

elif opcion == "3":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    print(f"La multiplicación es: {num1 * num2}")

elif opcion == "4":
    num1 = int(input("Ingrese el numerador: "))
    num2 = int(input("Ingrese el denominador: "))
    if num2 == 0:
        print("Error, el denominador no puede ser cero")
    else:
        print(f"La división es: {num1 / num2}")

elif opcion == "5":
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("Error, ingrese un número entero positivo")
    else:
        print(f"La raíz cuadrada es: {math.sqrt(n)}")

elif opcion == "6":
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"La potencia es: {math.pow(base, exponente)}")

elif opcion == "7":
    n = int(input("Ingrese un número entero positivo: "))
    if n <= 0:
        print("Error, ingrese un número entero positivo")
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"El factorial es: {factorial}")

else:
    print("Opción no válida.")

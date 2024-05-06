def Sumar(num1,num2):
    Total = num1 + num2
    return Total

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

print("La suma es: " + str(Sumar(numero1,numero2)))

def multiplicar(num1,num2):
    Total = num1*num2
    return Total

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

print("La multiplicacion es: " + str(multiplicar(numero1,numero2)))

def dividir(num1,num2):
    Total = num1/num2
    return Total

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
if (numero2 == 0):
    print("El numero 0 no es valido")
else:
print("La division es: " + str(dividir(numero1,numero2)))

def restar(num1,num2):
    Total = num1-num2
    return Total

numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

print("La resta es: " + str(restar(numero1,numero2)))

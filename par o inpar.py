try:
    numero = int(input("Ingrese un numero: "))

    if numero<0:
        print ("su numero es negativo")
    elif numero==0:
        print ("su numero no es ni par ni impar")
    else:
        print("su numero es positivo ") 
        if numero%2==0:
            print("su numero es par")
        else: 
            print("su numero es impar")
except ValueError:
    print ("Ingrese un valor valido ")
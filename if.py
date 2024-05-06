edad = int(input("ingrese un número: "))
if edad<0 or edad>120: 
    print("Edad no valida  ")
else: 
     if edad>=18: 
        print("la persona es mayor de edad")
     else: 
         print("la persona es menor de edad")
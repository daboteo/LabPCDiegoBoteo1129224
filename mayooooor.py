
n = int(input("¿Cuantas edades deseas ingresar? ")) 
lista = []
cantidad = 0 

while cantidad<n:
    valor = int(input("Ingrese un numero: "))
    if (valor>0): 
        lista.append(valor) 
        cantidad = cantidad+1
    else: 
        print("Numero no valido, ingrese un valor de nuevo")

mayor = 0 
for i in lista: 
    if (i>mayor):
        mayor = i

print("El valor mayor es "+ str(mayor))
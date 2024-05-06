#Ejercicio Condicionales Diego Boteo y Rafael Guevara 
#Problema 1 
print("Bienvenido a nuestro cajero")
monto = int(input("Ingrese su cantidad a pagar: "))
descuento = 0
codigo = input("Tiene algun codigo de descunto? s/n: ")

if monto < 400:
    descuento = monto * 0 
    print("No aplica descuento")
elif monto >= 400 and monto < 1000:
    descuento = monto * 0.07
    print("Se aplicó un 7 por ciento de descuento")
elif monto>= 1000 and monto <5000:
    descuento = monto * 0.10
    print("Se aplicó un 10 por ciento de descuento")
elif monto >= 5000 and monto < 15000:
    descuento = monto * 0.15
    print("Se aplicó un 15 por ciento de descuento")
elif monto >= 15000:
    descuento = monto * 0.25
    print("Se aplicó un 25 por ciento de descuento")
if  codigo == "s":
    descuento += monto *0.05
    print("Se aplicó un 5 por ciento de descuento por su codigo")

total_a_pagar = monto - descuento
print(f"Total a pagar: {total_a_pagar}")

#Problema 2 
print("Bienvenido a envios en la ciudad de Guatemala")

v1 = input("¿Desea el envío en vehículo o motocicleta? : m/v ")
try:
    kilometros = int(input("¿Cuántos kilómetros desea realizar el envío?: "))

    if v1 == "m":
        costf = 10 
        if kilometros < 5:
            costo_km = kilometros * 3
        elif 5 <= kilometros < 10:
            costo_km = kilometros * 2.50
        else:
            costo_km = kilometros * 2
        preciof = costf + costo_km 
        print(f"El precio final es {preciof}")
    elif v1 == "v":
        costf = 20 
        if kilometros < 5:
            costo_km = kilometros * 6
        elif 5 <= kilometros < 10:
            costo_km = kilometros * 5
        else:
            costo_km = kilometros * 4
        preciof = costf + costo_km 
        print(f"El precio final es {preciof}")
        
except ValueError:
    print("Ingrese un valor válido")

    
 
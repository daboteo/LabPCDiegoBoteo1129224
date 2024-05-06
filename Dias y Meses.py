
print()
print()
print("Ejercicio 1: Días")

try:
    días=int(input("Ingrese un número para asignarle un día de la semana: "))
    if días>7 or días<1:
        print("Número de la semana inválido")
    elif días==1:
        print("Lunes")
    elif días==2:
        print("Martes")
    elif días==3:
        print("Miércoles")
    elif días==4:
        print("Jueves")
    elif días==5:
        print("Viernes")
    elif días==6:
        print("Sábado")
    else: 
        print("Domingo")
except ValueError:
    print("Por favor ingrese un valor válido")

print()
print()
print("Ejercicio 2: Meses")
print()
try: 
    mes=input("Ingrese un mes del año: ")
    mes1="Enero" and "enero"
    mes2="Febrero" and "Febrero"
    mes3="Marzo" and "marzo"
    mes4="Abril" and "abril"
    mes5="Mayo" and "mayo"
    mes6="Junio" and "junio"
    mes7="Julio" and "julio"
    mes8="Agosto" and "agosto"
    mes9="Septiembre" and "septiembre"
    mes10="Octubre" and "octubre"
    mes11="Noviembre" and "noviembre"
    mes12="Diciembre" and "diciembre"

    if mes==mes1:
        print("January")
    elif mes==mes2:
        print("February")
    elif mes==mes3:
        print("March")
    elif mes==mes4:
        print("April")
    elif mes==mes5:
        print("May")
    elif mes==mes6:
        print("June")
    elif mes==mes7:
        print("July")
    elif mes==mes8:
        print("August")
    elif mes==mes9:
        print("September")
    elif mes==mes10:
        print("October")
    elif mes==mes11:
        print("November")
    elif mes==mes12:
        print("December")
    else:
        print("El mes que eligió no existe")

except ValueError:
    print("Por favor ingrese un mes válido")
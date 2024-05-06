print ("semana no. 10: Ejercicio 1: ")

mesEntrada = int(input("Ingrese un número del 1-12: "))
mesSalida = " "
match mesEntrada:
    case 1:
        mesSalida = "Enero"
    case 2: 
        mesSalida = "Febrero"
    case 3:
        mesSalida = "Marzo"
    case 4: 
        mesSalida = "Abril"
    case 5:
        mesSalida = "Mayo"
    case 6: 
        mesSalida = "Junio"
    case 7:
        mesSalida = "Julio"
    case 8:
        mesSalida = "Agosto"
    case 9: 
        mesSalida = "Septiembre"
    case 10:
        mesSalida = "Octubre"
    case 11: 
        mesSalida = "Noviembre"
    case 12:
        mesSalida = "Diciembre"
    
    case _: 
        print("Error: El numero a ingresar debe de ser del 1 al 12")

print(f"MES: {mesSalida}")

#Actividad 2 
print("Ejercicio 2: " )
A = int(input("Ingrese un primer numero mayor a 0: "))
B = int(input("Ingrese un segundo numero mayor a 0: "))
C = int(input("Ingrese un tercer numero mayor a 0: "))

if A > B:
    if A > C:
        print("A es el mayor.")
    elif A == C:
        print("A y C son mayores que B.")
    else:
        print("C es el mayor.")
elif A == B:
    if A > C:
        print("A y B son mayores que C.")
    elif A == C:
        print("Todos los números son iguales.")
    else:
        print("C es el mayor.")
else:
    if B > C:
        print("B es el mayor.")
    elif B == C:
        print("B y C son mayores que A.")
    else:
        print("C es el mayor.")

#Actividad 03 
dia = int(input("Ingrese el día de su fecha de nacimiento: "))
mes = int(input("Ingrese el mes de su fecha de nacimiento: "))

signo = ""

if mes == 1:
    if dia <= 19:
        signo = "Capricornio"
    else:
        signo = "Acuario"
elif mes == 2:
    if dia <= 18:
        signo = "Acuario"
    else:
        signo = "Piscis"
elif mes == 3:
    if dia <= 20:
        signo = "Piscis"
    else:
        signo = "Aries"
elif mes == 4:
    if dia <= 19:
        signo = "Aries"
    else:
        signo = "Tauro"
elif mes == 5:
    if dia <= 20:
        signo = "Tauro"
    else:
        signo = "Géminis"
elif mes == 6:
    if dia <= 20:
        signo = "Géminis"
    else:
        signo = "Cáncer"
elif mes == 7:
    if dia <= 22:
        signo = "Cáncer"
    else:
        signo = "Leo"
elif mes == 8:
    if dia <= 22:
        signo = "Leo"
    else:
        signo = "Virgo"
elif mes == 9:
    if dia <= 22:
        signo = "Virgo"
    else:
        signo = "Libra"
elif mes == 10:
    if dia <= 22:
        signo = "Libra"
    else:
        signo = "Escorpio"
elif mes == 11:
    if dia <= 21:
        signo = "Escorpio"
    else:
        signo = "Sagitario"
elif mes == 12:
    if dia <= 21:
        signo = "Sagitario"
    else:
        signo = "Capricornio"
else:
    print("Mes inválido")

print("Su signo zodiacal es:", signo)

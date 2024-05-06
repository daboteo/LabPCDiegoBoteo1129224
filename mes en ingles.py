print ("semana no. 10: Ejercicio 1: ")

mesEntrada = (input("Ingrese un mes del año (escribalo con la primer letra en mayusculasFeb y sin espacios): "))
mesSalida = " "
match mesEntrada:
    case "Enero":
        mesSalida = "January"
    case "Febrero": 
        mesSalida = "February"
    case "Marzo":
        mesSalida = "March"
    case "Abril": 
        mesSalida = "April"
    case "Mayo":
        mesSalida = "May"
    case "Junio": 
        mesSalida = "June"
    case "Julio":
        mesSalida = "July"
    case "Agosto":
        mesSalida = "August"
    case "Septiembre": 
        mesSalida = "September"
    case "Octubre":
        mesSalida = "October"
    case "Noviembre": 
        mesSalida = "November"
    case "Diciembre":
        mesSalida = "December"
    
    case _: 
        print("Error: El numero a ingresar debe de ser del 1 al 12")

print(f"Traduccion: {mesSalida}")
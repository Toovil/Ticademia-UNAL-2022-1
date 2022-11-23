def zeller(dia, mes, año):
    
    return None

def main():
    cantidad = int(input())
    
    for i in range(cantidad):
        fecha = input().split("-")
        dia, mes, año = fecha[0], fecha[1], fecha[2]

        if(mes == "enero" or mes == "febrero"):
            año = int(año) - 1                   # <----- OJO, SE PODRÍA USAR PARA SUMAR LAS VENTAS DEL EJERCICIO ANTERIOR

        print(zeller(dia, mes, año))


main()
def insalubles(empleado):
    imc = round((float(empleado[1])/(float(empleado[2]))**2), 1)
    if imc > 25 and float(empleado[3]) > 100 and (float(empleado[4])) > 150:
        return [empleado[0], imc]
    return None


num_empleados = int(input())
lista_insalubles = []
count = 0

for i in range(num_empleados):
    empleado = input().split(", ")
        
    if insalubles(empleado) != None:
        lista_insalubles.append(insalubles(empleado))

lista_insalubles.sort(key=lambda x: x[0], reverse=True)
lista_insalubles.sort(key=lambda x:x[1], reverse=True)

for j in lista_insalubles:
    count += 1
    print(count, *j)
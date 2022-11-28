from datetime import datetime

def duracion(inicio, fin):
    inicio = datetime.strptime(inicio, '%Y-%m-%d')
    fin = datetime.strptime(fin, '%Y-%m-%d')

    diferencia = fin - inicio

    dias = diferencia.days
    horas = dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    return (
        dias,
        horas,
        minutos,
        segundos
    )

num = int(input())

resultados = []

for i in range(num):
    entrada_tiempo = input()
    entrada_tiempo = entrada_tiempo.split(" ")
    fecha_inicial, fecha_final = entrada_tiempo[1], entrada_tiempo[2]

    resultados.append(duracion(fecha_inicial, fecha_final))

for r in resultados:
    days, hours, minutes, seconds = r
    print(f'{days} dias = {hours} horas = {minutes} minutos = {seconds} segundos')



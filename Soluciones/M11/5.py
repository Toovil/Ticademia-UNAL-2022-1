#Casi
from datetime import timedelta

def tiempo_en(registers):
    tiempo_barbero = []
    for r in registers:
        date, empieza_tiempo, tiempo_atrás = r
        hora_0, min_0, seg_0 = empieza_tiempo.split(":")
        hora_1, min_1, seg_1 = tiempo_atrás.split(":")
        empieza_tiempo = timedelta(hours=int(hora_0), minutes=int(min_0), seconds=int(seg_0))
        tiempo_atrás = timedelta(hours=int(hora_1), minutes=int(min_1), seconds=int(seg_1))
        restante = tiempo_atrás - empieza_tiempo

        tiempo_barbero.append(restante)

    promo = sum(tiempo_barbero, start=timedelta()) / len(tiempo_barbero)
    hora, minu, seg = promo.seconds // 3600, promo.seconds // 60 % 60, promo.seconds % 60

    print(f"{hora} horas, {minu} minutos, {seg} segundos")



c = int(input())
registers = []

for i in range(c):
    entry = input()
    date, place, empieza_tiempo, tiempo_atrás = entry.split(", ")

    if place == "barberia":
       registers.append([date, empieza_tiempo, tiempo_atrás])

tiempo_en(registers)



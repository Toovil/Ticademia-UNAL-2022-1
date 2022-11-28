def formateo_hora(time):
    tiempo, tz = time.split(" ")
    hora, minuto, segundo = tiempo.split(":")
    hora, minuto, segundo = int(hora), int(minuto), int(segundo)

    if hora == 12 and tz == "AM":
        hora -= 12

    if tz == "PM" and hora != 12:
        hora = int(hora) + 12

    return (hora * 60 * 60) + (minuto * 60) + segundo


def izquierda(tiempo):
    dia = 86400
    formateo = formateo_hora(tiempo)
    return round((formateo * 100) / dia, 3)



c = int(input())

for i in range(c):
    entrada = input()
    resultado = izquierda(entrada)

    print(f"Loading day ... {resultado}%")



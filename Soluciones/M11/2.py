from datetime import datetime


def impresora(resultado):
    print(f'true vampires {resultado["true vampires"]}')
    print(f'early birds {resultado["early birds"]}')
    print(f'sunny warmers {resultado["sunny warmers"]}')
    print(f'lunch workers {resultado["lunch workers"]}')
    print(f'sunset lovers {resultado["sunset lovers"]}')
    print(f'prime timers {resultado["prime timers"]}')


def horario(arreglo_tiempo):
    calidad = {
        "true vampires": 0,
        "early birds": 0,
        "sunny warmers": 0,
        "lunch workers": 0,
        "sunset lovers": 0,
        "prime timers": 0
    }

    for time in arreglo_tiempo:
        tiempo_parseado = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        date = time.split(" ")[0]
        if (datetime.strptime(f"{date} 00:00:00", '%Y-%m-%d %H:%M:%S') <= tiempo_parseado <= datetime.strptime(
                f"{date} 03:59:59", '%Y-%m-%d %H:%M:%S')):
            calidad["true vampires"] += 1
        elif (datetime.strptime(f"{date} 04:00:00", '%Y-%m-%d %H:%M:%S') <= tiempo_parseado <= datetime.strptime(
                f"{date} 07:59:59", '%Y-%m-%d %H:%M:%S')):
            calidad["early birds"] += 1
        elif (datetime.strptime(f"{date} 08:00:00", '%Y-%m-%d %H:%M:%S') <= tiempo_parseado <= datetime.strptime(
                f"{date} 11:59:59", '%Y-%m-%d %H:%M:%S')):
            calidad["sunny warmers"] += 1
        elif (datetime.strptime(f"{date} 12:00:00", '%Y-%m-%d %H:%M:%S') <= tiempo_parseado <= datetime.strptime(
                f"{date} 15:59:59", '%Y-%m-%d %H:%M:%S')):
            calidad["lunch workers"] += 1
        elif (datetime.strptime(f"{date} 16:00:00", '%Y-%m-%d %H:%M:%S') <= tiempo_parseado <= datetime.strptime(
                f"{date} 19:59:59", '%Y-%m-%d %H:%M:%S')):
            calidad["sunset lovers"] += 1
        elif (datetime.strptime(f"{date} 20:00:00", '%Y-%m-%d %H:%M:%S') <= tiempo_parseado <= datetime.strptime(
                f"{date} 23:59:59", '%Y-%m-%d %H:%M:%S')):
            calidad["prime timers"] += 1

    return calidad



c = int(input())

commiting_times = []

for i in range(c):
    entry = input()
    commiting_times.append(entry)

result = horario(commiting_times)
impresora(result)



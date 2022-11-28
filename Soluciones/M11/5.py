from datetime import timedelta


def time_in(registers):
    time_in_barber = []
    for r in registers:
        date, time_go, time_back = r
        h0, m0, s0 = time_go.split(":")
        h1, m1, s1 = time_back.split(":")
        time_go = timedelta(hours=int(h0), minutes=int(m0), seconds=int(s0))
        time_back = timedelta(hours=int(h1), minutes=int(m1), seconds=int(s1))
        time_left = time_back - time_go

        time_in_barber.append(time_left)

    prom = sum(time_in_barber, start=timedelta()) / len(time_in_barber)
    h, m, s = prom.seconds // 3600, prom.seconds // 60 % 60, prom.seconds % 60

    print(f"{h} horas, {m} minutos, {s} segundos")



c = int(input())
registers = []

for i in range(c):
    entry = input()
    date, place, time_go, time_back = entry.split(", ")

    if place == "barberia":
        registers.append([date, time_go, time_back])

time_in(registers)



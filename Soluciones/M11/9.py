#Casi

"""
3
26/03/1879
16/06/1723
14/06/1825

"""
from calendar import Calendar
from datetime import datetime


def imprimir_cal(date):
    dias = ["lun", "mar", "mie", "jue", "vie", "sab", "dom"]
    mes = date.month
    año = date.year
    c = Calendar(firstweekday=0)
    arreglo_cal = c.monthdayscalendar(year=año, month=mes)
    arreglo_cal = list(map(lambda x: list(map(lambda y: y if y != 0 else "", x)), arreglo_cal))
    arreglo_cal.insert(0, dias)
    print("\n".join(map(lambda x: "\t".join(map(str, x)), arreglo_cal)))



c = int(input())
for i in range(c):
    d = input()
    date = datetime.strptime(d, "%d/%m/%Y")
    imprimir_cal(date)




"""horas = int(input())

minutos = int(input()) 

periodo = input()


if(periodo == 'pm'):
    if(horas != 12 and minutos != 0):
        tiempo = (12 * 60 + ((horas * 60) + minutos)) - 12 *60
        print(f"faltan {tiempo} para las 12a")
    else:
        tiempo = 12 * 60
        print(f"faltan {tiempo} para las 12a")

elif(periodo == "am"):
    if(horas == 12 or minutos != 0):
        tiempo = (24 * 60 + ((horas * 60) + minutos)) - 12 *60
        print(f"faltan {tiempo} para las 12b")
    else:
        tiempo = 24 * 60
        print(f"faltan {tiempo} para las 12b")
"""

horas = int(input())
minutos = int(input())
periodo = input()
if periodo =='pm':
    if horas==12:
        print('Faltan',(720 - minutos),'para las 12')
    else:
        print('Faltan',(720-((horas*60) + minutos)),'para las 12')

else:
    if horas==12:
        print('Faltan',((24 * 60) - minutos),'para las 12')
    else:
        print('Faltan',((24 * 60) - ((horas*60)+ minutos)),'para las 12')

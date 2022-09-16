horas = int(input())
minutos = int(input())
if minutos == 0 and horas!=12:
  horas = 12 - horas
elif minutos ==0 and horas==12:
  horas = 12
elif minutos !=0 and horas==12:
  horas= 11
  minutos = 60 - minutos
elif minutos!= 0 and horas != 11:
  horas = (12 - horas) - 1
  minutos = 60 - minutos
elif minutos != 0:
  horas = 12
  minutos = 60 - minutos
print(f"{horas}:{minutos}")
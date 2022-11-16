def promedio(lista_):
  lista_talleres = [9, 11, 12, 8, 12,9,11,8,11,10,9,10]
  cal_taller = 0
  cal_total = 0

  for i in lista_[1:]:
    for j in lista_talleres: 
      cal_taller += round(((int(i) / j)),1)
      cal_total += cal_taller * 5
      break


  promedio_total = cal_total/120
  return round(promedio_total, 1)

  
n = int(input())
lista_estudiantes = []

for i in range(n):
  estudiante = input().split(", ")
  ccyNota = [estudiante[0], promedio(estudiante)]
  lista_estudiantes.append(ccyNota)

lista_estudiantes.sort()

for i in lista_estudiantes:
  print(*i)
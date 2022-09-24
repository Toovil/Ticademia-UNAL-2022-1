cant = int(input()) # es la cantidad de lotes que desea Fernanda
Alado = float(input()) # longitud (en metros) de uno de los lados del lote más pequeño,
incr = float(input()) # incremento de la longitud de cada lado entre un lote y otro
acum = 0

for i in range(1,cant+1):
  acum += Alado ** 2
  Alado += incr
  
print(f'El area total es de {acum} metros cuadrados')
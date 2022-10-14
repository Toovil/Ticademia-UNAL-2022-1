# C es la velocidad de la luz en el vacío(299792458 metros/segundo)
# V es la velocidad del observador
from math import sqrt
lista = []
resultado = []
cadena = ''
c = 299792458
n = int(input())

for i in range(n):
    v = (float(input())) / 3.6
    lista.append(v)

def lorentz(lista):
    for j in lista:
       lorent = 1 / sqrt(1 - (j)**2/(c)**2)
       resultado.append(lorent)
    
    cadena = "".join(resultado)
    return cadena

print(lorentz(lista))
"""
r = radio
h = altura del cilindro
v = velocidad qué se vasea por minuto
m = minutos

¿Cuál será su volumen después de m minutos?

"""

import math

r = float(input())
h = float(input()) 
v = float(input()) 
m = float(input())

cilindro = (math.pi * r ** 2) *h - (v*m)

redondeado = round(cilindro,3)

a = max(0, redondeado)
print(a)

"""
Supongamos que nos contratan para diseñar el software de un cajero automático. Lo
primero que tenemos que hacer es que, dada una cantidad de dinero que quiere retirar
el usuario, la cual siempre será múltiplo de mil y no mayor a un millón, se debe determinar
la mínima cantidad de billetes en la que se le entregará esa cantidad. Para esto debemos
tener en cuenta que las denominaciones disponibles de los billetes son $1000, $2000,
$5000, $10000, $20000, y $50000.

Así por ejemplo, si el cliente va a retirar $188000, la mínima cantidad de billetes será:
3 de $50000
1 de $20000
1 de $10000
1 de $5000
1 de $2000
1 de $1000

!Entrada
La entrada contiene una única línea con un valor entero que corresponde a la cantidad a
retirar.

!Salida
La equivalencia en billetes correspondiente, de a uno por línea como se mostró
anteriormente y sin mostrar valores nulos para la cantidad de billetes de una determinada
denominación.

"""

money = int(input())

while money % 50000 == 0:
    count50k =+ 1

count50k = 0
count20k = 0
count10k = 0
count5k = 0
count2k = 0


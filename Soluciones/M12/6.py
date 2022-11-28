def mindhunter(x):
    valor=(x[1]-x[0]).days
    for i in range(1,len(x)):
        if (x[i]-x[i-1]).days!=valor:
            return False
    return True    
from datetime import datetime
n=int(input())
ajiaco=[]
for i in range(n):
    asesino=input()
    asesino=asesino.split(', ')
    d=int(asesino[1])
    fecha=[]
    for j in range(d):
        dia=input()
        dia=datetime.strptime(dia,'%Y-%m-%d')
        fecha.append(dia)
    if mindhunter(fecha):
        dif=fecha[1]-fecha[0]
        premonicion=fecha[-1]+dif
        prem=datetime.strftime(premonicion,'%Y-%m-%d')
        ajiaco.append(str(str(asesino[0])+' ataca cada '+str(dif.days)+' dias y volvera a hacerlo en '+str(prem)))
    else:
        ajiaco.append(str(str(asesino[0])+' no es asesino(a) serial periodico'))
for i in ajiaco:
    print(i)
    print()  
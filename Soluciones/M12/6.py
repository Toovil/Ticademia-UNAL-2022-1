from datetime import datetime

def hunter_(x):
    value=(x[1]-x[0]).days
    for i in range(1,len(x)):
        if (x[i]-x[i-1]).days!=value:
            return False
    return True    

num=int(input())
g=[]
for i in range(num):
    killer=input()
    killer=killer.split(', ')
    d=int(killer[1])
    fecha=[]
    for j in range(d):
        day=input()
        day=datetime.strptime(day,'%Y-%m-%d')
        fecha.append(day)
    if hunter_(fecha):
        diferencia=fecha[1]-fecha[0]
        premonition=fecha[-1]+diferencia
        pre=datetime.strftime(premonition,'%Y-%m-%d')
        g.append(str(str(killer[0])+' ataca cada '+str(diferencia.days)+' dias y volvera a hacerlo en '+str(pre)))
    else:
        g.append(str(str(killer[0])+' no es asesino(a) serial periodico'))
for i in g:
    print(i)
    print()  
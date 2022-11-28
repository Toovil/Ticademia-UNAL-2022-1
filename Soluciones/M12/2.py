from datetime import datetime
from time import time


a=int(input())
b=[]
c=[]
d=datetime(1,1,1)-datetime(1,1,1)
for i in range(a):
    e=input()
    e=e.split(' ')
    f=e[0].split('-')
    h=e[1].split(':')
    g=datetime(int(f[0]),int(f[1]),int(f[2]),int(h[0]),int(h[1]),int(h[2]))
    b.append(g)
for i in range(len(b)-1):
    g=b[i+1]-b[i]
    d+=g
    print(g.days,'dias,',g.seconds//60//60,'horas,',g.seconds//60%60,'minutos,',g.seconds%60,'segundos')
print('\nPromedio:',(d/(len(b)-1)).days,'dias,',(d/(len(b)-1)).seconds//60//60,'horas,',(d/(len(b)-1)).seconds//60%60,'minutos,',(d/(len(b)-1)).seconds%60,'segundos')


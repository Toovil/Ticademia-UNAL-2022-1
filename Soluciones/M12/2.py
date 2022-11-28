from datetime import datetime
from time import time
p=int(input())
v=[]
j=[]
l=datetime(1,1,1)-datetime(1,1,1)
for i in range(p):
    k=input()
    k=k.split(' ')
    q=k[0].split('-')
    c=k[1].split(':')
    x=datetime(int(q[0]),int(q[1]),int(q[2]),int(c[0]),int(c[1]),int(c[2]))
    v.append(x)
for i in range(len(v)-1):
    g=v[i+1]-v[i]
    l+=g
    print(g.days,'dias,',g.seconds//60//60,'horas,',g.seconds//60%60,'minutos,',g.seconds%60,'segundos')
print('\nPromedio:',(l/(len(v)-1)).days,'dias,',(l/(len(v)-1)).seconds//60//60,'horas,',(l/(len(v)-1)).seconds//60%60,'minutos,',(l/(len(v)-1)).seconds%60,'segundos')


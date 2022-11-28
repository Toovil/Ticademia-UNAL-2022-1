def clorox(x):
    x=x.lower()
    x=x.lstrip('¿')
    x=x.lstrip('¡')
    x=x.rstrip('?')
    x=x.rstrip('!')
    x=x.rstrip(',')
    x=x.rstrip('.')
    x=x.rstrip(';')
    x=x.rstrip(':') 
    return x
a=open('discurso.txt','r')
dic={}
cuchao=[]
for i in a:
    y=i.split()
    l=[]
    for j in y:
        j=clorox(j)
        if len(j)>4:
            if not j in l:
                l.append(j)
    for k in l:            
        if k in dic:
            dic[k]+=1 
        else:    
            dic[k]=1
            cuchao.append(k)  
cuchao.sort()
for i in cuchao:
    print(i,dic[i])    
a.close()
def clorox(b):
    b=b.lower()
    b=b.lstrip('¿')
    b=b.lstrip('¡')
    b=b.rstrip('?')
    b=b.rstrip('!')
    b=b.rstrip(',')
    b=b.rstrip('.')
    b=b.rstrip(';')
    b=b.rstrip(':') 
    return b
a=open('discurso.txt','r')
dic_={}
cu_=[]
for i in a:
    y=i.split()
    l=[]
    for j in y:
        j=clorox(j)
        if len(j)>4:
            if not j in l:
                l.append(j)
    for k in l:            
        if k in dic_:
            dic_[k]+=1 
        else:    
            dic_[k]=1
            cu_.append(k)  
cu_.sort()
for i in cu_:
    print(i,dic_[i])    
a.close()
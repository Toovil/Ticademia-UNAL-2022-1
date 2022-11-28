A= input().split("x") #m*n
B=input().split("x") #r*p
m= int(A[0])
n= int(A[1])

r=int(B[0])
p=int(B[1])
if  n==r:
    A=[]                  #matriz 1
    for i in range(m):
      C=[]
      for j in range(n):
        C.append(int(input())) #componentes
      A.append(C)  
    #for k in range (m):
     #   print (A[k])
    #####
    
    #matriz 2
    B=[]
    for i in range(r):
      C=[]
      for j in range(p):
        C.append(int(input()))
      B.append(C)  
      
    #multiplicacion
    Q=[]
    for l in range(m):
        F=[]
        for s in range(p):
             v=0  
             for x in range(r):
                 v+=A[l][x]*B[x][s]
             F.append(v)    
        Q.append(F)
    
    lista =Q
    for e in lista:
        print(' '.join(map(str, e)))

else:
    print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")
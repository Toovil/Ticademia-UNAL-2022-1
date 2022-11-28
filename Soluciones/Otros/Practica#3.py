#Ejercicio de Willington
matriz_A = input().split("x")
 
matriz_B = input().split("x")

A=[]                  #matriz 1
for i in range(int(matriz_A[0])):
  C=[]
  for j in range(int(matriz_A[1])):
    C.append(int(input())) #componentes
  A.append(C)  


#matriz 2
B=[]
for i in range(int(matriz_B[0])):
  C=[]
  for j in range(int(matriz_B[1])):
    C.append(int(input()))
  B.append(C)  
#multiplicacion

Q=[]
string_multiplicacion = ""
for l in range(int(matriz_A[0])):
    F=[]
    for s in range(int(matriz_B[1])):
         v=0  
         for x in range(int(matriz_B[0])):
             v+=A[l][x]*B[x][s]
         F.append(v)
    Q.append(F)    

for i in Q:
    print(*i)
     
    


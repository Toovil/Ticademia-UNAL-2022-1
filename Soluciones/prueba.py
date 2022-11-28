
m=int(input())
n=int(input())
r=int(input())
p=int(input())

A=[]                  #matriz 1
for i in range(m):
  C=[]
  for j in range(n):
    C.append(float(input())) #componentes
  A.append(C)  
#for k in range (m):
 #   print (A[k])
#####

#matriz 2
B=[]
for i in range(r):
  C=[]
  for j in range(p):
    C.append(float(input()))
  B.append(C)  
#multiplicacion

Q=[]
string_multiplicacion = ""
for l in range(m):
    F=[]
    for s in range(p):
         v=0  
         for x in range(r):
             v+=A[l][x]*B[x][s]
         Q.append(v)    


string_matriz = ""
counter = 0
for x1 in range(len(Q)):
    counter += 1
    if counter != p and counter < p:
        string_matriz+= f"{str(Q[0])} {str(Q[x1 + 1])}"
    else:
        x1 = p
        string_matriz += f"\n{str(Q[x1])}"

print(string_matriz)

#print(matriz_string)   
#print(f"{''.join(str(Q[0:p]))}\n{''.join(str(Q[p:]))}")


"""def main():
    matriz_A = input().split("x")
    matriz_B = input().split("x")

    if matriz_A[1] != matriz_B[0]:
        print("Las columnas de la primera tabla deben ser iguales a las filas de la segunda tabla")
    else:
        int(matriz_A[1])"""
n=int(input())
cont=0
while cont<n:
    cont=cont+1
    caso=input()
    x=0
    f=1
    lista=[]
    suma=0
    while x<9:
        sudoku=input().split()
        linea=[int(u) for u in sudoku]
        sudoku=sum(linea)
        lista.append(linea)
        if sudoku!=45:
            f=0            
        x=x+1
    for i in range(len(lista)):
        suma=0
        for j in range(len(lista)):
            suma=suma+lista[j][i]  
        if suma!=45:
            f=0
    if f==0:
        print("No resuelto")
    if f==1:
        print("Resuelto")
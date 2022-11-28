iteraciones=[]
C = int(input())
for w in range(C):
    tamano = int(input())
    cubo = []
    for w in range(1,tamano+1):
        X = []
        for w in range(1,tamano+1):
            X.append(w)
        cubo.append(X)
    op = input().split()
    for inst in op:
        num = int(inst[1])-1
        if inst[0] == 'F':
            if inst[2] == '+':
                cubo[num].insert(0,cubo[num][-1])
                cubo[num].pop(-1)
            else:
                cubo[num].append(cubo[num][0])
                cubo[num].pop(0)
        else:
            for w in range(len(cubo)):
                if inst[2] == '+':
                    cubo[w].insert(num+1,cubo[w-1][num])
                else:
                    cubo[w-1].insert(num+1,cubo[w][num])
            for w in range(len(cubo)):
                cubo[w].pop(num)
    iteraciones.append(cubo)
for Cub in iteraciones:
    for w in range(len(Cub)):
        for y in range(len(Cub)):
            print(Cub[w][y],end='')
        print()
    print()

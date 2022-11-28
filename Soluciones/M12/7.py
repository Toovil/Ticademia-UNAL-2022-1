iteration=[]
A = int(input())
for w in range(A):
    size = int(input())
    cube = []
    for w in range(1,size+1):
        X = []
        for w in range(1,size+1):
            X.append(w)
        cube.append(X)
    up = input().split()
    for instante in up:
        num = int(instante[1])-1
        if instante[0] == 'F':
            if instante[2] == '+':
                cube[num].insert(0,cube[num][-1])
                cube[num].pop(-1)
            else:
                cube[num].append(cube[num][0])
                cube[num].pop(0)
        else:
            for w in range(len(cube)):
                if instante[2] == '+':
                    cube[w].insert(num+1,cube[w-1][num])
                else:
                    cube[w-1].insert(num+1,cube[w][num])
            for w in range(len(cube)):
                cube[w].pop(num)
    iteration.append(cube)
for Cub in iteration:
    for w in range(len(Cub)):
        for y in range(len(Cub)):
            print(Cub[w][y],end='')
        print()
    print()

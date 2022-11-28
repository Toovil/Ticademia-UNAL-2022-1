for i in range(int(input())):
    b = []
    _Superior = []
    _Inferior = []
    c = int(input())
    for j in range(c):
        a = input().split(' ')
        a = [int(float(x)) for x in a]
        b.append(a)
    for l in range(c):
        _Superior.append(b[l][l+1:])
        _Inferior.append(b[l][:l])
        sup_ = 0
        for h in _Superior:
            for g in h:
                if g != 0:
                    sup_ += 1
        inf_ = 0
        for h in _Inferior:
            for g in h:
                if g != 0:
                    inf_ += 1
    if sup_ == 0 and inf_ == 0:
        print('Diagonal')
    elif sup_ == 0:
        print('Triangular inferior')
    elif inf_ == 0:
        print('Triangular superior')
    else:
        print('Ni diagonal ni triangular')

A=open('cameos.txt', 'r')
B='saramago'
for renglon in A:
    a=renglon.lower()
    a=a.replace(',', '')
    a=a.replace('.', '')
    a=a.replace('\n', '')
    c=0
    t=0
    for letra in a:
        if B[c]==letra:
            c+=1
            if c==7:
                t+=1
                c*=0
    print(t)
A.close()
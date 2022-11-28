archivo =open('cameos.txt', 'r')
x='saramago'
for renglon in archivo:
    a=renglon.lower()
    a=a.replace(',', '')
    a=a.replace('.', '')
    a=a.replace('\n', '')
    j=0
    t=0
    for letra in a:
        if x[j]==letra:
            j+=1
            if j==7:
                t+=1
                j*=0
    print(t)
archivo.close()

archivo = open('matrix.txt','r')
preguntas = []

for renglon in archivo:
    renglon = renglon.rstrip('\n')
    renglon = renglon.split()
    
    if renglon[0] != 'Smith:':
        continue
    
    i = 0
    
    while i <len(renglon):        
        palabra = renglon[i]
        if palabra.startswith('?'):
            pre = ''
            ini = renglon.index(palabra)
            for p in renglon[ini:]:
                pre += p + ' '
                if p.endswith('?'):
                    fin = renglon.index(p)
                    break
            if pre not in preguntas: #pa que no se repitan
                preguntas.append(pre)
            del renglon[:fin]
        else :
            i = i+1
            
for i in preguntas:
    print(i.rstrip(' '))
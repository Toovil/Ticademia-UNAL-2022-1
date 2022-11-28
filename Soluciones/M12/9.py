archivo = open('M12/textos/matrix.txt','r')
questions = []

for renglon in archivo:
    renglon = renglon.rstrip('\n')
    renglon = renglon.split()
    
    if renglon[0] != 'Smith:':
        continue
    
    i = 0
    
    while i <len(renglon):        
        word = renglon[i]
        if word.startswith('?'):
            before = ''
            init = renglon.index(word)
            for p in renglon[init:]:
                before += p + ' '
                if p.endswith('?'):
                    end = renglon.index(p)
                    break
            if before not in questions: #pa que no se repitan
                questions.append(before)
            del renglon[:end]
        else :
            i = i+1
            
for i in questions:
    print(i.rstrip(' '))
C = int(input())
for i in range (C):
    n=input()
    entrada = n.replace(' ','').split(':')
    guia=[]
    eje = []
    eje[:] = entrada[1]
    guia[:]=entrada[0]
    
    if len(guia)==len(eje):
         for i in eje:
             if guia.count(i) != eje.count(i):
                 print('No es anagrama')
                 anagrama = False
                 break
             if i in entrada[0]:
                 anagrama = True
             else:
                 print('No es anagrama')
                 anagrama = False
                 break
         if anagrama == True:
             print('Es anagrama')
    else:
        print('No es anagrama')

n=int(input())
for i in range (n):
    saltos={}
    m=int(input())
    for i in range(m):
        universe=input()
        universe=universe.split(' ')
        saltos[universe[0]]=universe[1]
    universo='C-137'
    ct=1
    for k in range(m):
         universo=saltos[universo]
         if universo in saltos:
          if universo != 'C-137':
             ct+=1 
          else:
             break
         else:
             break
    if universo=='C-137':
       print('Pueden volver a C-137 en {} saltos'.format(ct))
    else:
        print('Deambulan por el multiverso')

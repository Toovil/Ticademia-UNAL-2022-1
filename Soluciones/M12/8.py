num=int(input())
for i in range (num):
    jumps={}
    n=int(input())
    for i in range(n):
        universo=input()
        universo=universo.split(' ')
        jumps[universo[0]]=universo[1]
    universo='C-137'
    kt=1
    for k in range(n):
         universo=jumps[universo]
         if universo in jumps:
          if universo != 'C-137':
             kt+=1 
          else:
             break
         else:
             break
    if universo=='C-137':
       print('Pueden volver a C-137 en {} saltos'.format(kt))
    else:
        print('Deambulan por el multiverso')

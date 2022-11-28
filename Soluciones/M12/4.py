for i in range(int(input())):
  P = []
  o_Superior = []
  r_Inferior = []
  T = int(input())
  for j in range(T):
    a = input().split(' ')
    a = [ int(float(x)) for x in a]
    P.append(a)
  for l in range(T):
    o_Superior.append(P[l][l+1:])
    r_Inferior.append(P[l][:l])
    i_Sup = 0
    for h in o_Superior:
      for g in h:
        if g != 0:
          i_Sup += 1
    l_Inf = 0      
    for h in r_Inferior:
      for g in h:
        if g != 0:
          l_Inf += 1
  if i_Sup == 0 and l_Inf == 0:
    print('Diagonal')
  elif i_Sup == 0:
    print('Triangular inferior')
  elif l_Inf == 0:
    print('Triangular superior')
  else:
    print('Ni diagonal ni triangular')
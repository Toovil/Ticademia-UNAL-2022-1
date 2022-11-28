#incompleto
a = int(input())  
p = int(input()) 
q = int(input())

for i in range(p, q , 1):
    change = a % i
    if(change != 0):
        print(f"{a} es polifactor entre {p} y {q}")
        continue
    else:

        print(f"{a} es polifactor entre {p} y {q}")
        continue



def rec(X):

    if X < 1:

        return 0

    return 4*X + rec(X-1)

 

print(rec(6)-5)

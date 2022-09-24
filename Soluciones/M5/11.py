a = int(input())  
p = int(input()) 
q = int(input())



for i in range(p, q , 1):
    change = a // i
    if(change % i == 0):
        if( i == q ):
            print(f"{a} es polifactor entre {p} y {q}")
            break
    else:
        print(f"{a} no es polifactor entre {p} y {q}")
        break


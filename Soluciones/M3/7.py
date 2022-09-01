v = int(input()) 
e = int(input())

cambio = e - v

if(cambio % 4 == 0):
    print(f"{cambio}")
elif(cambio % 10 == 0 or cambio % 15 == 0):
    print(f"{cambio}\ny te lo puedes quedar")

def circuito(pareja_cable):
    count_m = 0
    count_f = 0
    for cable in range(len(pareja_cable)):
        for extremo in pareja_cable[cable]:
            if extremo == "M":
                count_m += 1
            else:
                count_f +=1
    if count_m == count_f:
        return "Es posible hacer un unico circulo"
    else:
        return "No es posible"

num = int(input())

for i in range(num):
    list_pareja = input().split(" ")
    print(circuito(list_pareja))
def Armstrong(num):
    totalF = 0
    leng = len(num)
    for j in num:
        totalF += int(j)**len(num)
    if(totalF == int(num)):
        return("es Armstrong")
    return("no es Armstrong")

cantN = int(input())

for i in range(cantN):
    valor = input()
    print(f"{valor} {Armstrong(valor)}")



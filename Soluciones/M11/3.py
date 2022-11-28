from random import randint


def ganador(pc):
    lanzamiento = randint(1, 6) + randint(1, 6)
    if lanzamiento > pc:
        print("Gana el humano")
    elif pc > lanzamiento:
        print("Gana la plataforma")
    else:
        print("Empate")



c = int(input())

for i in range(c):
    entrada = input()
    numero = int(entrada.split(" ")[1])
    ganador(numero)



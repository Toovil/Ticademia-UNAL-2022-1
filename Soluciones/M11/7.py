from random import randint


def juzgado(humano, robot):
    restaultados = {
        "humano": 0,
        "robot": 0
    }
    for i in range(10):
        if humano[i] > robot[i]:
            restaultados["humano"] += 1
        elif humano[i] < robot[i]:
            restaultados["robot"] += 1

    return restaultados


def generar_cartas():
    cartas = []
    for i in range(10):
        cartas.append(randint(1, 13))
    return cartas


c = int(input())

for i in range(c):
    x = input()
    x = x.split(" ")[1:]
    x = list(map(lambda x: int(x), x))
    resta = juzgado(generar_cartas(), x)
    print(f"Puntos humano: {resta['humano']} Puntos plataforma: {resta['robot']}")





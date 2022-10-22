def card(v, p):
    nueva_carta = [v, p]
    return nueva_carta

cartas = []

a = int(input())

for i in range(a):
    counter = 0
    while counter < 5:
        x = int(input())
        y = input()
        cartas.append(card(x, y))
        counter += 1

    print('Evaluation unimplemented.')
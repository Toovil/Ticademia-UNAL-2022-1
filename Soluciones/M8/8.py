#NO ESTÁ LISTO
def cartas(valor, palo):
    carta = [valor, palo]
    return carta

def escalera_normal(lista_cartas):
    orden_cartas = [2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
    """for carta in lista_cartas:
        for cartas_ordenadas in range(orden_cartas):
            if carta[0] == 0:"""
    

def color():
    return

def escalera_color():
    return

def escalera_real():
    return

n = int(input())

list_cards = []

for i in range(n):
    for j in range(5):
        valor = int(input())
        palo = input()
        list_cards.append(cartas(valor, palo))

print(escalera_normal(list_cards))



"""
7
D
6
C
9
T
8
P
5
T
"""

"""
11
C
10
C
13
C
14
C
12
C
"""
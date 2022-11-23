#LISTO
def panvocalica(palabra):
    vocales = ["a", "e", "i", "o", "u"]
    lista_comprueba = []
    for i in vocales:
        for vocal in palabra:
            if vocal not in lista_comprueba:
                if i == vocal:
                    lista_comprueba.append(vocal)
    if len(lista_comprueba) == len(vocales):
        return "Panvocalica"
    else:
        return "No es panvocalica"


num = int(input())

for i in range(num):
    palabras = input()
    print(panvocalica(palabras))
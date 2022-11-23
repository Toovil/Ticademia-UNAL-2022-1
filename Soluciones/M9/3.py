#LISTO
def encontrar_procedencia(nombre):
    if nombre[-2:] == "ix":
        return "Galo"
    elif nombre[-2:] == "us":
        return "Romano"
    elif nombre[-2:] == "ic":
        return "Godo"
    elif nombre[-2:] == "as":
        return "Griego"
    elif nombre [-2:] == "af":
        return "Normando"
    elif nombre[-2:] == "is" or nombre[-2:] == "ax":
        return "Breton"
    elif nombre[-2:] == "ez":
        return "Hispano"
    elif nombre[-1:] == "a":
        return "Indio"
    else:
        return "Desconocido"
    



num = int(input())

for i in range(num):
    nombres = input()
    print(encontrar_procedencia(nombres))
    

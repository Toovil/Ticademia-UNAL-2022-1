def traductor(palabras, palabra_ewokes ):
    lista_ewokes = []
    lista_español = []
    for i in palabras:
        lista_ewokes.append(i)



    return None

def main():
    cantidad_palabras = int(input())
    lista_palabras_ewokes = []
    lista_palabras_espanol = []

    for i in range(cantidad_palabras):
        palabras = input().split(" ")
        lista_palabras_ewokes.append(palabras[0][0])
        continue
    
    cantidad_traducir = int(input())
    for j in range(cantidad_traducir) :
        palabra_ewokes = input()
        traductor(lista_palabras_ewokes, palabra_ewokes)

main()
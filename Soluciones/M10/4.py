def traductor(palabras_espanol, palabras_ewokes, a_traducir):
    for d in a_traducir:
        if d in palabras_ewokes:
            index = palabras_ewokes.index(d)
            print(f"{palabras_espanol[index]}", end=" ")
        else:
            print("palabra no encontrada")

def main():    
    cantidad_palabras = int(input())
    lista_palabras_ewokes = []
    lista_palabras_espanol = []

    for i in range(cantidad_palabras):
        palabras = input().split(" ")
        lista_palabras_ewokes.append(palabras[0])
        lista_palabras_espanol.append(palabras[1])
            
    cantidad_traducir = int(input())

    for j in range(cantidad_traducir):
        ewokes_traducir = input().split()
        traductor(lista_palabras_espanol, lista_palabras_ewokes, ewokes_traducir)

main()
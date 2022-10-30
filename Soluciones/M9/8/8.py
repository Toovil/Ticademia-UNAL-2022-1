archivo = open("Soluciones/M9/8/mensaje.txt", "r")
texto = ""
for renglon in archivo:
    print(texto.join(list(reversed(renglon))))

archivo.close()
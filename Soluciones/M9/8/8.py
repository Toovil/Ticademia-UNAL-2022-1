archivo = open("M9/8/mensaje.txt", "r")
texto = ""
for renglon in archivo:
    print(texto.join(list(reversed(renglon))).strip("\n"))
archivo.close()
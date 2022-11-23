#LISTO, RECUERDA QUITAR EL ("M9/8/mensaje.txt", "r") Y PONER ("mensaje.txt", "r")
archivo = open("M9/8/mensaje.txt", "r")
texto = ""
for renglon in archivo:
    print(texto.join(list(reversed(renglon))).strip("\n"))
archivo.close()
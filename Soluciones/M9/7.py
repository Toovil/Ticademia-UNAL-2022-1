def conversor(mensaje):
    mensaje = mensaje.split("_")
    for palabra in mensaje:
        palabra.capitalize()
    mensaje = "".join(mensaje)
    return mensaje

num = int(input())

for i in range(num):
    variable = input()
    print(conversor(variable))
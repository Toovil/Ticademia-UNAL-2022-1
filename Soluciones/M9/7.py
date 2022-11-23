#LISTO
def conversor(mensaje):
    camel_list = []
    mensaje = mensaje.split("_")
    for palabra in mensaje:
        camel_list.append(palabra.capitalize())
    mensaje = "".join(camel_list)
    return mensaje

num = int(input())

for i in range(num):
    variable = input()
    print(conversor(variable))
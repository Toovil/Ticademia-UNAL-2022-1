#LISTO
def mas_viejo(lista_):
    for i in (lista_):
        if min(lista_) == i:
            return "Mi cacharrito es el mas viejo de todos los autos ;D"
        else:
            return "Al menos otro auto es mas viejo que mi cacharrito :("

num = int(input())

for i in range(num):
    placa = input().split(" ")
    print(mas_viejo(placa))

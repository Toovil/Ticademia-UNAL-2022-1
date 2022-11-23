#NO ESTÁ LISTO
import functools
from math import factorial as factorial


def arrlist(int_):
    return [int(a) for a in str(int_)]


def is_fuerte(value):
    numarr = arrlist(value)
    factorial = []
    for num in numarr:
        factorial.append(factorial(num))

    total = functools.reduce(lambda a, b: a + b, factorial)

    if total == value:
        print(f'{value} es fuerte')
    else:
        print(f'{value} no es fuerte')


values = int(input())
for i in range(values):
    value = int(input())
    is_fuerte(value)

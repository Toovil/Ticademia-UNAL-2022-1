"""import functools
from math import factorial


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


def main():
    values = int(input())
    for i in range(values):
        value = int(input())
        is_fuerte(value)
if __name__ == '__main__':
    main()"""

def cuadrado(x):
    return x**2

n = 5
print(cuadrado(n))
#lISTO
from math import sqrt
def f(x):
    num = sqrt(2+5*x)
    return num

def g(x):
    num = (4 + x)**3
    return num

while True:
    x = int(input())
    if(x == 0):
        break
    if(x % 2 == 0):
        print(f(g(x)))
    else:
        print(g(f(x)))
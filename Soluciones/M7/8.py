from ast import parse
from math import sqrt

def P(x):
    return 2*x +1

def A(x):
    return 3**x

def N(x):
    return sqrt(5*x + 4)

n = int(input())

for i in range(n):
    nums = float(input())
    print(P(A(N(nums))))
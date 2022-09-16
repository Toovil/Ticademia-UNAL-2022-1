
a = float(input()) 
b = float(input()) 
c = float(input())

if((a < b and b < c) or (c < b and b < a)):
    print(f"{b} es la mediana")
elif((b < a and a < c) or (c < a and a < b)):
    print(f"{a} es la mediana")
else:
    print(f"{c} es la mediana")

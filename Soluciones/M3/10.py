c = int(input())
k = int(input())

percentage = ((k - c)/c) * 100

if k > c:
    gains = k - c
    print(f"Hubo una ganancia de $ {gains} correspondiente al {percentage} % del capital invertido") 
elif c > k: 
    lost = c - k
    print(f"Hubo una perdida de $ {lost} correspondiente al {percentage*-1} % del capital invertido") 
else:
    print("No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menos no de dinero")
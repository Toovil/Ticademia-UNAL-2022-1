c = int(input())
k = int(input())

percentage = ((k - c)/c) * 100

if k > c:
    gains = k - c
    print(f"hubo una ganacia de $ {str(gains)} correspondiente al {str(percentage)}% del capital invertido") 
elif c > k: 
    lost = c - k
    print(f"hubo una perdida de $ {str(lost)} correspondiente al {str(percentage)}% del capital invertido") 
else:
    print("No hubo ni ganancia ni perdida, la inversion fue un desperdicio de tiempo, pero al menosno de dinero ")
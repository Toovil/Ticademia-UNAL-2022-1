cargaT = float(input())
cantE = int(input())
count = 0

for i in range(cantE+1, 1, -1):
    pesoE = float(input())
    if(cargaT - pesoE >= 0):
        cargaT -= pesoE
        count += 1
        continue
    else:
        break

print(count)


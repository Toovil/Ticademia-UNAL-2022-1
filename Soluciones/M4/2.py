x = float(input())
y = float(input())

if(x == 0 and y == 0):
    print(f'La coordenada ({x}, {y}) corresponde al origen')
elif(y == 0 and x != 0):
    print(f"La coordenada ({x}, {y}) esta sobre el eje X")
elif(x==0 and y != 0):
    print(f"La coordenada ({x}, {y}) esta sobre el eje Y")
elif( x > 0 and y > 0 ):
    print(f"La coordenada ({x}, {y}) se encuentra en el cuadrante 1")
elif(x < 0 and y > 0):
    print(f"La coordenada ({x}, {y}) se encuentra en el cuadrante 2")
elif( x < 0 and y < 0 ):
    print(f"La coordenada ({x}, {y}) se encuentra en el cuadrante 3")
else:
    print(f"La coordenada ({x}, {y}) se encuentra en el cuadrante 4")



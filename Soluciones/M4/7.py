x = input()
y = input()

if( x == y ):
    print("empate")
elif(x == "piedra" and y == "tijera") or (y == "piedra" and x == ("tijera")):
    print("piedra vence tijera")
elif((x == ("tijera") and y == "papel") or (y == "tijera" and x == "papel")):
    print("tijera vence papel")
elif((x == "papel" and y == "piedra") or (y == "papel" and x == "piedra" )):
    print("papel vence piedra")
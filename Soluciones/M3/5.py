calle = int(input())
num_casa = int(input())

if((calle % 13 == 0 or calle % 24 == 0) or (num_casa % 13 == 0 or num_casa % 23 == 0)):
    print(f"La direccion calle {calle} # {num_casa} esta prohibida ")
else:
    print(f"La direccion calle {calle} # {num_casa} no esta prohibida ")

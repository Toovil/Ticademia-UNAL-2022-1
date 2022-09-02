num = int(input())

if(num % 3 == 0 and num != 3):
    print(f'El numero {num} es multiplo de 3. Y el numero 3 es el mejor')
elif(num % 3 != 0):
    if((num + 1)%3 == 0):
        print(f'El numero {num} no es multiplo de 3, pero si le sumas 1 el resultado si lo es. Y el numero 3 es el mejor')
    elif((num - 1)%3 == 0):
        print(f'El numero {num} no es multiplo de 3, pero si le restas 1 el resultado si lo es. Y el numero 3 es el mejor')
elif(num == 3):
    print('El numero 3 es el mejor')
def ganador(persona):
    
    return None

num_personas = int(input())
lista_personas = []
numero_ventas = []
acum = 0

for i in range(num_personas):
    alias_personas = input().split(":") #Separa el vendedor de sus ventas si encuentra un :
    if alias_personas.count(i) > 1:
        print(alias_personas[0])
    """for j in alias_personas:                        #recorre la lista de tal forma que si el nombre de la persona ya se encuentra
        if alias_personas.count(j) > 1:"""
            

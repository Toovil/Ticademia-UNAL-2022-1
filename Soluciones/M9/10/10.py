a=open("conversaciones.txt","r")
#Estas variables pueden ir adentro del ciclo, así no será necesario renombrarlas abajo nuevamente.
OP=0 #Casos opositivos por renglón
CA=0 #Casos causativos por renglón
for i in a:
    I=i.lower() #Cada renglón lo vuelvo todo en minúsculas, así me será más sencillo y evitar errores al comparar texto
    if "sin embargo" in I:
        OP+=I.count("sin embargo") #Cuántas veces está ese Opositivo en el renglón. Así si es que aparece más de una vez no los cuento por separado
    if "no obstante" in I:
        OP+=I.count("no obstante")
    if "ahora bien" in I:
        OP+=I.count("ahora bien")
    if "aun asi" in I:
        OP+=I.count("aun asi")
    if "por tanto" in I:
        CA+=I.count("por tanto") #Cuántas veces está ese Causativo en el renglón. Así si es que aparece más de una vez no los cuento por separado
    if "dado que" in I:
        CA+=I.count("dado que")
    if "por consiguiente" in I:
        CA+=I.count("por consiguiente")
    if "asi pues" in I:
        CA+=I.count("asi pues")
    if "por ende" in I:
        CA+=I.count("por ende")
    print(f"Opositivos {OP} Causativos {CA}")
    #Reinicio los valores porque los necesito por cada renglón, no que se acumulen con los del renglón anterior
    OP=0
    CA=0
a.close()
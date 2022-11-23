#LISTO, RECUERDA CAMBIAR LO QUE TE HE DICHO
a=open("M9/10/conversaciones.txt","r")
OP=0 
CA=0 
for i in a:
    I=i.lower() 
    if "sin embargo" in I:
        OP+=I.count("sin embargo")
    if "no obstante" in I:
        OP+=I.count("no obstante")
    if "ahora bien" in I:
        OP+=I.count("ahora bien")
    if "aun asi" in I:
        OP+=I.count("aun asi")
    if "por tanto" in I:
        CA+=I.count("por tanto") 
    if "dado que" in I:
        CA+=I.count("dado que")
    if "por consiguiente" in I:
        CA+=I.count("por consiguiente")
    if "asi pues" in I:
        CA+=I.count("asi pues")
    if "por ende" in I:
        CA+=I.count("por ende")
    print(f"Opositivos {OP} Causativos {CA}")
    
    OP=0
    CA=0
a.close()
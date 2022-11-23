#LISTO, RECUERDA QUITAR EL ("M9/9/cadena.txt","r") Y PONER ("cadena.txt", "r")

a=open("M9/9/cadena.txt","r")
for i in a:
  Lista=i.split() 
  for j in range(len(Lista)-1): 
    if Lista[j][-2:]==Lista[j+1][:2] or Lista[j][-3:]==Lista[j+1][:3]: 
      if Lista[j+1] == Lista[-1]: 
       print("cadena completa")
       break 
    else:
       print("cadena rota")
       break
a.close()
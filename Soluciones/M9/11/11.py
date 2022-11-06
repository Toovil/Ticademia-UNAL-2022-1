a=open("M9/11/trifelios.txt","r")
for i in a:
    Lista=i.rstrip("\n") 
    Lista2=Lista.split("-") 
    C=0 
    Primera=Lista2[0] 
    P=len(Primera) 
    Segunda=Lista2[1] 
    for j in range(1,P): 
        PU=Primera[:j] 
        PD=Primera[(j-P):] 
        Nueva=PD+PU 
        if Nueva==Segunda: 
            C+=1
    if C>=1:
        print("Es trifelio")
    else:
        print("No es trifelio")
a.close()

#LISTO
def encuesta(info):
  for i in range(len(info)):
    info[i][1] = info[i][1].upper()

  info.sort(key=lambda x:int(x[0]), reverse = True)
  info.sort(key=lambda x:int(x[2]), reverse = True)

  for j in info:
    print(" ".join(j))

n = int(input())
info_personas = []
for i in range(n):
  persona = input().split(" ")
  if "positiva" in persona: 
    info_personas.append(persona[1:])
encuesta(info_personas) 
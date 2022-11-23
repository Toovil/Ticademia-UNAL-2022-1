#listo
def hyperpar(numtext):
    listnum.clear()
    countodd = 0
    counteven = 0
    for i in range(len(numtext)):
        listnum.append(numtext[i])
        

    for x in range(len(listnum)):
        if int(listnum[x]) % 2 == 0 or int(listnum[x]) == 0:
            countodd += 1
        else:
            counteven += 1

    if countodd == len(listnum):
        print("Hyperpar")
    else:
        print("No es hyperpar")

listnum = []
nums = []

while True:
    numtext = input()
    if int(numtext) == -1:
        break
    hyperpar(numtext)

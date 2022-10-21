listnum = []
nums = []

def hyperpar(numtext):
    countodd = 0
    counteven = 0
    for i in numtext:
        listnum.append(int(i))

    print(listnum)

    for x in listnum:
        if listnum[x] % 2 == 0:
            countodd += 1
        else:
            counteven += 1

    if countodd == len(listnum):
        print("Hyperpar")
    else:
        print("No es hyperpar")

while True:
    numtext = input()
    if int(numtext) == -1:
        break
    hyperpar(numtext)

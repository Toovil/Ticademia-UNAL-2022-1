def multidig(num):
    numlist = []
    count = 0
    for i in num:
        if i not in numlist or 1 <= i <= 5:
            numlist.append(i)
            count += 1
            if count == len(num):
                print("Multidigito")
        else:
            print("No es Multidigito")
            break
        
while True:
    n = input()
    if int(n) == 0:
        break
    multidig(n)


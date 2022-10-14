listnum = []
nums = []


def hyperpar(numtext):
    countodd = 0
    counteven = 0
    for i in numtext:
        listnum.append(i)

    for j in listnum:
        nums.append(int(j))

    for x in nums:
        if nums[x] % 2 == 0:
            countodd += 1
        else:
            counteven += 1

    if countodd == len(nums):
        print("Hyperpar")
    else:
        print("No es hyperpar")




while True:
    numtext = input()
    hyperpar(numtext)
    if int(numtext) == -1:
        break

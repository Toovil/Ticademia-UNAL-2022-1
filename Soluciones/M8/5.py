def order(lis):
    new_list = []

    for j in lis:
        if(lis[j] < lis[j-1]):
            new_list.append(j)

    return new_list

total_players = int(input())
each_list = []

for i in range(total_players):
    each_number = int(input())
    each_list.append(each_number)

order(each_list)
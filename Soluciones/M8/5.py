#NO ESTÁ LISTO
def order(lis):
    new_list = []

    for j in range(len(lis)):
        if(lis[j] < lis[j-1]):
            new_list.append(lis[j])

    return new_list

total_players = int(input())
each_list = []

for i in range(total_players):
    each_number = float(input())
    each_list.append(each_number)

print(order(each_list))
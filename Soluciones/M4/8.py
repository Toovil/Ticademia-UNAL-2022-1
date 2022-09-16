money = int(input())

if (money >= 50000):
    count50k = money // 50000
    money -= 50000 * count50k
    print(f'{count50k} de $50000')
if (money >= 20000):
    count20k = money // 20000
    money -= 20000 * count20k
    print(f'{count20k} de $20000')
if (money >= 10000):
    count10k = money // 10000
    money -= 10000 * count10k
    print(f'{count10k} de $10000')
if (money >= 5000):
    count5k = money // 5000
    money -= 5000 * count5k
    print(f'{count5k} de $5000')
if (money >= 2000):
    count2k = money // 2000
    money -= 2000 * count2k
    print(f'{count2k} de $2000')
if (money >= 1000):
    count1k = money // 1000
    money -= 1000 * count1k
    print(f'{count1k} de $1000')
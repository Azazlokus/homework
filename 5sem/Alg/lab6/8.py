bank = {
    1: 10,
    3: 5,
    4: 4,
    10: 10,
    50: 3,
    100: 4,
}
coins = [1, 3, 4, 10, 50, 100]

clients_num = int(input("Кол-во клиентов: "))

for c in range(clients_num):
    print("Клиент", c+1)
    sum = int(input("Сумма: "))
    lookup = [float("inf")] * (sum+1)
    lookup[0] = 0
    for m in range(1, sum+1):
        for i in range(len(coins)):
            if m >= coins[i] and lookup[m-coins[i]] + 1 < lookup[m]:
                lookup[m] = lookup[m-coins[i]] + 1

    ans = {}
    while (sum > 0):
        for i in range(len(coins)):
            if lookup[sum-coins[i]] == lookup[sum] - 1:
                sum -= coins[i]
                if coins[i] in ans:
                    ans[coins[i]] += 1
                else:
                    ans[coins[i]] = 1
                break

    ans_keys = list(ans.keys())
    bank_c = bank.copy()

    status = True
    for coin in ans_keys:
        bank_c[coin] -= ans[coin]
        if bank_c[coin] < 0:
            status = False
            break
    if status:
        bank = bank_c
        sorted_tuple = sorted(ans.items(), key=lambda x: -x[0])
        print("Выдача: ", dict(sorted_tuple))
        print("Банк:", bank)
    else:
        print("Сумму выдать невозможно")

coins = [1, 3, 4, 10, 50, 100]
n = int(input("Сумма: "))

ans = {}
coins_r = reversed(coins)
for coin in coins_r:
    count = n // coin
    if count > 0:
        ans[coin] = count
    n = n % coin
print(ans)


# 66

import timeit


def find_coins_greedy(req):
    coins = [50, 25, 10, 5, 2, 1]
    payout = {}
    while req:
        for coin in coins:
            greed = req // coin
            if greed >= 1:
                payout[coin] = greed
                req -= greed * coin
    return payout


def find_min_coins(req):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (req + 1)
    dp[0] = 0
    coin_used = [0] * (req + 1)

    for coin in coins:
        for x in range(coin, req + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                coin_used[x] = coin

    payout = {}
    while req > 0:
        coin = coin_used[req]
        if coin in payout:
            payout[coin] += 1
        else:
            payout[coin] = 1
        req -= coin
    return payout


print(timeit.timeit(lambda: find_coins_greedy(143), number=1000))
print(timeit.timeit(lambda: find_min_coins(143), number=1000))

def dpMakeChange(coinValueList, change):
    minCoin_list = [0 for i in range(change + 1)]
    coinUsed_list = [[] for i in range(change + 1)]
    for cents in range(change + 1):
        minCoin = cents
        coinUsed = []
        for coin in [coin for coin in coinValueList if coin <= cents]:
            temp = minCoin_list[cents - coin] + 1
            if temp <= minCoin:
                minCoin = temp
                coinUsed = coinUsed_list[cents - coin] + [coin]
        minCoin_list[cents] = minCoin
        coinUsed_list[cents] = coinUsed
    return minCoin_list[change], coinUsed_list[change]

coinValueList = [1, 2, 5, 10, 25, 21]
print dpMakeChange(coinValueList, 63)

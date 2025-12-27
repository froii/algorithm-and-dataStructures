

coins = [50, 25, 10, 5, 2, 1]


def find_min_coins(amount: int) -> dict:
    result = {}

    dpList = [float('inf')] * (amount + 1)
    dpList[0] = 0
    parent = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if dpList[i - coin] + 1 < dpList[i]:
                    dpList[i] = dpList[i - coin] + 1
                    parent[i] = coin

    current = amount
    while current > 0:
        coin = parent[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


print('dp solution:', find_min_coins(113))
# {50: 2, 10: 1, 2: 1, 1: 1}

print('dp solution:', find_min_coins(173))
# {50: 3, 10: 2, 2: 1, 1: 1}


print('dp solution:', find_min_coins(943))
# {50: 18, 25: 1, 10: 1, 5: 1, 2: 1, 1: 1}

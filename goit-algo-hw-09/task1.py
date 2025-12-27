coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict:
    result = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result

print('greedy solution:', find_coins_greedy(113))
# {50: 2, 10: 1, 2: 1, 1: 1}

print('greedy solution:', find_coins_greedy(173))
# {50: 3, 10: 2, 2: 1, 1: 1}


print('greedy solution:', find_coins_greedy(943))
# {50: 18, 25: 1, 10: 1, 5: 1, 2: 1, 1: 1}

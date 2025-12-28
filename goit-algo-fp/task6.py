items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    efficiency = {}
    for name, data in items.items():
        efficiency[name] = data["calories"] / data["cost"]

    sorted_items = sorted(efficiency, key=lambda x: efficiency[x], reverse=True)

    selected = []
    total = 0
    for name in sorted_items:
        if total + items[name]["cost"] <= budget:
            selected.append(name)
            total += items[name]["cost"]
    return selected


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i, name in enumerate(names, 1):
        cost, cal = items[name]["cost"], items[name]["calories"]
        dp[i] = dp[i - 1][:]
        for w in range(cost, budget + 1):
            dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + cal)

    selected = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(names[i - 1])
            w -= items[names[i - 1]]["cost"]
    return selected


budget = 100
print("Жадібний:", greedy_algorithm(items, budget))
print("DP:", dynamic_programming(items, budget))
# дані просто не підготовлені для жадібного алгоритму, для точності для хаотичних даних нема сенсу його використовувати
# хоча в цьому випадку він кращий - хтось недоїдатиме 

# good examples in links below
# https://networkx.org/documentation/stable/auto_examples/index.html
# https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

import networkx as nx

metro = nx.Graph()

red_line = ["Академмістечко", "Святошин", "Берестейська", "Університет", "Театральна", "Хрещатик", "Дніпро"]
blue_line = ["Героїв Дніпра", "Оболонь", "Контрактова площа", "Майдан Незалежності", "Площа Льва Толстого", "Либідська"]
green_line = ["Сирець", "Лук'янівська", "Золоті ворота", "Палац спорту", "Печерська", "Осокорки"]

for i in range(len(red_line) - 1):
    metro.add_edge(red_line[i], red_line[i + 1], line="M1", color="red")

for i in range(len(blue_line) - 1):
    metro.add_edge(blue_line[i], blue_line[i + 1], line="M2", color="blue")

for i in range(len(green_line) - 1):
    metro.add_edge(green_line[i], green_line[i + 1], line="M3", color="green")

transfers = [
    ("Театральна", "Золоті ворота"),
    ("Хрещатик", "Майдан Незалежності"),
    ("Площа Льва Толстого", "Палац спорту")
]

for station1, station2 in transfers:
    metro.add_edge(station1, station2, line="transfer", color="gray")


print("=" * 80)
print("ПОРІВНЯННЯ АЛГОРИТМІВ DFS ТА BFS")
print("=" * 80)

test_routes = [
    ("Академмістечко", "Дніпро"),
    ("Героїв Дніпра", "Осокорки"),
    ("Сирець", "Либідська"),
    ("Академмістечко", "Либідська")
]

for start, goal in test_routes:
    print(f"\n{start} → {goal}")

    dfs_result = list(nx.dfs_preorder_nodes(metro, start))
    dfs_path = dfs_result[:dfs_result.index(goal) + 1] if goal in dfs_result else []

    bfs_result = nx.shortest_path(metro, start, goal)

    if dfs_path and bfs_result:
        print(f"DFS ({len(dfs_path) - 1}): {' → '.join(dfs_path)}")
        print(f"BFS ({len(bfs_result) - 1}): {' → '.join(bfs_result)}")

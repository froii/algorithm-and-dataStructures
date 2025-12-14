# https://networkx.org/documentation/stable/auto_examples/index.html
# https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

import networkx as nx

start_station = "Академмістечко"

def print_table(distances, visited):
    print("{:<30} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 50)

    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(int(distance))

        status = "Так" if vertex in visited else "Ні"
        print("{:<30} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    print_table(distances, visited)
    return distances


metro = nx.Graph()

red_line = ["Академмістечко", "Святошин", "Берестейська", "Університет", "Театральна", "Хрещатик", "Дніпро"]
blue_line = ["Героїв Дніпра", "Оболонь", "Контрактова площа", "Майдан Незалежності", "Площа Льва Толстого", "Либідська"]
green_line = ["Сирець", "Лук'янівська", "Золоті ворота", "Палац спорту", "Печерська", "Осокорки"]

weights_red = [3, 4, 3, 2, 2, 3]
weights_blue = [5, 3, 2, 3, 4]
weights_green = [4, 3, 2, 3, 3]

for i in range(len(red_line) - 1):
    metro.add_edge(red_line[i], red_line[i + 1], weight=weights_red[i])

for i in range(len(blue_line) - 1):
    metro.add_edge(blue_line[i], blue_line[i + 1], weight=weights_blue[i])

for i in range(len(green_line) - 1):
    metro.add_edge(green_line[i], green_line[i + 1], weight=weights_green[i])

transfers = [
    ("Театральна", "Золоті ворота", 2),
    ("Хрещатик", "Майдан Незалежності", 3),
    ("Площа Льва Толстого", "Палац спорту", 2)
]

for station1, station2, weight in transfers:
    metro.add_edge(station1, station2, weight=weight)

graph = {}
for node in metro.nodes():
    graph[node] = {}
    for neighbor in metro.neighbors(node):
        graph[node][neighbor] = metro[node][neighbor]['weight']

print("=" * 80)
print("АЛГОРИТМ ДЕЙКСТРИ - ВЛАСНА РЕАЛІЗАЦІЯ")
print("=" * 80)
print(f"\nПочаткова станція: {start_station}\n")

dijkstra(graph, start_station)


print("\n" + "=" * 80)
print("АЛГОРИТМ ДЕЙКСТРИ - МЕТОД NETWORKX")
print("=" * 80)
distances_nx = nx.single_source_dijkstra_path_length(metro, start_station)
visited_nx = list(distances_nx.keys())
print(f"\nПочаткова станція: {start_station}\n")
print_table(distances_nx, visited_nx)

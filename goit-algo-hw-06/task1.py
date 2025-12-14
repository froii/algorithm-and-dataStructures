# good examples in links below
# https://networkx.org/documentation/stable/auto_examples/index.html
# https://www.cs.usfca.edu/~galles/visualization/Algorithms.html

import matplotlib.pyplot as plt
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

degrees = dict(metro.degree)

plt.figure(figsize=(10, 8))

pos = nx.spring_layout(metro, k=1, iterations=50, seed=42)

edges_by_line = {}
for u, v, data in metro.edges(data=True):
    line = data.get('line', 'unknown')
    if line not in edges_by_line:
        edges_by_line[line] = []
    edges_by_line[line].append((u, v))

line_colors = {'M1': '#DC143C', 'M2': '#0047AB', 'M3': '#228B22', 'transfer': '#808080'}
line_labels = {'M1': 'Червона', 'M2': 'Синя', 'M3': 'Зелена', 'transfer': 'Пересадка'}

for line, edges in edges_by_line.items():
    is_transfer = line == 'transfer'
    nx.draw_networkx_edges(
        metro, pos, edgelist=edges,
        edge_color=line_colors.get(line, 'black'),
        width=2 if is_transfer else 3,
        alpha=0.4 if is_transfer else 0.7,
        style='dashed' if is_transfer else 'solid',
        label=line_labels.get(line, line)
    )

node_sizes = [300 + degrees[node] * 200 for node in metro.nodes()]
node_colors = ['#FFD700' if degrees[node] > 2 else '#87CEEB' for node in metro.nodes()]

nx.draw_networkx_nodes(
    metro,
    pos,
    node_size=node_sizes,
    node_color=node_colors,
    edgecolors='black',
    linewidths=2,
    alpha=0.9
)

pos_labels = {node: (x, y - 0.08) for node, (x, y) in pos.items()}
nx.draw_networkx_labels(metro, pos_labels, font_size=8, font_weight='bold')

plt.title("Київське метро", fontsize=14, pad=14)
plt.legend(loc='upper left', fontsize=10)
plt.axis('off')
plt.tight_layout()
plt.savefig('kyiv_metro_graph.png', dpi=300, bbox_inches='tight')
print("Збережено: kyiv_metro_graph.png")
plt.show()

print("\n✓ Готово!")

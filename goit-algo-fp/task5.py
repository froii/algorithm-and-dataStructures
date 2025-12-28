# type: ignore
import heapq
import uuid
from collections import deque

import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            left_x = x - 1 / 2 ** layer
            pos[node.left.id] = (left_x, y - 1)
            left_x = add_edges(graph, node.left, pos, x=left_x, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            right_x = x + 1 / 2 ** layer
            pos[node.right.id] = (right_x, y - 1)
            right_x = add_edges(graph, node.right, pos, x=right_x, y=y - 1, layer=layer + 1)
    return graph


def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def dfs(root):
    stack, order = [root], []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs(root):
    queue, order = deque([root]), []
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return order


def visualize(root, traversal, title, rgb=(18, 96, 240)):
    order = traversal(root)
    n = max(len(order) - 1, 1)

    for i, node in enumerate(order):
        node.color = '#' + ''.join(f'{int(c + (255 - c) * i / n):02X}' for c in rgb)

    tree, pos = nx.DiGraph(), {root.id: (0, 0)}
    add_edges(tree, root, pos)

    nx.draw(tree, pos,
            labels={nd: tree.nodes[nd]['label'] for nd in tree},
            node_color=[tree.nodes[nd]['color'] for nd in tree],
            node_size=2500)
    plt.title(f"{title}: {' → '.join(str(nd.val) for nd in order)}")
    plt.show()


data = [100, 77, 66, 19, 36, 33, 17, 3, 25, 11, 1, 2, 3, 7]
heapq.heapify(data)

visualize(build_heap_tree(data), dfs, "DFS (стек)")
visualize(build_heap_tree(data), bfs, "BFS (черга)")

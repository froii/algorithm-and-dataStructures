import heapq

def dijkstra(graph: dict, start: str) -> dict:
    distances = {v: float('inf') for v in graph}
    distances[start] = 0

    heap = [(0, start)]
    visited = set()

    while heap:
        dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        for neighbor, weight in graph[current]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2), ('F', 6)],
    'E': [('F', 3)],
    'F': [('A', 13)] 
}

distances = dijkstra(graph, 'A')
print(distances)

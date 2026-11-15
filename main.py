import heapq


def prim(graph, start):
    if not graph:
        return [], 0, False
    if start not in graph:
        raise ValueError(f"Стартовая вершина {start!r} отсутствует в графе")

    visited = set()
    mst_edges = []
    total_weight = 0

    pq = [(0, None, start)]

    while pq:
        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)

        if u is not None:
            mst_edges.append((u, v, weight))
            total_weight += weight

        for neighbor, w in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(pq, (w, v, neighbor))

    connected = len(visited) == len(graph)
    return mst_edges, total_weight, connected


if __name__ == "__main__":
    graph = {
        'A': [('B', 6), ('C', 2)],
        'B': [('A', 6), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 10)],
        'D': [('C', 10), ('B', 5), ('E', 2)],
        'E': [('D', 2)],
    }

    edges, weight, connected = prim(graph, 'A')

    for u, v, w in edges:
        print(f"{u}{v} = {w}")
    print("Вес:", weight)
    print("Рёбер:", len(edges))
    print("Связный:", connected)

    disconnected = {
        'A': [('B', 1)],
        'B': [('A', 1)],
        'C': [('D', 1)],
        'D': [('C', 1)],
    }
    edges2, weight2, connected2 = prim(disconnected, 'A')
    print("Рёбер:", len(edges2), "Вес:", weight2, "Связный:", connected2)
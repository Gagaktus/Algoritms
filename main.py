import heapq


def topological_sort(graph):
    indegree = {v: 0 for v in graph}

    for u, neighbors in graph.items():
        for v in neighbors:
            if v not in indegree:
                indegree[v] = 0
            indegree[v] += 1

    zero_indegree = [v for v, deg in indegree.items() if deg == 0]
    heapq.heapify(zero_indegree)

    order = []

    while zero_indegree:
        u = heapq.heappop(zero_indegree)
        order.append(u)

        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(zero_indegree, v)

    if len(order) != len(indegree):
        raise ValueError("Граф содержит цикл: топологическая сортировка невозможна")

    return order


graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["E"],
    "E": ["F"],
    "F": [],
}

print(topological_sort(graph))

graph["F"].append("B")

try:
    print(topological_sort(graph))
except ValueError as e:
    print(e)
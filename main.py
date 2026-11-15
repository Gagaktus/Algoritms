from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'E'],
    'D': ['B'],
    'E': ['C'],
}

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(start)
    order.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

if __name__ == "__main__":
    print("BFS:", " → ".join(bfs(graph, 'A')))
    print("DFS:", " → ".join(dfs(graph, 'A')))
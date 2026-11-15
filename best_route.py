from collections import deque
from itertools import permutations


def bfs(start, adj):
    n = len(adj)
    dist = [-1] * n
    parent = [None] * n

    q = deque([start])
    dist[start] = 0

    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                parent[v] = u
                q.append(v)

    return dist, parent


def restore_path(parent, start, finish):
    if start == finish:
        return [start]

    if parent[finish] is None:
        return None

    path = []
    cur = finish

    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = parent[cur]

    if not path or path[-1] != start:
        return None

    return path[::-1]


def best_route(c, flights, home, tourists):
    adj = [[] for _ in range(c)]

    for u, v in flights:
        adj[u].append(v)

    sources = [home] + tourists
    data = {}

    for s in sources:
        data[s] = bfs(s, adj)

    best_flights = None
    best_order = None

    for perm in permutations(tourists):
        order = [home] + list(perm) + [home]

        total = 0
        ok = True

        for a, b in zip(order, order[1:]):
            d = data[a][0][b]
            if d == -1:
                ok = False
                break
            total += d

        if ok and (best_flights is None or total < best_flights):
            best_flights = total
            best_order = order

    if best_flights is None:
        return None, None

    route = []

    for a, b in zip(best_order, best_order[1:]):
        part = restore_path(data[a][1], a, b)

        if part is None:
            return None, None

        if not route:
            route.extend(part)
        else:
            route.extend(part[1:])

    return best_flights, route
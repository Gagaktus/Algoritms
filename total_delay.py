def total_delay(r, edges, entries):
    adj = [[] for _ in range(r)]
    total_len = 0

    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        total_len += w

    D = total_len
    INF = 10**18

    dist = [INF] * r
    buckets = [[] for _ in range(D + 1)]

    for s in entries:
        dist[s] = 0
        buckets[0].append(s)

    visited = [False] * r
    answer = 0

    for d in range(D + 1):
        for u in buckets[d]:
            if visited[u] or dist[u] != d:
                continue

            visited[u] = True
            answer += d

            for v, w in adj[u]:
                nd = d + w
                if nd < dist[v] and nd <= D:
                    dist[v] = nd
                    buckets[nd].append(v)

    return answer
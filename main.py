class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

        return True


def minimum_spanning_tree(graph):
    vertices = set()
    for u, v, w in graph:
        vertices.add(u)
        vertices.add(v)

    dsu = DSU(vertices)

    mst_edges = []
    total_weight = 0

    for u, v, w in sorted(graph, key=lambda edge: edge[2]):
        if dsu.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w

    return mst_edges, total_weight


graph = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("B", "E", 6),
]

mst, total_weight = minimum_spanning_tree(graph)

print("Выбранные рёбра:")
for u, v, w in mst:
    print(f"{u}{v}={w}")

print(f"\nОбщий вес дерева: {total_weight}")
print(f"Число рёбер: {len(mst)}")
print("Способ предотвращения циклов: DSU / Union-Find — ребро пропускается, "
      "если его вершины уже находятся в одной компоненте связности.")
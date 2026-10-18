from dataclasses import dataclass

@dataclass
class Equipment:
    id: int
    name: str
    room: str
    status: str
    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("id must be positive")

def dh(k, m): return k % m
def mh(k, m): return ((7 * k + 3) % 101) % m

def analyze(keys, m, hf):
    b = [[] for _ in range(m)]
    col = 0
    for k in keys:
        a = hf(k, m)
        if b[a]: col += 1
        b[a].append(k)
    occ = sum(1 for x in b if x)
    mx = max(len(x) for x in b)
    return [(k, hf(k, m)) for k in keys], occ, m - occ, col, mx, len(keys) / m


class Node:
    def __init__(self, e):
        self.data, self.next = e, None


class Chained:
    def __init__(self, m=13):
        self.m, self.n, self.b = m, 0, [None] * m

    def insert(self, e):
        i = e.id % self.m
        if self.b[i] is None:
            self.b[i] = Node(e); self.n += 1; return True
        cur = self.b[i]
        while True:
            if cur.data.id == e.id: return False
            if cur.next is None: break
            cur = cur.next
        cur.next = Node(e); self.n += 1; return True

    def search(self, k):
        cur, vis, cnt = self.b[k % self.m], [], 0
        while cur:
            cnt += 1; vis.append(cur.data.id)
            if cur.data.id == k: return cur.data, cnt, vis
            cur = cur.next
        return None, cnt, vis

    def update(self, k, room=None, status=None):
        r = self.search(k)[0]
        if r is None: return False
        if room: r.room = room
        if status: r.status = status
        return True

    def delete(self, k):
        i = k % self.m
        cur, prev = self.b[i], None
        while cur:
            if cur.data.id == k:
                if prev: prev.next = cur.next
                else: self.b[i] = cur.next
                self.n -= 1; return True
            prev, cur = cur, cur.next
        return False

    def contains(self, k): return self.search(k)[0] is not None
    def load(self): return self.n / self.m

    def display(self):
        for i, h in enumerate(self.b):
            ids = []
            while h: ids.append(str(h.data.id)); h = h.next
            print(f"{i}: " + " -> ".join(ids) if ids else f"{i}: —")

    def rehash(self, m):
        old = []
        for h in self.b:
            while h: old.append(h.data); h = h.next
        self.m, self.n, self.b = m, 0, [None] * m
        for e in old: self.insert(e)


EMPTY, DELETED = object(), object()

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

def next_prime(n):
    while not is_prime(n): n += 1
    return n


class Open:
    def __init__(self, m=13, strat="linear", auto=False):
        self.m, self.n, self.delc = m, 0, 0
        self.data = [EMPTY] * m
        self.strat, self.auto = strat, auto

    def probe(self, k, home, i):
        if self.strat == "linear":    return (home + i) % self.m
        if self.strat == "quadratic": return (home + i * i) % self.m
        return (home + i * (1 + k % (self.m - 1))) % self.m

    def _ins(self, e):
        home, pr, oc = e.id % self.m, 0, 0
        for i in range(self.m):
            idx = self.probe(e.id, home, i)
            c = self.data[idx]; pr += 1
            if c is EMPTY:
                self.data[idx] = e; self.n += 1; return True, pr, oc, idx
            if c is DELETED:
                self.data[idx] = e; self.n += 1; self.delc -= 1
                return True, pr, oc, idx
            oc += 1
            if c.id == e.id: return False, pr, oc, idx
        return False, pr, oc, -1

    def insert(self, e):
        if self.auto and (self.n + 1) / self.m > 0.70:
            self.rehash(next_prime(2 * self.m))
        return self._ins(e)

    def _find(self, k):
        home, vis = k % self.m, []
        for i in range(self.m):
            idx = self.probe(k, home, i)
            vis.append(idx)
            c = self.data[idx]
            if c is EMPTY: return -1, vis
            if c is DELETED: continue
            if c.id == k: return idx, vis
        return -1, vis

    def search(self, k):
        idx, vis = self._find(k)
        return (self.data[idx] if idx >= 0 else None), vis, len(vis)

    def update(self, k, room=None, status=None):
        idx, _ = self._find(k)
        if idx < 0: return False
        r = self.data[idx]
        if room: r.room = room
        if status: r.status = status
        return True

    def delete(self, k):
        idx, _ = self._find(k)
        if idx < 0: return False
        self.data[idx] = DELETED; self.n -= 1; self.delc += 1
        return True

    def contains(self, k): return self.search(k)[0] is not None
    def load(self): return self.n / self.m
    def used(self): return (self.n + self.delc) / self.m

    def display(self):
        for i, c in enumerate(self.data):
            if c is EMPTY: print(f"{i}: —")
            elif c is DELETED: print(f"{i}: DELETED")
            else: print(f"{i}: {c.id}")

    def rehash(self, m):
        old = [c for c in self.data if c is not EMPTY and c is not DELETED]
        self.m, self.n, self.delc = m, 0, 0
        self.data = [EMPTY] * m
        for e in old: self._ins(e)


def records():
    return [
        Equipment(26, "Проектор", "A-201", "Свободно"),
        Equipment(39, "3D-принтер", "A-305", "Обслуживание"),
        Equipment(52, "Осциллограф", "B-214", "Свободно"),
        Equipment(14, "Ноутбук", "A-108", "Выдано"),
        Equipment(27, "Маршрутизатор", "B-214", "Свободно"),
        Equipment(40, "Набор микроконтроллеров", "A-305", "Выдано"),
        Equipment(16, "Веб-камера", "A-108", "Свободно"),
        Equipment(29, "Графический планшет", "A-201", "Обслуживание"),
        Equipment(42, "Лазерный принтер", "A-108", "Свободно"),
    ]


def main():
    print("=== Этап 2 ===")
    ks = [r.id for r in records()]
    for hf, nm in [(dh, "division"), (mh, "mixed")]:
        a, o, e, c, mx, al = analyze(ks, 13, hf)
        print(nm, a)
        print(f"  occupied={o} empty={e} collisions={c} max={mx} alpha={al:.3f}")

    print("\n=== Этап 3 ===")
    ch = Chained(13)
    for r in records(): ch.insert(r)
    ch.display()
    print(f"load={ch.load():.3f}")
    r, c, v = ch.search(42); print(f"search 42: id={r.id} cmp={c} path={v}")
    r, c, v = ch.search(91); print(f"search 91: id=None cmp={c} path={v}")
    print("dup 27:", ch.insert(Equipment(27, "x", "x", "x")))
    ch.update(27, "B-310", "Выдано")
    ch.insert(Equipment(195, "Документ-камера", "B-210", "Свободно"))
    ch.delete(39)
    print("has 52:", ch.contains(52), "has 195:", ch.contains(195))
    ch.insert(Equipment(351, "VR-шлем", "B-212", "Свободно"))
    ids = []
    cur = ch.b[0]
    while cur: ids.append(cur.data.id); cur = cur.next
    print("bucket 0:", ids)

    print("\n=== Этап 5 ===")
    ts = {}
    for s in ["linear", "quadratic", "double"]:
        t = Open(13, s)
        oc = pr = 0
        for r in records():
            _, p, o, _ = t.insert(r); oc += o; pr += p
        ts[s] = t
        print(f"{s}: occupied={oc} probes={pr}")
        t.display()

    print("\n=== Этап 7 ===")
    for s, t in ts.items():
        r, v, p = t.search(42); print(f"{s} 42: path={v} probes={p}")
        r, v, p = t.search(91); print(f"{s} 91: path={v} probes={p}")

    print("\n=== Этап 8 ===")
    for s, t in ts.items():
        t.insert(Equipment(195, "Документ-камера", "B-210", "Свободно"))
        t.delete(39)
        r, v, p = t.search(195)
        print(f"{s} 195 after delete 39: path={v} probes={p}")
        t.insert(Equipment(351, "VR-шлем", "B-212", "Свободно"))
        t.display()

    print("\n=== Этап 9 ===")
    for s, t in ts.items():
        t.auto = True
        t.insert(Equipment(54, "Набор датчиков", "A-305", "Свободно"))
        print(f"{s}: m={t.m} n={t.n} deleted={t.delc} alpha={t.load():.3f}")
        t.display()

    print("\n=== Этап 10 ===")
    experiment()


def experiment():
    m = 101
    for fill in [0.25, 0.50, 0.70, 0.85]:
        n = int(m * fill)
        ks = [(i * 37 + 11) % 1009 + 1 for i in range(n)]
        miss = [2000 + i for i in range(50)]

        ch = Chained(m)
        c = ti = mi = 0
        for k in ks:
            i = k % m
            L = 0; h = ch.b[i]
            while h: L += 1; h = h.next
            if L: c += 1
            cmp = L + 1; ti += cmp; mi = max(mi, cmp)
            ch.insert(Equipment(k, "", "", ""))
        ok = sum(ch.search(k)[1] for k in ks)
        bad = sum(ch.search(k)[1] for k in miss)
        mc = 0
        for h in ch.b:
            L = 0
            while h: L += 1; h = h.next
            mc = max(mc, L)
        emp = sum(1 for h in ch.b if h is None)
        print(f"{fill:.2f} chain     col={c:3} avgI={ti/n:.2f} maxI={mi:3} "
              f"avgOK={ok/n:.2f} avgBAD={bad/50:.2f} maxChain={mc:2} empty={emp:3}")

        for s in ["linear", "quadratic", "double"]:
            t = Open(m, s)
            c = tp = mp = 0
            for k in ks:
                _, p, o, _ = t._ins(Equipment(k, "", "", ""))
                c += o; tp += p; mp = max(mp, p)
            ok = sum(t.search(k)[2] for k in ks)
            bad = sum(t.search(k)[2] for k in miss)
            mc = cur = emp = 0
            for cell in t.data:
                if cell is EMPTY: emp += 1; cur = 0
                else: cur += 1; mc = max(mc, cur)
            print(f"{fill:.2f} {s:<9} col={c:3} avgI={tp/n:.2f} maxI={mp:3} "
                  f"avgOK={ok/n:.2f} avgBAD={bad/50:.2f} maxChain={mc:2} empty={emp:3}")


if __name__ == "__main__":
    main()  
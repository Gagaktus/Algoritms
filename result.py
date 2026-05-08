import sys
from algorithms import bubble_sort, quick_sort
from data_generator import best_case, average_case, worst_case
from benchmark import measure

sys.setrecursionlimit(1_000_000)

sizes = [100, 1000, 5000]

cases = {
    "лучший (возрастающий)": best_case,
    "средний (случайный)":  average_case,
    "худший (убывающий)":   worst_case,
}

stats = []

print("=" * 70)
print("Сравнение пузырька и быстрой сортировки")
print("=" * 70)

for n in sizes:
    for name, gen in cases.items():
        arr = gen(n)
        print(f"\n>> n={n}, тип={name}")

        t_bubble = measure(bubble_sort, arr)
        print(f"   Bubble: {t_bubble:.6f} с")

        t_quick = measure(quick_sort, arr)
        print(f"   Quick:  {t_quick:.6f} с")

        stats.append({
            "n": n,
            "case": name,
            "bubble": t_bubble,
            "quick": t_quick,
        })

print("\n\n")
print("=" * 80)
print("РЕЗУЛЬТАТЫ")
print("=" * 80)
print(f"{'n':<10} {'Сценарий':<24} {'Bubble (сек)':<18} {'Quick (сек)':<18}")
print("-" * 80)

for s in stats:
    print(f"{s['n']:<10} {s['case']:<24} {s['bubble']:<18.6f} {s['quick']:<18.6f}")

print("=" * 80)

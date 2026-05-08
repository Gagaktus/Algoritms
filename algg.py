import time

def measure(sort_func, data, tries=3):
    best = float('inf')
    for _ in range(tries):
        copy_data = data.copy()
        start = time.perf_counter()
        sort_func(copy_data)
        end = time.perf_counter()
        t = end - start
        if t < best:
            best = t
    return best


if __name__ == "__main__":
    def dummy_sort(arr):
        arr.sort()
    
    test_arr = [3, 1, 4, 1, 5, 9, 2]
    t = measure(dummy_sort, test_arr)
    print(f"Лучшее время из 3 попыток: {t:.6f} сек")

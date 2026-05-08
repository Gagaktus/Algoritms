import time

def measure_time(sort_func, arr, trials=3):
    best_time = float('inf')
    for _ in range(trials):
        test_arr = arr.copy()
        start = time.perf_counter()
        sort_func(test_arr)
        end = time.perf_counter()
        elapsed = end - start
        if elapsed < best_time:
            best_time = elapsed
    return best_time

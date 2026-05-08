def bubble_sort(arr):
    n = len(arr)
    data = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

def quick_sort(arr):
    data = arr.copy()
    _quick_sort_inner(data, 0, len(data) - 1)
    return data

def _quick_sort_inner(arr, low, high):
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_inner(arr, low, pi - 1)
        _quick_sort_inner(arr, pi + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

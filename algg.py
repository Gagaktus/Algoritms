import random

def best_case(n):
    return list(range(n))

def worst_case(n):
    return list(range(n, 0, -1))

def average_case(n):
    a = list(range(n))
    random.shuffle(a)
    return a


if __name__ == "__main__":
    n = 10
    print(f"n = {n}")
    print("Лучший случай:", best_case(n))
    print("Худший случай:", worst_case(n))
    print("Средний случай:", average_case(n))

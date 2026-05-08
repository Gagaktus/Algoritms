from collections import deque

class Queue:
    def __init__(self):
        self._data = []
    
    def enqueue(self, value):
        self._data.append(value)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._data.pop(0)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def size(self):
        return len(self._data)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._data[0]


def counting_rhyme(step, kids):
    circle = deque(kids)

    while len(circle) > 1:
        for _ in range(step - 1):
            circle.append(circle.popleft())
      
        circle.popleft()

    return circle[0]


if __name__ == "__main__":
    print("Считалочка\n")

    step = 4
    kids = ["Петя", "Лена", "Гена", "Витя", "Саша"]

    print(f"Считаем до: {step}")
    print(f"Дети: {kids}")

    winner = counting_rhyme(step, kids)
    print(f"\nПобедитель: {winner}")

    assert winner == "Петя"
    print("Тест пройден\n")

    print("Дополнительные проверки\n")

    tests = [
        (3, ["Аня", "Боря", "Вера"], "Аня"),
        (2, ["X", "Y", "Z"], "Z"),
        (5, ["A", "B", "C", "D", "E", "F", "G"], "D"),
    ]

    for step, kids, expected in tests:
        result = counting_rhyme(step, kids)
        ok = "OK" if result == expected else "NAH"
        print(f"{ok}  шаг={step}, дети={kids}: {result} (ждали {expected})")

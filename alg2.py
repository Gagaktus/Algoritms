class Stack:
    def __init__(self):
        self._data = []
    
    def push(self, value):
        self._data.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self._data[-1]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def size(self):
        return len(self._data)

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


if __name__ == "__main__":
    print("=== Задача 2i: Стек ===\n")
    
    s = Stack()
    s.push('x')
    s.push('y')
    s.pop()
    s.push('z')
    top = s.peek()
    print(f"Результат s.peek(): {top}")
    assert top == 'z'
    print("Правильно: 'z'\n")
    
    print("=== Задача 2ii: Очередь ===\n")
    
    qq = Queue()
    qq.enqueue('hello')
    qq.enqueue('dog')
    qq.enqueue(3)
    qq.dequeue()
    
    print(f"Элементы в очереди: {qq._data}")
    print(f"Первый элемент: {qq.peek()}")
    assert qq._data == ['dog', 3]
    print("Правильно: ['dog', 3]")

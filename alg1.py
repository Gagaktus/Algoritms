class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self._size += 1
    
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1
    
    def remove(self):
        if self.head is None:
            raise IndexError("Нельзя удалить из пустого списка")
        
        val = self.head.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        
        self._size -= 1
        return val
    
    def delete(self):
        if self.head is None:
            raise IndexError("Нельзя удалить из пустого списка")
        
        val = self.tail.data
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            cur = self.head
            while cur.next != self.tail:
                cur = cur.next
            cur.next = None
            self.tail = cur
        
        self._size -= 1
        return val
   
    def iterate(self):
        if self.head is None:
            print("Список пуст")
            return
        
        cur = self.head
        elems = []
        while cur:
            elems.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(elems))

    def size(self):
        return self._size


if __name__ == "__main__":
    print("Проверка работы односвязного списка...\n")
    
    lst = LinkedList()
    
    print("1. Новый список:")
    print(f"   Длина: {lst.size()}")
    lst.iterate()
    assert lst.size() == 0
    
    print("\n2. Добавляем элементы:")
    lst.insert(10)
    lst.insert(20)
    lst.append(30)
    lst.append(40)
    print(f"   Длина: {lst.size()}")
    lst.iterate()
    assert lst.size() == 4
    
    print("\n3. Удаляем с головы:")
    x = lst.remove()
    print(f"   Удалено: {x}")
    print(f"   Длина: {lst.size()}")
    lst.iterate()
    assert x == 20
    assert lst.size() == 3
    
    print("\n4. Удаляем с хвоста:")
    x = lst.delete()
    print(f"   Удалено: {x}")
    print(f"   Длина: {lst.size()}")
    lst.iterate()
    assert x == 40
    assert lst.size() == 2
    
    print("\n5. Список из одного элемента:")
    single = LinkedList()
    single.append(100)
    print(f"   Длина: {single.size()}")
    single.iterate()
    assert single.size() == 1
    
    x = single.delete()
    print(f"   Удалён с хвоста: {x}")
    assert x == 100
    assert single.size() == 0
    single.iterate()
    
    print("\n6. Проверка исключений:")
    try:
        empty1 = LinkedList()
        empty1.remove()
        print("   Ошибка: исключение не выброшено!")
    except IndexError as e:
        print(f"   OK: {e}")
    
    try:
        empty2 = LinkedList()
        empty2.delete()
        print("   Ошибка: исключение не выброшено!")
    except IndexError as e:
        print(f"   OK: {e}")
    
    print("\n7. Несколько операций подряд:")
    lst2 = LinkedList()
    lst2.insert(1)
    lst2.append(2)
    lst2.insert(3)
    lst2.append(4)
    lst2.iterate()
    assert lst2.size() == 4
    
    assert lst2.remove() == 3
    assert lst2.delete() == 4
    assert lst2.remove() == 1
    assert lst2.delete() == 2
    assert lst2.size() == 0
    print("   Порядок операций правильный!")
    
    print("\nВсе тесты успешно завершены")

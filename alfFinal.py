from dataclasses import dataclass
from collections import deque


@dataclass
class Request:
    id: int
    title: str
    priority: int


class TreeNode:
    def __init__(self, request):
        self.request = request
        self.left = None
        self.right = None


def insert(root, request):
    if root is None:
        return TreeNode(request)

    if request.id < root.request.id:
        root.left = insert(root.left, request)
    elif request.id > root.request.id:
        root.right = insert(root.right, request)

    return root


def preorder(root):
    if root is None:
        return []
    return [root.request] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.request] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.request]


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.request)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def search(root, request_id):
    path = []
    current = root

    while current is not None:
        path.append(current.request.id)

        if request_id == current.request.id:
            return current.request, path
        elif request_id < current.request.id:
            current = current.left
        else:
            current = current.right

    return None, path


def find_min_node(node):
    while node.left is not None:
        node = node.left
    return node


def find_min(root):
    if root is None:
        return None
    return find_min_node(root).request


def find_max(root):
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right

    return current.request


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def get_depth(root, request_id):
    depth = 0
    current = root

    while current is not None:
        if request_id == current.request.id:
            return depth
        elif request_id < current.request.id:
            current = current.left
        else:
            current = current.right
        depth += 1

    return -1


def validate_bst(root):
    ids = [request.id for request in inorder(root)]

    for i in range(1, len(ids)):
        if ids[i] <= ids[i - 1]:
            return False

    return True


def delete(root, request_id):
    if root is None:
        return None

    if request_id < root.request.id:
        root.left = delete(root.left, request_id)
    elif request_id > root.request.id:
        root.right = delete(root.right, request_id)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # используем симметричного преемника
        successor = find_min_node(root.right)
        root.request = successor.request
        root.right = delete(root.right, successor.request.id)

    return root


def heap_key(request):
    return (request.priority, request.id)


def sift_down(data, heap_size, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and heap_key(data[left]) > heap_key(data[largest]):
        largest = left

    if right < heap_size and heap_key(data[right]) > heap_key(data[largest]):
        largest = right

    if largest != index:
        data[index], data[largest] = data[largest], data[index]
        sift_down(data, heap_size, largest)


def build_max_heap(data):
    for i in range(len(data) // 2 - 1, -1, -1):
        sift_down(data, len(data), i)


def is_max_heap(data):
    n = len(data)

    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap_key(data[i]) < heap_key(data[left]):
            return False
        if right < n and heap_key(data[i]) < heap_key(data[right]):
            return False

    return True


def heap_sort(data):
    build_max_heap(data)
    n = len(data)

    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        sift_down(data, i, 0)


def request_str(request):
    return f"{request.id}({request.priority})"


def print_requests(requests):
    print(", ".join(request_str(request) for request in requests))


def print_ids(requests):
    print(", ".join(str(request.id) for request in requests))


requests_data = [
    Request(50, "Ошибка оплаты", 9),
    Request(30, "Сброс пароля", 4),
    Request(70, "Интеграция API", 13),
    Request(20, "Изменение профиля", 2),
    Request(40, "Ошибка отчёта", 7),
    Request(60, "Настройка уведомлений", 11),
    Request(80, "Сбой сервера", 15),
    Request(10, "Удаление аккаунта", 1),
    Request(25, "Проблема входа", 3),
    Request(35, "Экспорт данных", 5),
    Request(45, "Возврат платежа", 8),
    Request(55, "Подключение тарифа", 10),
    Request(65, "Ошибка синхронизации", 12),
    Request(75, "Недоступна база данных", 14),
    Request(90, "Обновление реквизитов", 6),
]

root = None
for request in requests_data:
    root = insert(root, request)

print("Этап 1")
print_requests(level_order(root))
print()

print("Этап 2")
print("Прямой обход:")
print_ids(preorder(root))
print("Симметричный обход:")
print_ids(inorder(root))
print("Обратный обход:")
print_ids(postorder(root))
print("Уровневый обход:")
print_ids(level_order(root))
print()

print("Этап 3")
found, path = search(root, 65)
print("Поиск 65:", found, path)
found, path = search(root, 99)
print("Поиск 99:", found, path)
print("Количество узлов:", count_nodes(root))
print("Количество листьев:", count_leaves(root))
print("Высота:", height(root))
print("Минимальный ID:", find_min(root).id)
print("Максимальный ID:", find_max(root).id)
print("Глубина узла 65:", get_depth(root, 65))
found, path = search(root, 65)
print("Путь к узлу 65:", " -> ".join(str(x) for x in path))
print("validate_bst:", validate_bst(root))
print()

print("Этап 4")
root = insert(root, Request(37, "Утечка данных", 16))
print("Добавлена заявка 37")
print_ids(inorder(root))
print("Количество узлов:", count_nodes(root))
print("Высота:", height(root))
print("validate_bst:", validate_bst(root))
print()

root = insert(root, Request(50, "Ошибка оплаты", 9))
print("Попытка добавить дубликат 50")
print_ids(inorder(root))
print("Количество узлов:", count_nodes(root))
print("Высота:", height(root))
print("validate_bst:", validate_bst(root))
print()

root = delete(root, 10)
print("Удалён узел 10")
print_ids(inorder(root))
print("Количество узлов:", count_nodes(root))
print("Высота:", height(root))
print("validate_bst:", validate_bst(root))
print()

root = delete(root, 35)
print("Удалён узел 35")
print_ids(inorder(root))
print("Количество узлов:", count_nodes(root))
print("Высота:", height(root))
print("validate_bst:", validate_bst(root))
print()

root = delete(root, 70)
print("Удалён узел 70")
print_ids(inorder(root))
print("Количество узлов:", count_nodes(root))
print("Высота:", height(root))
print("validate_bst:", validate_bst(root))
print()

root = delete(root, 999)
print("Попытка удалить узел 999")
print_ids(inorder(root))
print("Количество узлов:", count_nodes(root))
print("Высота:", height(root))
print("validate_bst:", validate_bst(root))
print()

print("Этап 5") 
remaining = inorder(root)
print("Исходный массив:")
print_requests(remaining)

heap_data = remaining[:]
build_max_heap(heap_data)

print("Массив после построения кучи:")
print_requests(heap_data)
print("Элементы кучи по уровням:")
print_requests(heap_data)
print("is_max_heap:", is_max_heap(heap_data))
print()

print("Этап 6")
heap_sort(heap_data)
print("Отсортированный массив:")
print_requests(heap_data)

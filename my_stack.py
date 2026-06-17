from typing import Any


class Queue:
    """Очередь (FIFO) на основе списка Python.

    Принцип работы: First In, First Out — первым вошёл, первым вышел.

    Сложность операций:
        enqueue : O(1)
        dequeue : O(n) — из-за сдвига элементов при list.pop(0)
        peek    : O(1)
        is_empty: O(1)
        size    : O(1)
    """

    def __init__(self) -> None:
        self._items: list[Any] = []

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди. O(1)."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """Удалить и вернуть элемент из начала очереди. O(n).

        Граничный случай: при попытке извлечь из пустой очереди
        возбуждается IndexError.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self) -> Any:
        """Посмотреть первый элемент без удаления. O(1).

        Граничный случай: при пустой очереди возбуждается IndexError.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Проверка, пуста ли очередь. O(1)."""
        return len(self._items) == 0

    def size(self) -> int:
        """Количество элементов в очереди. O(1)."""
        return len(self._items)
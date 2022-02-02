from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """

        self.value = value
        self.next = next_

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {self._next})"

    @classmethod
    def is_valid(cls, node: Any) -> None:
        """Проверка относится ли к классу Node"""

        if not isinstance(node, (type(None), cls)):
            raise TypeError("Неверно введен тип данных")

    @property
    def next(self):
        """Возвращает значение node.next"""

        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        """Устанавливает значение node.next"""

        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, prev: Optional["DoubleLinkedNode"] = None,
                 next_: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        """Возвращает значение DoubleLinkedNode.prev"""
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["DoubleLinkedNode"]):
        """Устанавливает значение DoubleLinkedNode.prev"""
        self.is_valid(prev_)
        self._prev = prev_

    def __repr__(self):
        return f"{self.__class__.__name__}({self._prev}, {self.value}, {self._next})"


if __name__ == "__main__":
    node1 = Node(123)
    node2 = Node(456, node1)

    dnode1 = DoubleLinkedNode(111)
    dnode2 = DoubleLinkedNode(222)
    dnode3 = DoubleLinkedNode(333, dnode1, dnode2)

    print(node1)
    print(node2)

    print("---------")

    print(repr(node1))
    print(repr(node2))

    print("---------")

    print(repr(dnode1))
    print(repr(dnode2))
    print(repr(dnode3))

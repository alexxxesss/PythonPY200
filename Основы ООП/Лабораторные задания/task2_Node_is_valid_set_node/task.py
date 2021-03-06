from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next: следующий узел, если он есть
        """
        self.value = value

        self.next_node = None
        self.set_next(next)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next_node})"

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError('Тип данных не верный')

    def set_next(self, next: Optional["Node"] = None) -> None:
        self.is_valid(next)
        self.next_node = next


if __name__ == '__main__':
    first_node = Node(1)
    second_node = Node(2)

    first_node.set_next(second_node)

    # TODO свяжите первый узел со вторым

    print(first_node)
    print(second_node)


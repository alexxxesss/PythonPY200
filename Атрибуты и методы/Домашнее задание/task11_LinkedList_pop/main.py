from typing import Any, Iterable, Optional

from node import Node


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value: Any) -> None:
        """ Метод добавдяет узел по указанному индексу. """

        if not isinstance(index, int):
            raise TypeError()

        if index < 0:
            raise IndexError()

        append_node = Node(value)

        if index == 0:
            append_node.next = self.head
            self.head = append_node
            self.len += 1
        elif index >= self.len:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = self.step_by_step_on_nodes(index)

            self.linked_nodes(prev_node, append_node)
            self.linked_nodes(append_node, next_node)

            self.len += 1

    def index(self, value: int, start: int = 0, stop: Optional[int] = None):
        """ Метод возвращает значение индекса элемента по его значению. """
        if stop is None:
            stop = self.len
        for index in range(start, stop):
            if value == self.step_by_step_on_nodes(index).value:
                return index
        raise ValueError("Значение не найдено")

    def count(self, value: int):
        """ Метод возвращает возвращает количество раз, когда указанный элемент появляется в списке. """
        count = 0
        for index in range(self.len):
            if value == self.step_by_step_on_nodes(index).value:
                count += 1
        return count

    def extend(self, add_linked_list: Optional["LinkedList"] = None):
        """ Добавление связного списка в конец связного списка. """
        first_node_add_list = add_linked_list.step_by_step_on_nodes(0)
        if add_linked_list is not None:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, first_node_add_list)

            self.len += add_linked_list.len

    def pop(self, index: int = None):
        if index is None:
            index = self.len - 1
        elif index > self.len - 1:
            IndexError("Введено неверное значение индекса")
        del_node = self.step_by_step_on_nodes(index)
        self.__delitem__(index)
        return del_node


if __name__ == '__main__':
    list_ = [1, 5, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 5, 99]
    linked_list = LinkedList(list_)
    print(linked_list)
    print(len(linked_list))

    print("-----------")

    print(linked_list.pop())

    print("-----------")

    print(linked_list)
    print(len(linked_list))

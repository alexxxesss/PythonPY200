from collections.abc import MutableSequence
from typing import Any, Optional, Iterable
from node import Node


class LinkedList(MutableSequence):
    ABSTRACT_CLASS_NODE = Node

    def __init__(self, data: Iterable = None):
        """ Конструктор связного списка. """

        self._len = 0
        self._head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """

        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """

        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """ Метод удаляет узел по указанному индексу. """

        if not isinstance(index, int):
            raise TypeError("Тип данных введен неверно")

        if not 0 <= index < self._len:  # для for
            raise IndexError("Значение индекса некорректно")

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            tail = self.step_by_step_on_nodes(index - 1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def __len__(self) -> int:
        return self._len

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    @staticmethod
    def linked_nodes(left_node: ABSTRACT_CLASS_NODE, right_node: Optional[ABSTRACT_CLASS_NODE] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def to_list(self) -> list:
        """" Метод, который формирует Python список из связного списка. """

        return [linked_list_value for linked_list_value in self]

    def append(self, value: Any) -> None:
        """ Добавление элемента в конец связного списка. """

        append_node = self.ABSTRACT_CLASS_NODE(value)

        if self._head is None:
            self._head = append_node
        else:
            last_index = self._len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self._len += 1

    def step_by_step_on_nodes(self, index: int) -> ABSTRACT_CLASS_NODE:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """

        if not isinstance(index, int):
            raise TypeError("Тип данных введен неверно")

        if not 0 <= index < self._len:
            raise IndexError("Значение индекса некорректно")

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def insert(self, index: int, value: Any) -> None:
        """ Метод добавдяет узел с указанным значением левосторонней вставкой от указанного индекса. """

        if not isinstance(index, int):
            raise TypeError("Тип данных введен неверно")

        if index < 0:
            raise IndexError("Введен несуществующий индекс")

        append_node = Node(value)

        if index == 0:
            append_node.next = self._head
            self._head = append_node
            self._len += 1
        elif index >= self._len:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = self.step_by_step_on_nodes(index)

            self.linked_nodes(prev_node, append_node)
            self.linked_nodes(append_node, next_node)

            self._len += 1

    def index(self, value: int, start: int = 0, stop: Optional[int] = None) -> int:
        """ Метод возвращает значение индекса элемента по его значению. """

        if stop is None:
            stop = self._len
        for index in range(start, stop):
            if value == self.step_by_step_on_nodes(index).value:
                return index
        raise ValueError("Значение не найдено")

    def count(self, value: int) -> int:
        """ Метод возвращает возвращает количество раз, когда указанный элемент появляется в списке. """

        count = 0
        for index in range(self._len):
            if value == self.step_by_step_on_nodes(index).value:
                count += 1
        return count

    def extend(self, add_linked_list: Optional["LinkedList"] = None) -> None:
        """ Добавление связного списка в конец связного списка. """
        if len(add_linked_list) == 0:
            print("Попытка добавить пустой список, в списке ничего не поменяется")
        elif add_linked_list is not None:
            first_node_add_list = add_linked_list.step_by_step_on_nodes(0)
            last_index = self._len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, first_node_add_list)

            self._len += add_linked_list._len

    def pop(self, index: int = None) -> ABSTRACT_CLASS_NODE:
        """ Возвращает значение элемента связного списка по его индексу, а затем удаляет. """

        if index is None:
            index = self._len - 1
        elif index > self._len - 1:
            IndexError("Введено неверное значение индекса")
        del_node = self.step_by_step_on_nodes(index)
        self.__delitem__(index)
        return del_node


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":

    list_value = [1, 22, 3, 4, 5, 6, 22, 8, 9, 10, 22]
    list_value_2 = [111, 222, 333, 444, 555]
    linked_list = LinkedList(list_value)
    linked_list_2 = LinkedList(list_value_2)
    print(linked_list)
    print(linked_list_2)
    print("-" * 15)
    print(repr(linked_list))
    print(f'Длина односвязного списка: {len(linked_list)}')
    print("-" * 15)
    linked_list.__setitem__(4, 99)
    print(linked_list)
    print(linked_list.__getitem__(4))
    print("-" * 15)
    linked_list.__delitem__(4)
    print(linked_list)
    print(f'Длина односвязного списка: {len(linked_list)}')
    print("-" * 15)
    linked_list.insert(4, 99)
    print(linked_list)
    print(f'Длина односвязного списка: {len(linked_list)}')
    print("-" * 15)
    print(linked_list.index(10))
    print("-" * 15)
    print(linked_list.count(22))
    print("-" * 15)
    linked_list.extend(linked_list_2)
    print(linked_list)
    print(f'Длина односвязного списка: {len(linked_list)}')
    print("-" * 15)
    print(linked_list.pop(14))
    print(linked_list)
    print(f'Длина односвязного списка: {len(linked_list)}')

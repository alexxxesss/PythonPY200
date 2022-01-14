from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.__init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.__init_occupied_volume(occupied_volume)

    def __init_capacity_volume(self, value: Union[int, float]):
        """
        Функция проверяет задаваемый объем стакана

        :param value: значение объема стакана
        :return: значение задаваемого объема стакана после проверки типов
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if not value > 0:
            raise ValueError
        self.capacity_volume = value

    def __init_occupied_volume(self, value: Union[int, float]):
        """
        Функция проверяет занятый объем стакана

        :param value: значение занятого объема стакана
        :return: значение занятого объема стакана после проверки типов
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        self.occupied_volume = value


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

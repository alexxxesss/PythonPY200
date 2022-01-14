from typing import Union


class Glass:

    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.__capacity_volume = None
        self.__init_capacity_volume(capacity_volume)
        self.__occupied_volume = self.__check_occupied_volume(occupied_volume)

        self.__check_overflow(self.__capacity_volume, self.__occupied_volume)

    def __init_capacity_volume(self, value: Union[int, float]) -> Union[int, float]:
        """
        Функция проверяет задаваемый объем стакана

        :param value: значение объема стакана
        :return: значение задаваемого объема стакана после проверки типов
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if not value > 0:
            raise ValueError
        self.__capacity_volume = value

    @staticmethod
    def __check_occupied_volume(value):
        """
        Функция проверяет занятый объем стакана

        :param value: значение занятого объема стакана
        :return: значение занятого объема стакана после проверки типов
        """
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

    @staticmethod
    def __check_overflow(capacity, occupied):
        if capacity < occupied:
            raise OverflowError('Стакан не резиновый')

    def get_capacity_volume(self):
        return self.__capacity_volume

    def get_occupied_volume(self):
        return self.__occupied_volume

    def add_water(self, value):
        self.__check_occupied_volume(value)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume + value)
        self.__occupied_volume += value


if __name__ == "__main__":
    g1 = Glass(200, 100)  # экземпляр класса
    print(g1.get_capacity_volume())
    print(g1.get_occupied_volume())

from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.__capacity_volume = self.__check_capacity_volume(capacity_volume)
        self.__occupied_volume = self.__check_occupied_volume(occupied_volume)
        self.__check_overflow(self.__capacity_volume, self.__occupied_volume)

    @staticmethod
    def __check_capacity_volume(value: Union[int, float]) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if not value > 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value: Union[int, float]) -> Union[int, float]:
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
    glass1 = Glass(200, 100)  # экземпляр класса
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())

    glass2 = Glass(500, 200)
    print(glass2.get_capacity_volume(), glass2.get_occupied_volume())

    glass1.add_water(50)
    print(glass1.get_capacity_volume(), glass1.get_occupied_volume())
    print(glass2.get_capacity_volume(), glass2.get_occupied_volume())

    print(glass1 is glass2)




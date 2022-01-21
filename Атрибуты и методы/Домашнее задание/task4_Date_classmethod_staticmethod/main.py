class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def __is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def __get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if 12 < month <= 0:
            raise ValueError("Неверно введен месяц")

        if self.__is_leap_year(year):
            day_on_month = self.DAY_OF_MONTH[1][month-1]
        else:
            day_on_month = self.DAY_OF_MONTH[0][month-1]

        return day_on_month

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        day_on_month = self.__get_max_day(month, year)
        if day <= 0 or day > day_on_month:
            raise ValueError("Неверно введен день")

        print("Дата введена корректно")

if __name__ == "__main__":
    new_year = Date(29, 2, 2022)



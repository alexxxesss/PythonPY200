from driver import Driver


class DriverTypeError(Exception):
    pass


class Car:
    brand = None
    _max_speed = 180
    __created_car = 0

    def __init__(self, color, body_type, model_name, engine_type, gear_type, complectation):

        self.__model_name = model_name
        self.__body_type = body_type
        self._engine_type = engine_type
        self._gear_type = gear_type
        self.complectation = complectation
        self.color = color

        self.__driver = None

    @property
    def driver(self):
        if self.__driver is None:
            return "Водитель не найден"
        return self.__driver

    @driver.setter
    def driver(self, driver: Driver):
        if not isinstance(driver, Driver):
            raise DriverTypeError(f'Ожидается {type(Driver)}, получено {type(driver)}')
        self.__driver = driver

    # Эквивалент свойствам (property):
    # def set_driver(self, driver: Driver):
    #     if not isinstance(driver, Driver):
    #         raise DriverTypeError(f'Ожидается {type(Driver)}, получено {type(driver)}')
    #     self.driver = driver
    #
    # def get_driver(self):
    #     return self.driver


if __name__ == "__main__":

    car = Car("Черный", "седан", "модель", "бензин", "автомат", "люкс")
    car.driver = Driver("Иван")
    print(car.driver)

# class Nissan(Car):
#     brand = "Nissan"
#
#     def __init__(self):
#

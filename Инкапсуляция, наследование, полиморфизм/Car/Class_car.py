import time

from driver import Driver


class DriverTypeError(Exception):
    pass


class EngineIsNotRunning(Exception):
    pass


class DriverNotFoundError(Exception):
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

        self.__mileage = 0
        self.__driver = None
        self.__engine_status = True

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

    def start_engine(self):
        self.__engine_status = True

    def __check_driver(self):
        if self.driver is not None:
            return True
        return False

    def __ready_status(self):
        if not self.__engine_status:
            raise EngineIsNotRunning("двигатель не запущен")
        if not self.__check_driver():
            raise DriverNotFoundError("водитель не найден")

        # if self.__engine_status and self.__check_driver():
        #     return True
        # return False

    def move(self, distance=10):
        try:
            if self.__ready_status():
                for i in range(distance):
                    print(f"Машина проехала {i+1} км")
                    time.sleep(0.3)
                print("Путь пройден")
        except (EngineIsNotRunning, DriverNotFoundError) as e:
            print(f'Машина не может начать движение, т.к. {e}')

    @property
    def _mileage(self):
        repr(self.__mileage)

    @_mileage.setter
    def _mileage(self):
        if not isinstance(mileage, (int, float)):
            raise T


if __name__ == "__main__":

    car = Car("Черный", "седан", "модель", "бензин", "автомат", "люкс")
    car.start_engine()

    car.driver = Driver("Иван")
    car.move()

# class Nissan(Car):
#     brand = "Nissan"
#
#     def __init__(self):
#

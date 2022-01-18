class Date:

    def __init__(self, day, month, year):
        self.day = None
        self.month = None
        self.year = None

        self.check_attr(day, month, year)

    def check_attr(self, day, month, year):
        if isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            self.day = day
            self.month = month
            self.year = year
        else:
            raise TypeError('Введено неверное значение')

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self):
        day = f"{self.day}".rjust(2, "0")
        month = f"{self.month}".rjust(2, "0")
        return f"{day}/{month}/{self.year}"


if __name__ == "__main__":

    new_year = Date(1, 1, 2022)
    print(new_year)

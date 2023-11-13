class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    date_string = "10-11-20222"
    date_string = "10-11-2022"
    @classmethod
    def extract_numbers(cls):
        day, month, year = map(int, cls.date_string.split("-"))
        return day, month, year

    @staticmethod
    def validate_date(day, month, year):
        if day < 1 or day > 31:
            raise ValueError("Недопустимое значение для дня")
        if month < 1 or month > 12:
            raise ValueError("Недопустимое значение для месяца")
        if year < 1000 or year > 9999:
            raise ValueError("Недопустимое значение для года")


# Пример использования класса
date_string = "01-01-2022"

date = Date(date_string)

day, month, year = date.extract_numbers()
print("Извлеченные числа:", day, month, year)

try:
    Date.validate_date(day, month, year)
    print("Дата валидна")
except ValueError as e:
    print("Ошибка валидации:", str(e))

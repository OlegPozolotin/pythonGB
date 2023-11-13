class DivisionByZeroError(Exception):
    def __init__(self, message="Деление на ноль"):
        super().__init__(message)


# Пример использования класса-исключения
try:
    dividend = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))

    if divisor == 0:
        raise DivisionByZeroError()

    result = dividend / divisor
    print("Результат деления:", result)

except ValueError:
    print("Ошибка ввода. Введите целое число.")
except DivisionByZeroError as e:
    print("Ошибка:", str(e))
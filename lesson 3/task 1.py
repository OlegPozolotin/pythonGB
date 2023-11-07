def divide_numbers(x, y):
    """

    :param x:
    :param y:
    :return:
    """
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")


# Ввод чисел пользователем
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вызов функции деления и обработка исключений
result = divide_numbers(num1, num2)
if result is not None:
    print("Результат деления:", result)

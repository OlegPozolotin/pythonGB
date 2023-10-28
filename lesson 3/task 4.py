def my_func(x, y):
    if y == 0:
        return 1
    result = 1
    for _ in range(abs(y)):
        result *= x
    if y < 0:
        result = 1 / result
    return result

# Тестирование функции
x = float(input("Введите положительное число x: "))
y = int(input("Введите отрицательное целое число y: "))
power_result = my_func(x, y)
print(f"Результат возведения числа {x} в степень {y}: {power_result}")

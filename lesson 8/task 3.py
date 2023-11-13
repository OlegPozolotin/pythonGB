class OnlyNumbersError(Exception):
    def __init__(self, message="Введенное значение не является числом"):
        super().__init__(message)


# Пример использования класса-исключения
numbers_list = []

while True:
    try:
        value = input("Введите число (или 'stop' для завершения): ")

        if value == "stop":
            break

        if not value.isnumeric():
            raise OnlyNumbersError()

        numbers_list.append(int(value))

    except OnlyNumbersError as e:
        print("Ошибка:", str(e))

# Вывод списка с числами
print("Список чисел:", numbers_list)

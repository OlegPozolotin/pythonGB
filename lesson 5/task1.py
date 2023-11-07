# Открываем файл для записи
with open('data.txt', 'w') as file:
    while True:
        # Получаем данные от пользователя
        data = input("Введите данные (пустая строка для окончания ввода): ")

        # Проверяем, является ли строка пустой
        if data == "":
            break

        # Записываем данные в файл
        file.write(data + "\n")

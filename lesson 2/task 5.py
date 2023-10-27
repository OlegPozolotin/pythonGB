# Задание начального списка рейтинга
rating_list = [7, 5, 3, 3, 2]

# Ввод нового элемента рейтинга от пользователя
new_element = int(input("Введите новый элемент рейтинга: "))

# Поиск позиции для вставки нового элемента
position = 0
while position < len(rating_list) and new_element < rating_list[position]:
    position += 1

# Вставка нового элемента в список рейтинга на найденную позицию
rating_list.insert(position, new_element)

# Вывод обновленного списка рейтинга
print("Обновленный рейтинг:", rating_list)
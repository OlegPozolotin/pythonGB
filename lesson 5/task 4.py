numbers_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

# Открываем исходный файл на чтение
with open('data.txt', 'r', encoding='utf-8') as file:
    # Создаем новый файл для записи
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        # Читаем каждую строку из исходного файла
        for line in file:
            # Разделяем строку на слова
            words = line.split()

            # Переводим английские числительные в русские
            new_words = [numbers_dict.get(word, word) for word in words]

            # Соединяем слова обратно в строку
            new_line = " ".join(new_words)

            # Записываем новую строку в файл
            output_file.write(new_line + "\n")
import re

# Открываем файл для чтения
with open('schedule.txt', 'r', encoding='utf-8') as file:
    # Инициализируем словарь для хранения общего количества занятий по предметам
    subjects_dict = {}

    # Обрабатываем каждую строку файла
    for line in file:
        # Разделяем строку на название предмета и список занятий
        subject, lessons_str = line.split(":", maxsplit=1)

        # Инициализируем общее количество занятий для предмета
        total_lessons = 0

        # Ищем все пары чисел в строке
        lessons = re.findall(r'\d+', lessons_str)
        if lessons:
            # Суммируем все числа
            total_lessons = sum(map(int, lessons))

        # Добавляем предмет и его общее количество занятий в словарь
        subjects_dict[subject.strip()] = total_lessons

# Выводим словарь с общим количеством занятий по предметам
print(subjects_dict)


import random

# Генерируем случайный набор чисел
numbers = [random.randint(1, 100) for _ in range(10)]

# Открываем файл для записи
with open('numbers.txt', 'w') as file:
    # Записываем числа в файл с разделителями
    file.write(' '.join(map(str, numbers)))

# Открываем файл для чтения
with open('numbers.txt', 'r') as file:
    # Читаем содержимое файла и разделяем на отдельные числа
    numbers_read = list(map(int, file.read().split()))

# Вычисляем сумму чисел
sum_numbers = sum(numbers_read)

# Выводим сумму на экран
print("Сумма чисел:", sum_numbers)

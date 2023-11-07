import random


def get_greater_elements(numbers):
    result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
    return result


# Генерация списка из 13 случайных чисел
numbers = [random.randint(1, 100) for _ in range(13)]

# Получение элементов, больших предыдущего элемента
result = get_greater_elements(numbers)
print(result)

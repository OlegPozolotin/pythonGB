def calculate_sum(numbers):
    """

    :param numbers:
    :return:
    """
    numbers_list = numbers.split()

    # Проверка наличия специального символа
    if 'Q' in numbers_list:
        numbers_list.remove('Q')
        should_continue = False
    else:
        should_continue = True

    # Суммирование чисел
    numbers_sum = sum(map(float, numbers_list))
    return numbers_sum, should_continue


total_sum = 0
continue_input = True

while continue_input:
    user_input = input("Введите числа, разделенные пробелом (для выхода введите 'Q'): ")
    current_sum, continue_input = calculate_sum(user_input)

    # Добавление текущей суммы к общей сумме
    total_sum += current_sum

    print("Сумма чисел:", total_sum)

print("Программа завершена.")

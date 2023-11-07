def int_func(word):
    """

    :param word:
    :return:
    """
    return word.capitalize()


# Тестирование функции
word = input("Введите слово из маленьких латинских букв: ")
result = int_func(word)
print(result)

def int_func(word):
    """

    :param word:
    :return:
    """
    return word.capitalize()


def process_string(string):
    """

    :param string:
    :return:
    """
    words = string.split()
    capitalized_words = [int_func(word) for word in words]
    processed_string = ' '.join(capitalized_words)
    return processed_string


# Тестирование функции
string = input("Введите строку из слов, разделенных пробелами: ")
result = process_string(string)
print(result)

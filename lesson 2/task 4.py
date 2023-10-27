# Ввод строки от пользователя
sentence = input("Введите строку из нескольких слов: ")

# Разделение строки на слова
words = sentence.split()

# Вывод каждого слова с новой строки с учетом ограничения в 10 символов
for index, word in enumerate(words, 1):
    shortened_word = word[:10] if len(word) > 10 else word
    print(f"{index}. {shortened_word}")

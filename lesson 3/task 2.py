def print_user_data(name, surname, birth_year, city, email, phone):
    """

    :param name:
    :param surname:
    :param birth_year:
    :param city:
    :param email:
    :param phone:
    """
    user_data = f"Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город: {city}, Email: {email}, Телефон: {phone}"
    print(user_data)


# Вызов функции и передача параметров как именованных аргументов
print_user_data(name="John", surname="Doe", birth_year=1990, city="New York", email="johndoe@example.com",
                phone="123-456-7890")

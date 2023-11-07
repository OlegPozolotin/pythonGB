# Ввод месяца от пользователя
month = int(input("Введите номер месяца (от 1 до 12): "))

# Определение времени года с использованием списка
seasons = ['зима', 'весна', 'лето', 'осень']
if month in [1, 2, 12]:
    season = seasons[0]
elif month in [3, 4, 5]:
    season = seasons[1]
elif month in [6, 7, 8]:
    season = seasons[2]
elif month in [9, 10, 11]:
    season = seasons[3]
else:
    season = "несуществующий месяц"

# Вывод результата
if season != "несуществующий месяц":
    print(f"Месяц {month} относится к времени года: {season}.")
else:
    print(f"{month} - {season}")

# Ввод месяца от пользователя
month = int(input("Введите номер месяца (от 1 до 12): "))

# Определение времени года с использованием словаря
seasons = {
    (1, 2, 12): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень'
}

# Поиск времени года в словаре
season = ''
for key in seasons:
    if month in key:
        season = seasons[key]
        break

# Вывод результата
if season:
    print(f"Месяц {month} относится к времени года: {season}.")
else:
    print(f"Введенный номер месяца {month} является некорректным.")

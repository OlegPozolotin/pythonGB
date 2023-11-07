import sys


def calculate_salary(hours, rate, bonus):
    try:
        hours_worked = float(hours)
        hourly_rate = float(rate)
        bonus_amount = float(bonus)

        salary = (hours_worked * hourly_rate) + bonus_amount
        return salary
    except ValueError:
        print("Ошибка: введены некорректные значения")


# Получение аргументов командной строки
arguments = sys.argv[1:]

if len(arguments) == 3:
    hours_worked, hourly_rate, bonus_amount = arguments
else:
    hours_worked = input("Введите выработку в часах: ")
    hourly_rate = input("Введите ставку в час: ")
    bonus_amount = input("Введите премию: ")

salary_result = calculate_salary(hours_worked, hourly_rate, bonus_amount)
if salary_result:
    print("Заработная плата сотрудника:", salary_result)

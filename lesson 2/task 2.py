# Заполнение списка элементами с помощью функции input()
my_list = []
n = int(input("Введите количество элементов списка: "))
for i in range(n):
    element = input(f"Введите значение элемента {i + 1}: ")
    my_list.append(element)

# Обмен значениями соседних элементов
for i in range(0, len(my_list) - 1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# Вывод списка после обмена значений
print("Список после обмена значений соседних элементов:", my_list)
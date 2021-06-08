# *** Коллекции (контейнеры) ***

# ** Список (list)

# Создание пустого списка
my_list = []
my_list = list()

# PEP8

# добавление объекта (элемента) в список
my_list.append(100)
my_list.append(3.14)
my_list.append("hello")
my_list.append([10, 20, 30])

# print(my_list)

# Чтение значений элемента
# в квадратную скобочку указываем индекс
el = my_list[3]
el = my_list[3][1]

# обратная индексация
el = my_list[-1]

# Замена значения элемента
my_list[0] = 2000

# Удаление элемента по значению
# my_list.remove(3.14)

# Удаление элемента по индексу
del my_list[-1]


# Срез списка
s = "Hello, World!"
my_list = list(s)

# срез со 2-го индекса до конца исходного списка
my_slice = my_list[2:]

# срез со 2-го нидекса до 5-го индекса не включительно
my_slice = my_list[2:5]

# срез с начала до 5-го нидекса не включительно
my_slice = my_list[:5]

# срез со 2-го индекса до 12 не включительно
# с шагом 2
my_slice = my_list[2:12:2]

# срез с применением обратной индексации
my_slice = my_list[-2:5]

# len() возвращает длину (количество элементов) коллекции
# print(len(my_list))
# print(my_list)
# print(my_slice)


# *** Кортеж (tuple) ***

# неизменяемая (immutable) коллекция

# создание кортежа
my_tuple = (10, 20, 30, 40, 50)

# my_tuple[0] = 100

print(my_tuple)

# чтение значения элементов
# print(my_tuple[0])

# срез
# print(my_tuple[2:])


# *** Словарь (dict) ***

# изменяемый, упорядоченный тип коллекции

# пара "ключ-значение"
# {ключ_1:значение_1, ключ_2:значение_2}

# создание словаря
my_dict = {10:3.14, "abc":[1,2,3]}

# print(my_dict)

# чтение значений
# print(my_dict[10])
# print(my_dict["abc"])

data0 = {"name":"Aiastaan", "age":15, "id":457.4}
data1 = {"name":"Henry", "age":14, "id":786.7}
data2 = {"name":"Michael", "age":14, "id":914.9}

total_data = {"p0":data0, "p1":data1, "p2":data2}

# print(total_data["p1"]["name"])

# изменение значений
my_dict["abc"] = "hello"

# при присвоении нового значения по несуществующему ключу
# создается новая пара
my_dict['A'] = 777

# удаление пары (элемента)
del my_dict[10]

# обновление данных

data0 = {"name":"Aiastaan", "age":15, "id":457.4}

data0.update({"age":16, "id":468.4, "w":45.8})

print(data0)
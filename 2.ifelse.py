# *** Логические операции ***

z = 3
w = 2

# операция "равно"
# мы спрашиваем "значение z равно значению w?"
# ответ будет присвоен переменной result
result = z == w

# операция "не равно"
result = z != w

# операция "меньше"
result = z < w

# операция "больше"
result = z > w

# операция "меньше либо равно"
result = z <= w

# операция "больше либо равно"
result = z >= w


# чистые логические операции

var_1 = True
var_2 = True

# оператор "НЕ" (NOT, инверция)
result = not var_1

# оператор "И" (AND)
# возвращает True толдько тогда,
# когда обе переменных являются True
result = var_1 and var_2

# оператор "ИЛИ" (OR)
# возвращает False только тогда,
# когда обе переменных являются False
result = var_1 or var_2

# print(result)


# *** Условные операторы ***

# Оператор if ("если")
# if False:
#    w = "hello"
#    print(w)

z = 10

# if z < 3: # "если"
#   print("меньше")
# else: "иначе"
#   print("не меньше")

v = "A"

if v == "B":
    res = "literal B"
elif v == "A":
    res = "literal A"
elif v == "D":
    res = "literal D"
elif v == "W":
    res = "literal W"
else:
    res = "не понятный мне символ :("

# print(res)


# *** пример, "Термостат" ***

# текущая температура помещения
current_temp = 25

# заданное значение диапазона температур
min_temp = 10
max_temp = 25

# параметр люди "есть/нет"
h = True

# логика термостата
if current_temp < min_temp and not h:
    print("включен нагрев до {min_temp}")
elif current_temp < max_temp and h:
    print("включен нагрев до {max_temp}")
else:
    print("нагрев выключен")
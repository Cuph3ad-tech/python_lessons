# *** Основы объектно-ориентированного программирования ***

# Объект принадлежит определенному классу (типу)
# Объекты обладают свойствами и методами (функции)

# Класс - это некий "чертеж" ("план") объектов.

# Объект опредлеленного класса называется экземпляром класса.


# Создание (определение) класса
# Названия классов принято писать с заглавной буквы
class Greeting:
    def __init__(self):
        # метод-конструктор
        # здесь создаются свойства (атрибут, поле)

        self.age = None

    def wassup(self):
        # метод
        print(f"Wassup, howzitgoin?! My age: {self.age}")

# создание экземпляров (объектов) класса Greeting
great = Greeting()

# присвоение значения свойству
great.age = 5

# чтение значения из свойства
val = great.age

# print(val)

# вызов метода
# great.wassup()

# ещё один экземпляр класса Greeting
good = Greeting()

good.age = 10

# good.wassup()


# *** Принцип Наследования ***

# Классы могут наследовать свойства и методы у других классов

# создание родительского (предкового) класса
class Farewell:
    def __init__(self, n_words):
        self.num_words = n_words

    def express(self):
        print(f"I express. Num words: {self.num_words}")

# создание дочерних классов
class Farewell_1(Farewell):
    pass

class Farewell_2(Farewell):
    def info(self):
        print("Farewell_2 is here")

Cya = Farewell_1(4)

Cya.express()

Bye = Farewell_2(5)

Bye.express()
Bye.info()

# самостоятельно:
# - полиморфизм
# - инкапсуляция
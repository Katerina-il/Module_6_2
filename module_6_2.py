""" Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств"  """

"""  Задача "Изменять нельзя получать":

В этой задаче мы реализуем классы транспорта, в которых нельзя будет просто так поменять цвет, 
мощность двигателя и прочие свойства, т.к. в реальной жизни это чаще всего делается не владельцем, 
а в специальных сервисах. Да, узнать значения этих свойств мы сможем, но вот изменить - нет. 
 
 
Пункты задачи:

1. Создайте классы Vehicle и Sedan.
2. Напишите соответствующие свойства в обоих классах.
3. Не забудьте сделать Sedan наследником класса Vehicle.
4. Создайте объект класса Sedan и проверьте, как работают все его методы, взяты из класса Vehicle. """

# from symtable import Class

class Vehicle:  # где Vehicle - это любой транспорт

    __COLOR_VARIANTS = [ "black", "rose", "white", "red", "blue dream", "sunset rose", "orange juice", 'blue', 'green']
        # Атрибут класса , в который записан список допустимых цветов для окрашивания.(Цвета свои)

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner  # индивидуальное имя
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color
        # owner = ""  # Атрибут владелец транспорта.(владелец может меняться)
        # __model = ""  # Атрибут модель(марка) транспорта.(мы не можем менять название модели)
        # __engine_power = int  # Атрибут мощность двигателя.(мы не можем менять мощность двигателя самостоятельно)
        # __color = ""  # Атрибут название цвета.(мы не можем менять цвет автомобиля своими руками)

class Sedan(Vehicle): # Sedan(седан) - наследник класса Vehicle
    __PASSENGERS_LIMIT = 5


    def get_model(self):
        print (f"Модель: {self.model}")

    def get_horsepower(self):
        return f"Мощность двигателя: {self.engine_power}"

    def get_color(self):
        return f"Цвет: {self.color}"

    def print_info(self):
        print(self.get_model(), self.get_horsepower(), self.get_color(), f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)


# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


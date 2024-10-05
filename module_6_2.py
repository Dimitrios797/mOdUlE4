class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']  # Допустимые цвета

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner  # Владелец
        self.__model = model  # Модель (скрытый атрибут)
        self.__engine_power = engine_power  # Мощность двигателя (скрытый атрибут)
        self.__color = color  # Цвет (скрытый атрибут)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5  # Максимальное количество пассажиров

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)  # Инициализация родительского класса


# Пример использования классов
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')  # Неправильный цвет
vehicle1.set_color('BLACK')  # Правильный цвет
vehicle1.owner = 'Vasyok'  # Меняем владельца

# Проверяем что поменялось
vehicle1.print_info()
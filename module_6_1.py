# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True  # Живое
        self.fed = False   # Накормленное
        self.name = name   # Индивидуальное название

# Родительский класс Plant
class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность по умолчанию
        self.name = name      # Индивидуальное название

# Класс-наследник Mammal
class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс-наследник Predator
class Predator(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс-наследник Flower
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)

# Класс-наследник Fruit
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем на съедобное

# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов и методов
print(a1.name)  # Вывод: Волк с Уолл-Стрит
print(p1.name)  # Вывод: Цветик семицветик

print(a1.alive)  # Вывод: True
print(a2.fed)    # Вывод: False

a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее ест фрукт

print(a1.alive)  # Вывод: False (если цветок несъедобный)
print(a2.fed)    # Вывод: True (если фрукт съедобный)
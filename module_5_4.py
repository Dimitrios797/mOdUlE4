class House:
    houses_history = []  # Атрибут класса для хранения истории построенных домов

    def __new__(cls, *args, **kwargs):
        # Добавляем название дома в историю
        cls.houses_history.append(args[0])
        return super(House, cls).__new__(cls)  # Создаем новый экземпляр объекта

    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")  # Сообщение при удалении объекта

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"


# Пример выполнения программы
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # Ожидаемый вывод: ЖК Акация снесён, но он останется в истории
del h3  # Ожидаемый вывод: ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # Ожидаемый вывод: ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
del h1  # Ожидаемый вывод: ЖК Эльбрус снесён, но он останется в истории
class House:
    def __init__(self, name, number_of_floors):
        self.name = name  # Название дома
        self.number_of_floors = number_of_floors  # Количество этажей

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors  # Возвращает количество этажей

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # Возвращает строку с информацией о доме

# Создание объектов класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Демонстрация работы метода __str__
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 20

# Демонстрация работы метода __len__
print(len(h1))  # Ожидаемый вывод: 10
print(len(h2))  # Ожидаемый вывод: 20
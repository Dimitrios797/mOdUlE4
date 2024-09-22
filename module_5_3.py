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

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)  # Используем __add__

    def __iadd__(self, value):
        return self.__add__(value)  # Используем __add__

# Пример выполняемого кода
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # Ожидаемый вывод: False

h1 = h1 + 10  # Увеличиваем этажи на 10
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # Ожидаемый вывод: True

h1 += 10  # Увеличиваем этажи на 10 с помощью оператора +=
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # Увеличиваем этажи у h2 на 10 с помощью оператора +
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)   # Ожидаемый вывод: False
print(h1 >= h2)  # Ожидаемый вывод: True
print(h1 < h2)   # Ожидаемый вывод: False
print(h1 <= h2)  # Ожидаемый вывод: True
print(h1 != h2)  # Ожидаемый вывод: False
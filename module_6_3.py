class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звук, который издает лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полета


class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)  # Инициализируем класс родитель Horse
        Eagle.__init__(self)  # Инициализируем класс родитель Eagle

    def move(self, dx, dy):
        self.run(dx)  # Вызываем метод run из класса Horse
        self.fly(dy)  # Вызываем метод fly из класса Eagle

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение

    def voice(self):
        print(self.sound)  # Печатаем звук орла


# Пример использования классов
if __name__ == "__main__":
    p1 = Pegasus()

    print(p1.get_pos())  # Вывод: (0, 0)
    p1.move(10, 15)
    print(p1.get_pos())  # Вывод: (10, 15)
    p1.move(-5, 20)
    print(p1.get_pos())  # Вывод: (5, 35)

    p1.voice()  # Вывод: I train, eat, sleep, and repeat
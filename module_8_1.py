def add_everything_up(a, b):
    # Проверяем, являются ли оба аргумента числами (int или float)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b  # Стандартное сложение чисел
    # Проверяем, являются ли оба аргумента строками
    elif isinstance(a, str) and isinstance(b, str):
        return a + b  # Стандартное сложение строк
    else:
        # Если типы разные, возвращаем строковое представление обоих аргументов
        return str(a) + str(b)

# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))     # Вывод: яблоко4215
print(add_everything_up(123.456, 7))          # Вывод: 130.456
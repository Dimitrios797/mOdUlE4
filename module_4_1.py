# module_4_1.py
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вызов функций с различными аргументами
result1 = fake_divide(69, 3)  # Ожидается: 23.0
result2 = fake_divide(3, 0)    # Ожидается: 'Ошибка'
result3 = true_divide(49, 7)   # Ожидается: 7.0
result4 = true_divide(15, 0)   # Ожидается: inf

# Вывод результатов на экран
print(result1)  # Вывод: 23.0
print(result2)  # Вывод: 'Ошибка'
print(result3)  # Вывод: 7.0
print(result4)  # Вывод: inf
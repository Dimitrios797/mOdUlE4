def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # Вызов вложенной функции внутри test_function


# Вызов test_function
test_function()

# Попытка вызвать inner_function вне test_function
try:
    inner_function()  # Это вызовет ошибку
except NameError as e:
    print(f"Ошибка: {e}")
import os
import time

def display_file_info(directory):
    # Обход каталога с помощью os.walk
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Формируем полный путь к файлу
            filepath = os.path.join(root, file)
            # Получаем время последнего изменения файла
            filetime = os.path.getmtime(filepath)
            # Форматируем время
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            # Получаем размер файла
            filesize = os.path.getsize(filepath)
            # Получаем родительскую директорию файла
            parent_dir = os.path.dirname(filepath)

            # Вывод информации о файле
            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Пример использования функции
if __name__ == "__main__":
    directory = "."  # Текущий каталог
    display_file_info(directory)
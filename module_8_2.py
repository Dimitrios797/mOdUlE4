def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += float(item)  
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {item}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:

        if not hasattr(numbers, '__iter__') or isinstance(numbers, str):
            raise TypeError

        total_sum, incorrect_count = personal_sum(numbers)


        count = len(numbers) - incorrect_count

        if count == 0:
            raise ZeroDivisionError

        return total_sum / count

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
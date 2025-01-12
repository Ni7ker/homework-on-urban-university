def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for element in numbers:
        try:
            result += float(element)
        except (TypeError, ValueError):
            print(f'Некорректный тип данных для подсчёта суммы - {element}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        total, incorrect_count = personal_sum(numbers)
        valid_count = len(numbers) - incorrect_count
        if valid_count == 0:
            return 0
        return total / valid_count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None

# Тестовые вызовы
print(f"Результат 1: {calculate_average('1, 2, 3')}")  # Строка
print(f"Результат 2: {calculate_average([1, 'Строка', 3, 'Ещё Строка'])}")  # Смешанные типы
print(f"Результат 3: {calculate_average(567)}")  # Некорректный тип данных
print(f"Результат 4: {calculate_average([42, 15, 36, 13])}")  # Корректные данные

def calculate_structure_sum(data):
    total = 0

    # Проверяем тип элемента
    if isinstance(data, (int, float)):
        # Если число, добавляем его к сумме
        total += data
    elif isinstance(data, str):
        # Если строка, добавляем её длину
        total += len(data)
    elif isinstance(data, (list, tuple, set)):
        # Если список, кортеж или множество, проходим по его элементам
        for item in data:
            total += calculate_structure_sum(item)
    elif isinstance(data, dict):
        # Если словарь, проходим по ключам и значениям
        for key, value in data.items():
            total += calculate_structure_sum(key)
            total += calculate_structure_sum(value)

    return total

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
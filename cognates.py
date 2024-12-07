def single_root_words(root_word, *other_words):
    same_words = []  # Список для подходящих слов

    # Приводим корень к нижнему регистру для нечувствительности к регистру
    root_word_lower = root_word.lower()

    # Перебираем все переданные слова
    for word in other_words:
        word_lower = word.lower()

        # Проверяем, что корень присутствует в слове и длина слова больше длины корня
        if root_word_lower in word_lower and len(word_lower) > len(root_word_lower):
            same_words.append(word)  # Если условие выполнено, добавляем слово

    return same_words  # Возвращаем список найденных слов


# Пример вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Dis' and 'ble', 'Able', 'Disable', 'Bagel')

# Вывод результата
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']

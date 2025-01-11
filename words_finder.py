import os
import string


class WordsFinder:
    def __init__(self, *file_names):
        # Имена файлов сохраняются в атрибут file_names
        self.file_names = file_names

    def get_all_words(self):
        # Подготовка словаря для всех слов
        all_words = {}
        for file_name in self.file_names:
            if not os.path.exists(file_name):
                raise FileNotFoundError(f"Файл {file_name} не найден")

            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()  # Преобразуем текст в нижний регистр
                for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punct, ' ')  # Убираем пунктуацию
                words = text.split()  # Разбиваем текст на слова
                all_words[file_name] = words
        return all_words

    def find(self, word):
        # Поиск первого вхождения слова в каждом файле
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            try:
                position = words.index(word) + 1  # Нумерация с 1
                results[name] = position
            except ValueError:
                results[name] = None  # Слово не найдено
        return results

    def count(self, word):
        # Подсчет количества вхождений слова в каждом файле
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for name, words in all_words.items():
            results[name] = words.count(word)
        return results


# Пример использования
if __name__ == "__main__":
    # Создайте файл test_file.txt с вашим текстом перед выполнением кода
    finder = WordsFinder('test_file.txt')

    # Получаем все слова из файла
    all_words = finder.get_all_words()
    print(all_words)

    # Находим первое вхождение слова "text"
    first_occurrence = finder.find('TEXT')
    print(first_occurrence)

    # Считаем количество вхождений слова "text"
    word_count = finder.count('teXT')
    print(word_count)

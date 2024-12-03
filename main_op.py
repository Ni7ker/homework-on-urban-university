def generate_password(n):
    result = ""  # Хранит итоговый пароль
    for a in range(1, n):  # Проходим по всем числам от 1 до n-1
        for b in range(a + 1, n + 1):  # b должно быть больше a
            if a + b == n:  # Проверяем, что сумма пары равна n
                result += f"{a}{b}"  # Добавляем пару к паролю
    return result

# Пример использования
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    print(f"Пароль для числа {n}: {generate_password(n)}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")

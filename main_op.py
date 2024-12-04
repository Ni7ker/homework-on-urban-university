def generate_password_with_pairs(n):
    result = ""  # Хранит итоговый пароль
    pairs = [] # Хранит список пар
    for a in range(1, n):  # Проходим по всем числам от 1 до n-1
        for b in range(a + 1, n):  # b должно быть больше a
            pair_sum = a + b # Сумма пары
            if n % pair_sum == 0: # Проверяем, что n кратна сумме пары
                result += f"{a}{b}"  # Добавляем пару к паролю
                pairs.append((a, b)) # Сохраняем пару в список
    return result, pairs

# Пример использования
n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password, pairs = generate_password_with_pairs(n)
    print(f"Пароль для числа {n}: {password}")
    print(f"Пары чисел для числа {n}: {pairs}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")

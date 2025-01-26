def sum_three(a, b, c):
    return a + b + c

def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            for i in range(2, result):
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

sum_three = is_prime(sum_three)

result = sum_three(2, 3, 6)
print(result)
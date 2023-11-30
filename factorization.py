import random
import math

def modpow(base, exponent, modulus):
    # Ініціалізація результату
    res = 1

    # Цикл, поки exponent не стане 0
    while (exponent > 0):
        # Якщо exponent непарне, множимо на базу
        if (exponent & 1):
            res = (res * base) % modulus

        # Ділимо exponent на 2
        exponent = exponent >> 1

        # Збільшуємо базу
        base = (base * base) % modulus

    return res

def pollard(n):
    # Обробка особливих випадків
    if (n == 1):
        return n
    if (n % 2 == 0):
        return 2

    # Ініціалізація змінних x, y, c
    x = random.randint(0, 2) % (n - 2)
    y = x
    c = random.randint(0, 1) % (n - 1)

    # Ініціалізація дільника
    d = 1

    # Цикл, поки не знайдено дільник
    while (d == 1):
        # "Тортуга" (повільний крок)
        x = (modpow(x, 2, n) + c + n) % n

        # "Заєць" (швидкий крок)
        y = (modpow(y, 2, n) + c + n) % n
        y = (modpow(y, 2, n) + c + n) % n

        # Обчислення найбільшого спільного дільника
        d = math.gcd(abs(x - y), n)

        # Якщо d дорівнює n, спробуємо ще раз
        if (d == n):
            return pollard(n)

    # Повертаємо дільник
    return d

# Зчитування числа для факторизації
check = int(input("Введіть число для факторизації: "))

# Виведення результату
print("Результат: ", check, " : ", pollard(check))

import math

def discreteLogarithm(a, b, m):
    n = int(math.sqrt(m) + 1)

    # Перевірка основи і модуля
    if a == 0 or m <= 1:
        return "Некоректні вхідні дані: a має бути більше 0 і m більше 1."

    an = 1
    for i in range(n):
        an = (an * a) % m

    value = [0] * m

    cur = an
    for i in range(1, n + 1):
        if value[cur] == 0:
            value[cur] = i
        cur = (cur * an) % m

    cur = b
    for i in range(n + 1):
        if value[cur] > 0:
            ans = value[cur] * n - i
            if ans < m:
                return ans
        cur = (cur * a) % m

    return "Не знайдено"

def babystep_giantstep_method():
    try:
        print("h = g^x mod p")
        h = int(input("h: "))
        g = int(input("g: "))
        p = int(input("p: "))

        if h < 0 or g < 0 or p < 0:
            print("Всі числа мають бути невід'ємні.")
        else:
            result = discreteLogarithm(g, h, p)
            print("x = ", result)
    except ValueError:
        print("Некоректний ввід.")

babystep_giantstep_method()

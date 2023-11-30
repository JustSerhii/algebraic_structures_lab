import random


def jacobi(a, m):
    if m <= 0:
        raise ValueError("n має бути додатнім")
    if m % 2 == 0:
        raise ValueError("n має бути непарним")
    a %= m
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = m % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            result = -result
        a %= m
    if m == 1:
        return result
    else:
        return 0


def solovoyStrassen(p, iterations):
    if (p < 2):
        return False
    if (p != 2 and p % 2 == 0):
        return False
    for i in range(iterations):
        a = random.randrange(p - 1) + 1
        jacobian = (p + jacobi(a, p)) % p
        mod = pow(a, int((p - 1) / 2), p)
        if (jacobian == 0 or mod != jacobian):
            return False
    return True


def strassen_method():
    num = int(input("Введіть число: "))

    iterations = int(input("Введіть кількість ітерацій: "))
    if (solovoyStrassen(num, iterations)):
        print(f"{num} є простим.")
    else:
        print(f"{num} не є простим.")


strassen_method()
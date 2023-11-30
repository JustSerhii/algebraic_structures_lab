def Legendre(arr, p):
    e = (p - 1) // 2
    results = [pow(a, e, p) for a in arr]
    return [(r-p if r > 1 else r) for r in results]


n = int(input("Оберіть число для функції Лежандра: "))
p = int(input("Оберіть число для функції Лежандра: "))
print("Функція Лежандра для числа", n, "дорівнює", Legendre([n], p))

def jacobi(a, m):
    if m <= 0:
        raise ValueError("m має бути додатнім")
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


a = int(input("Вкажіть значення a: "))
m = int(input("Вкажіть значення m: "))
print(jacobi(a, m))
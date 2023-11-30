from functools import reduce

# Функція Ейлера
def euler_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

# Функція Мьобіуса
def mobius(n):
    if n == 1:
        return 1
    p = 2
    count = 0
    while p * p <= n:
        if n % p == 0:
            count += 1
            n //= p
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        count += 1
    return -1 if count % 2 else 1

# НСД
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# НСК
def lcm(a, b):
    return a * b // gcd(a, b)

# НСК для набору чисел
def lcm_of_list(numbers):
    return reduce(lcm, numbers)

# Приклад використання
number = 12
numbers_list = [12, 18, 20]

print(f"Функція Ейлера для числа {number}: {euler_phi(number)}")
print(f"Функція Мьобіуса для числа {number}: {mobius(number)}")
print(f"НСК чисел {numbers_list}: {lcm_of_list(numbers_list)}")

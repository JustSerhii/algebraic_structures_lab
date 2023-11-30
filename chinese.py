def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Обернене за модулем не існує')
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    sum = 0
    prod = 1
    for a, n in congruences:
        prod *= n

    for a, n in congruences:
        p = prod // n
        sum += a * mod_inverse(p, n) * p
    return sum % prod

# Приклад використання:
congruences = [(2, 3), (3, 5), (1, 7)] # x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 1 (mod 7)
print(chinese_remainder_theorem(congruences))

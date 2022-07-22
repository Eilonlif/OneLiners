from fastPow import f


def power(a, n):
    if n == 0:
        return 1
    x = power(a, n // 2) ** 2
    if n % 2 == 1:
        x *= a
    return x


print(power(2, 34))
print(f(2, 34))

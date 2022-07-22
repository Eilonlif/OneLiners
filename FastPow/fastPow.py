f = lambda a, n: 1 if n == 0 else f(a, n // 2) ** 2 * a ** (n % 2)

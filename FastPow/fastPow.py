f = lambda a, n: f(a, n // 2) ** 2 * a ** (n % 2) if n else 1

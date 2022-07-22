f = lambda n: (g := lambda a, b, n: g(b, a + b, n - 1) if n else a + b)(0, 1, n - 2) if n - 1 > 0 else n

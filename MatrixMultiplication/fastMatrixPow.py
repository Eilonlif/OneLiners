f = lambda m, n: m if n == 1 else (
    g := (lambda m1, m2: [[sum(a * b for a, b in zip(ra, cb)) for cb in list(zip(*m2))] for ra in m1]))(
    g(t := f(m, n // 2), t), m if n % 2 else [[0 if i != j else 1 for i in range(len(m))] for j in range(len(m))])

f = lambda n: (h := lambda m, k: m if k == 1 else (
    g := (lambda m1, m2: [[sum(a * b for a, b in zip(ra, cb)) for cb in list(zip(*m2))] for ra in m1]))(
    g(t := h(m, k // 2), t), m if k % 2 else [[0 if i != j else 1 for i in range(len(m))] for j in range(len(m))]))(
    [[1, 1], [1, 0]], n - 1)[0][0]

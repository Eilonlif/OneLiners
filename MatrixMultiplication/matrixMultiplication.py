f = lambda m1, m2: [[sum(a * b for a, b in zip(ra, cb)) for cb in list(zip(*m2))] for ra in m1] if len(m1[0]) == len(
    m2) else None

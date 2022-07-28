f = lambda s: s if len(s) == 1 else set(l + p for i, l in enumerate(s) for p in f(s[:i] + s[i + 1:]))
